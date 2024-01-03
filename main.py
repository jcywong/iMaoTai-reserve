import datetime
import logging
import os
import sys
import config
import process
import notify

DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
TODAY = datetime.date.today().strftime("%Y%m%d")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
                    stream=sys.stdout,
                    datefmt=DATE_FORMAT)

print(r'''
**************************************
    欢迎使用i茅台自动预约工具
**************************************
''')

process.get_current_session_id()

s_title = '茅台预约成功'
s_content = ""

users_list = []


def get_users():
    try:
        if "mao_user" in os.environ:
            users = os.environ["mao_user"]
            print(users)
            users = users.split('&')
            if len(users) != 0:
                # user : mobile=xxx, userid=xxx,token=xxx, province=xxx , city=xxx, lat=xxx,lng=xxx
                for user in users:
                    user = user.split(',')
                    user_info = {"mobile": user[0].split('=')[1].replace(' ', ''),
                                 "userId": user[1].split('=')[1].replace(' ', ''),
                                 "token": user[2].split('=')[1].replace(' ', ''),
                                 "province": user[3].split('=')[1].replace(' ', ''),
                                 "city": user[4].split('=')[1].replace(' ', ''),
                                 "lat": user[5].split('=')[1].replace(' ', ''),
                                 "lng": user[6].split('=')[1].replace(' ', '')}
                    users_list.append(user_info)
    except Exception as e:
        print(e)


if len(users_list) == 0:
    get_users()
    if len(users_list) == 0:
        logging.error("未配置用户信息")
        sys.exit(1)

for user in users_list:
    mobile = user["mobile"]
    token = user["token"]
    userId = user["userId"]
    province = user["province"]
    city = user["city"]
    lat = user["lat"]
    lng = user["lng"]

    p_c_map, source_data = process.get_map(lat=lat, lng=lng)

    process.UserId = userId
    process.TOKEN = token
    process.init_headers(user_id=userId, token=token, lng=lng, lat=lat)
    # 根据配置中，要预约的商品ID，城市 进行自动预约
    try:
        for item in config.ITEM_CODES:
            max_shop_id = process.get_location_count(province=province,
                                                     city=city,
                                                     item_code=item,
                                                     p_c_map=p_c_map,
                                                     source_data=source_data,
                                                     lat=lat,
                                                     lng=lng)
            # print(f'max shop id : {max_shop_id}')
            if max_shop_id == '0':
                continue
            shop_info = source_data.get(str(max_shop_id))
            title = config.ITEM_MAP.get(item)
            shopInfo = f'商品:{title};门店:{shop_info["name"]}'
            logging.info(shopInfo)
            reservation_params = process.act_params(max_shop_id, item)
            # 核心预约步骤
            r_success, r_content = process.reservation(reservation_params, mobile)
            # 为了防止漏掉推送异常，所有只要有一个异常，标题就显示失败
            if not r_success:
                s_title = '！！失败！！茅台预约'
            s_content = s_content + r_content + shopInfo + "\n"
            # 领取小茅运和耐力值
            process.getUserEnergyAward(mobile)
    except BaseException as e:
        print(e)
        logging.error(e)

# 推送消息
notify.bark(s_title, s_content)

