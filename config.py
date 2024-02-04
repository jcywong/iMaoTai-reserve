import os

'''
*********** 商品配置 ***********
'''
ITEM_MAP = {
    "10941": "53%vol 500ml贵州茅台酒（甲辰龙年）",
    "10942": "53%vol 375ml×2贵州茅台酒（甲辰龙年）",
    "10056": "53%vol 500ml茅台1935",
    "2478": "53%vol 500ml贵州茅台酒（珍品）"
}

ITEM_CODES = ['10941', '10942']   # 需要预约的商品(默认只预约2个赚钱的茅子)


'''
*********** 地图配置 ***********
获取地点信息,这里用的高德api,需要自己去高德开发者平台申请自己的key
'''
# AMAP_KEY = os.environ.get("GAODE_KEY")
AMAP_KEY = "71c63xxxxxxxx5194f"


'''
*********** 个人账户认证配置 ***********
个人用户 credentials 路径
不配置,使用默认路径,在项目目录中;如果需要配置,你自己应该也会配置路径
例如： CREDENTIALS_PATH = './myConfig/credentials'
'''
# CREDENTIALS_PATH = None
CREDENTIALS_PATH = './credentials'


'''
*********** 预约规则配置 ************
因为目前支持代提的还是少,所以建议默认预约最近的门店
'''
_RULES = {
    'MIN_DISTANCE': 0,   # 预约你的位置最近的门店
    'MAX_SALES': 1,      # 预约本市出货量最大的门店
}
RESERVE_RULE = 0         # 在这里配置你的规则，只能选择其中一个
