# import pandas as pd

# # 示例数据：食物、评分和权重
# # data = {
# #     'food': ['火鍋', '鴨肉飯', '魯肉飯', '義大利麵', '壽司'],
# #     'rating': [4.5, 4.0, 4.1, 4.2, 4.7],  # 评分
# #     'weight': [0.025, 0.9, 0.025, 0.025, 0.025]          # 权重
# # }
# # data = {
# #     'food': ['火鍋', '鴨肉飯', '魯肉飯', '義大利麵', '壽司'],
# #     'rating': [4.5, 4.0, 4.1, 4.2, 4.7],  # 评分
# #     'weight': [0.3, 0.1, 0.05, 0.05, 0.5]          # 权重
# # } #火鍋會贏
# data = {
#     'food': ['火鍋', '鴨肉飯', '魯肉飯', '義大利麵', '壽司'],
#     'rating': [9, 6, 6, 2, 9],  # 评分
#     'weight': [0.3, 0.1, 0.05, 0.05, 0.5]          # 权重
# } #rating同分怎麼辦

# df = pd.DataFrame(data)

# # 计算加权评分
# df['weighted_rating'] = df['rating'] * df['weight']
# total_weight = df['weight'].sum()
# weighted_score = df['weighted_rating'].sum() / total_weight

# # 显示加权评分结果
# print(weighted_score)

import random
 
sampleList = ['火鍋', '鴨肉飯', '魯肉飯', '義大利麵', '壽司']
for i in range(10):
    randomList = random.choices(
    sampleList,  weights=(0.52, 0.4, 0.4, 0.4, 0.52), k=5) # weights=(80, 30, 30, 30, 70) 0.8
    
    print(randomList)