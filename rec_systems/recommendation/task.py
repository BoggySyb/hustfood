import math

from django.core.cache import cache
from rec_systems.models.log.log import Log
from rec_systems.models.appuser.appuser import AppUser
from rec_systems.models.food.food import Food
from datetime import datetime, timedelta
from collections import defaultdict
import pytz

def get_hot_list():
    wall = datetime.now() - timedelta(days=30)
    wall = wall.replace(tzinfo=pytz.timezone('Asia/Shanghai'))

    cnt_food_hot = defaultdict(int)
    logs = Log.objects.all().filter(action_time__gt=wall)
    for log in logs:
        if log.action_type == "click":
            cnt_food_hot[log.food_id] += 1
        elif log.action_type == "like" or log.action_type == "collection":
            cnt_food_hot[log.food_id] += 2
        else:
            cnt_food_hot[log.food_id] -= 0.5

    last_month_hot_food_list = []
    food_hot_rank = sorted(cnt_food_hot.items(), key=lambda x: x[1], reverse=True)
    for food_id, _ in food_hot_rank[:10]:
        last_month_hot_food_list.append(food_id)

    cache.delete("hot_food_list")
    cache.set("hot_food_list", last_month_hot_food_list, 31*24*60*60)


def get_item_users_dict(user_set):
    wall = datetime.now() - timedelta(days=1)
    wall = wall.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
    today_logs = Log.objects.all().filter(user_name__in=user_set, action_time__gt=wall)
    item_users_dict = defaultdict(dict)
    for log in today_logs:
        item_id, user_id, score = log.food_id, log.user_name, 0
        if log.action_type == "click": score = 1
        elif log.action_type == "like" or log.action_type == "unlike": score = 2
        if score:
            item_users_dict[item_id].setdefault(user_id, 0)
            item_users_dict[item_id][user_id] += score
    return item_users_dict


def calc_user_sims(user_set):
    item_users_dict = get_item_users_dict(user_set)
    user_cnt = defaultdict(int)
    u2u_sim = defaultdict(dict)

    for item_id, user_list in item_users_dict.items():
        for user_i, score_i in user_list.items():
            user_cnt[user_i] += 1
            for user_j, score_j in user_list.items():
                if user_i == user_j:
                    continue
                u2u_sim[user_i].setdefault(user_j, 0)
                u2u_sim[user_i][user_j] += score_i * score_j

    u2u_sim_ = u2u_sim.copy()
    for user_i, rel_users in u2u_sim.items():
        for user_j, wij in rel_users.items():
            u2u_sim_[user_i][user_j] = wij / math.log1p(user_cnt[user_i] * user_cnt[user_j])
    return u2u_sim_


def UserCF(user_id, u2u_sim):
    user_items_lastk = cache.get('user_items_lastk')
    item_rank = {}
    for rel_user, w in u2u_sim[user_id].items():
        for item_id in user_items_lastk[rel_user]:
            item_rank.setdefault(item_id, 0)
            item_rank[item_id] += w
    item_rank = sorted(item_rank.items(), key=lambda x: x[1], reverse=True)

    rec_list = []
    for item, _ in item_rank:
        if len(rec_list) == 10: break
        rec_list.append(item)
    return rec_list


def generate_recommendation():
    df = cache.get('user_rec_list')
    old_users = set()

    appusers = AppUser.objects.all()
    for appuser in appusers:
        if appuser.is_new_user: # 如果是新用户，通过冷启动规则推荐
            near_foods = Food.objects.all().filter(position=appuser.near_pos)
            favour_foods1 = Food.objects.all().filter(class1=appuser.favour_class)
            favour_foods2 = Food.objects.all().filter(class2=appuser.favour_class)
            food_list = []
            food_list += [food.food_id for food in near_foods]
            food_list += [food.food_id for food in favour_foods1]
            food_list += [food.food_id for food in favour_foods2]
            df[appuser.user.username] = food_list
        else: # 老用户则通过 UserCF 推荐
            old_users.add(appuser.user.username)

    u2u_sim = calc_user_sims(old_users)
    for user_id in old_users:
        df[user_id] = UserCF(user_id, u2u_sim)

    cache.set('user_rec_list', df, timeout=None)