ITEMS_DATA = {
    "items": {
        "redJewel": {
            "cls": "items",
            "name": "红宝石",
            "text": "'Your Attack+'+RED_JEWEL*",
            "num": 1,
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
            "num": 1,
            "weight": 10
        },
        "expPotion": {
            "cls": "items",
            "name": "经验药水",
            "text": "'Your EXP+'+EXP_POTION*",
            "num": 1,
            "weight": 10
        },
        "coin": {
            "cls": "constants",
            "name": "lucky coin",
            "text": "持有时打败怪物可得双倍金币",
            "weight": 1
        },
    },
    "itemEffect": {
        "redJewel": "self.Attack += RED_JEWEL*",
        "blueJewel": "self.Defend += BLUE_JEWEL*",
        "redPotion": "self.HealthPoint += RED_POTION*",
        "expPotion": "self.Experience += EXP_POTION*",
    }
}
