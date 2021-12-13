# 定义地图大小，房间布置
# Define map size
WIDTH = 4
HEIGHT = 4
# 随机生成地图路径时需要转化
# Map paths need to be transformed when they are generated randomly
Width = WIDTH * 2 + 1
Height = HEIGHT * 2 + 1
# Show map at first
SHOW_MAP = True
# Set Size of Map in Gui
MapSize = 50
# 日志输出等级（DEBUG, INFO, WARNING, ERROR, CRITICAL）
LOGGING_LEVEL = "INFO"

Name = "DJ"
Gold = 50
# Monster basic attributes
Mon_Attack = 10
Mon_Defend = 10
Mon_HealthPoint = 100
# Hero basic attributes
Hero_Attack = 20
Hero_Defend = 20
Hero_HealthPoint = 100
Level = 1
Experience = 0
MaxWeight = 100
# 升级需要的基础经验
# Basic experience for upgrading
LevelNeed = 50
# Base Monster Exp give
MonsterExp = 20
# The probability of building a shop
Shop_Rate = 1

dirsx = [1, 0, 0, -1]
dirsy = [0, -1, 1, 0]
dir = ["south", "west", "east", "north"]
CommandWords = ['help', 'go', 'hero', 'quit', 'list', 'use', 'pick', 'throw', 'fight', 'buy']

# 怪物名字
MonsterName = {
    'Level1': ['Spider', 'Wolf', 'Bat', 'Snake'],
    'Level2': ['Zombie', 'Blaze', 'Witch', 'butcher'],
    'Level3': ['Giant', 'Wither', 'hellhound'],
    'Level30': ['devil']
}
# 物品效果
# Item effect
RED_JEWEL = 10
BLUE_JEWEL = 10
RED_POTION = 50
EXP_POTION = 10

# 图片路径
ImageDict = {'wall': 'wall.png', 'Hero01': 'Hero01.png', 'Hero02': 'Hero02.png', 'road': 'road01.png',
             'room01': 'room01.png', 'room02': 'room02.png', 'room03': 'room03.png', 'Head01': 'Head01.png',
             'Head02': 'Head02.png', 'Head03': 'Head03.png', 'Head04': 'Head04.png', 'Head05': 'Head05.png',
             'redJewel': 'redJewel.png', 'blueJewel': 'blueJewel.png', 'redPotion': 'redPotion.png',
             'expPotion': 'expPotion.png'}

# 初始背包
Dict = {
    "redJewel": {
        "cls": "items",
        "name": "红宝石",
        "text": "'Your Attack+'+RED_JEWEL*",
        "num": 0,
        "weight": 3
    },
    "blueJewel": {
        "cls": "items",
        "name": "蓝宝石",
        "text": "'Your Defend+'+BLUE_JEWEL*",
        "num": 1,
        "weight": 3
    },
    "redPotion": {
        "cls": "items",
        "name": "红药水",
        "text": "'Your HP+'+RED_POTION*",
        "num": 2,
        "weight": 10
    },
    "expPotion": {
        "cls": "items",
        "name": "经验药水",
        "text": "'Your EXP+'+EXP_POTION*",
        "num": 3,
        "weight": 10
    }
}

Shop_Dict = {
    "redJewel": {
        "cls": "items",
        "name": "红宝石",
        "text": "'Your Attack+'+RED_JEWEL*",
        "price": 10,
        "num": 1,
        "weight": 3
    },
    "blueJewel": {
        "cls": "items",
        "name": "蓝宝石",
        "text": "'Your Defend+'+BLUE_JEWEL*",
        "price": 10,
        "num": 1,
        "weight": 3
    },
    "redPotion": {
        "cls": "items",
        "name": "红药水",
        "text": "'Your HP+'+RED_POTION*",
        "price": 50,
        "num": 1,
        "weight": 10
    },
    "expPotion": {
        "cls": "items",
        "name": "经验药水",
        "text": "'Your EXP+'+EXP_POTION*",
        "price": 50,
        "num": 1,
        "weight": 10
    }
}

## 定义颜色
# 红色系
RED = (255, 0, 0)
DARKRED = (139, 0, 0)
# 橙色系
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
DARKORANGE = (255, 140, 0)
# 黄色系
LIGHTYELLOW = (255, 255, 224)
YELLOW = (255, 255, 0)
# 绿色系
LIMEGREEN = (50, 205, 50)
GREEN = (0, 255, 0)
SPRINGGREEN = (0, 255, 127)
SEAGREEN = (46, 139, 87)
OLIVE = (128, 128, 0)
# 青色系
CYAN = (0, 255, 255)
DARKCYAN = (0, 139, 139)
# 蓝色系
LIGHTSKYBLUE = (135, 206, 250)
SKYBLUE = (135, 206, 235)
DEEPSKYBLUE = (0, 191, 255)
LIGHTSTEELBLUE = (176, 196, 222)
BLUE = (0, 0, 255)
MEDIUMBLUE = (0, 0, 205)
DARKBLUE = (0, 0, 139)
# 紫色系
VIOLET = (238, 130, 238)
FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)
INDIGO = (75, 0, 130)
# 粉色系
PINK = (255, 192, 203)
LIGHTPINK = (255, 182, 193)
DEEPPINK = (255, 20, 147)
# 白色系
WHITE = (255, 255, 255)
SNOW = (255, 250, 250)
AZURE = (240, 255, 255)
# 灰色系
LIGHTGRAY = (211, 211, 211)
SILVER = (192, 192, 192)
DARKGRAY = (169, 169, 169)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
# 棕色系
WHEAT = (245, 222, 179)
CHOCOLATE = (210, 105, 30)
BROWN = (165, 42, 42)
# --- 基本常数 END ---
