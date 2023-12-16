import random
import pandas as pd
# # Expanded set of unique food items (50 different kinds) with more Chinese dishes
# unique_foods_with_chinese = [
#     "火鍋", "鴨肉飯", "魯肉飯", "義大利麵", "四川麻辣燙", "北京烤鴨", "粵式炒飯", "宮保雞丁", "麻婆豆腐", "上海小籠包",
#     "辣子雞", "鹵水豆腐", "蘭州拉麵", "酸菜魚", "紅燒肉", "清蒸魚", "麵筋", "鹹鴨蛋", "糖醋里脊", "豆腐腦",
#     "壽司", "泰式炒麵", "墨西哥捲餅", "印度咖喱", "中式炒飯", "日式拉麵", "法式薄餅", "西班牙海鮮飯", "土耳其烤肉", "越南河粉",
#     "希臘沙拉", "韓國烤肉", "俄羅斯紅菜湯", "英式炸魚薯條", "美式漢堡", "波蘭餃子", "埃及豆泥", "巴西燒烤", "加拿大楓糖餅", "阿根廷牛排",
#     "比利時巧克力", "瑞典肉丸", "丹麥熏鯖魚", "秘魯刺身", "摩洛哥燉肉", "尼泊爾咖哩", "澳洲維京牛排", "新西蘭羊排", "意式千層麵", "匈牙利燉牛肉"
# ]

# # Generating a list of 50 items with unique food names including more Chinese dishes
# unique_food_data_list_with_chinese = []

# for food in unique_foods_with_chinese:
#     rating_choice = random.randint(1, 10)  # Ratings from 1 to 10
#     happiness_choice = random.choice([0, 1])  # Happiness 0 or 1

#     unique_food_data_list_with_chinese.append({
#         "food": food,
#         "rating": rating_choice,
#         "happiness": happiness_choice
#     })

# #print(unique_food_data_list_with_chinese)  # Displaying the first 5 items for brevity
# df = pd.DataFrame(unique_food_data_list_with_chinese)
# print(df)



food1 =  [
    "火鍋", "鴨肉飯", "魯肉飯", "義大利麵", "糖醋排骨", "宮保雞丁", "餃子", "北京烤鴨", 
    "春卷", "魚香茄子", "紅燒肉", "辣子雞", "麻婆豆腐", "撈麵", "炒飯", "牛肉麵", 
    "蘿蔔糕", "叉燒", "包子", "湯圓", "粽子", "蛋撻", "豆漿", "油條", "粉蒸肉", 
    "鹵水豆腐", "涼拌黃瓜", "酸辣湯", "燒賣", "鹹酥雞", "雞絲麵", "蔥油餅", "糖不甩", 
    "椒鹽排骨", "小籠包", "蝦餃", "蒸魚", "牛肉丸", "炒馬鈴薯絲", "蒜泥白肉", 
    "酸菜魚", "豆腐花", "酸辣粉", "海鮮煲", "五香豬蹄", "麻辣燙", "螞蟻上樹", "土豆粉", "涼皮"
]
rating1 = [
    9, 3, 5, 9, 7, 8, 6, 10, 
    7, 5, 8, 6, 9, 4, 7, 8, 
    5, 7, 6, 9, 5, 6, 4, 3, 8, 
    7, 6, 8, 7, 5, 6, 4, 3, 8, 
    9, 8, 7, 6, 7, 6, 8, 7, 5, 
    6, 9, 4, 8, 7, 6, 5
]
happiness1 = [
    0, 1, 1, 0, 1, 1, 0, 1, 
    0, 1, 1, 0, 1, 0, 1, 1, 
    0, 1, 0, 1, 0, 1, 0, 0, 1, 
    1, 0, 1, 0, 1, 0, 1, 0, 1, 
    1, 0, 1, 0, 1, 0, 1, 1, 0, 
    1, 0, 1, 0, 1, 0, 1
]



food2 = [
    "扬州炒饭", "炒河粉", "蒸饺", "鱼香肉丝", "馄饨", "宫保鸡丁", "牛肉面", "辣白菜", 
    "糖醋鱼", "炸酱面", "麻辣烫", "叉烧包", "豆花", "凉面", "芝麻鸡", "香辣蟹", 
    "肉夹馍", "煎饼果子", "锅贴", "花卷", "鱼头豆腐汤", "豉汁排骨", "糖醋藕", "炸豆腐", 
    "烤鱼", "海带汤", "烧茄子", "红烧鱼", "烤鸭", "酱牛肉", "炒面", "杂粮煎饼", 
    "糯米鸡", "烤串", "烤肉", "蛋炒饭", "牛肉丸", "炖鸡", "炒豆芽", "豆腐乳", 
    "冬瓜汤", "鸡蛋饼", "韭菜盒子", "芹菜炒肉", "干锅菜花", "白切鸡", "卤肉饭", "菠菜汤", 
    "炒土豆丝", "糖醋排骨"
]
# rating2= [
#     8, 7, 6, 8, 5, 9, 7, 6, 
#     7, 6, 8, 7, 5, 4, 8, 9, 
#     6, 7, 5, 4, 8, 7, 6, 5, 
#     8, 6, 7, 8, 9, 7, 5, 6, 
#     7, 8, 9, 7, 6, 5, 4, 3, 
#     8, 7, 6, 5, 4, 8, 7, 6, 
#     7, 8
# ]
# happiness2= [
#     1, 0, 1, 0, 1, 1, 0, 1, 
#     0, 1, 0, 1, 1, 0, 1, 1, 
#     0, 1, 0, 1, 0, 1, 0, 1, 
#     0, 1, 1, 0, 1, 1, 0, 1, 
#     0, 1, 1, 0, 1, 0, 1, 0, 
#     1, 0, 1, 0, 1, 0, 1, 1, 
#     0, 1
# ]

food3 = list(food1) + food2
# rating3 = list(rating1) + rating2
# happiness3 = list(happiness1) + happiness2
rating3 = []
happiness3 = []
for food in food3:
    rating_choice = random.randint(1, 10)  # Ratings from 1 to 10
    happiness_choice = random.choice([0, 1])  # Happiness 0 or 1
    rating3.append(rating_choice)
    happiness3.append(happiness_choice)
grades = {
    "food": food3,
    "rating": rating3,
    "happiness": happiness3
}

df = pd.DataFrame(grades)
csv_file_path = './Chinese_Foods.csv'
#df.to_csv(csv_file_path, index=False,encoding="utf-8")

a = pd.read_csv("./Chinese_Food.csv")
print(a[a["happiness"]==1])