from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random,math
from .models import Food
from datetime import datetime
from collections import defaultdict
@csrf_exempt  # 禁用 CSRF 保護，僅用於示例
def my_view(request):
    if request.method == 'GET':
        # data = json.loads(request.body)
        # # 處理數據
        # print(data)
        #selected_dinner = random_choose(data)
        food = Food.objects.all()
        selected_dinner = random_choose(food)
        print(selected_dinner)
        return JsonResponse({'status': 'success', 'data': selected_dinner.name})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def random_choose(data):
    
    return random.choice(data)

def sigmoid_weight(score):
    return 1 / (1 + math.exp(-score))

def pickupDinner(request):
    now = datetime.now()

    # 格式化日期
    formatted_date = now.strftime('%Y-%m-%d')

    #User Input 選取的Tag 跟 現在心情
    pick_up_tag = ["雞肉","麵"] #ToDo: 給使用者選取
    mood = "中性"

    #step1: pickup all food which contains tag that user selected
    pickup_food = set()
    food_tags = []
    data = defaultdict(list)
    
    for tag in pick_up_tag:
        foods = Food.objects.filter(tag__description=tag) #因為tag是外鍵 必須加上__
        food_tag = []
        for food in foods:
            pickup_food.add(food)  
    print(pickup_food)

    #prepare every chosen food that contains user select tag
    for p in pickup_food:
        food_tag = []
        #print(p.tag.all())
        for tag in p.tag.all():            
            if tag.description in pick_up_tag:                
                food_tag.append(tag.description)
        data["tag"].append(food_tag)
    
    print(food_tags)

    # step2: Initial Data of Input model
    
    for i,food in enumerate(pickup_food):
        data["food_name"].append(food.name)
        data["time"].append(formatted_date)
        data["mood"] = mood
        data["label"].append(len(data["tag"][i]))
    print(data)

    #step3 prepare regression LSTM model


    #step4(最終輸入) 把 step3 的輸出值(浮點數) 帶入到 sigmoid 函數
    score = 1.25  #隨便假設 應該由step3得到
    output_list = []
    output_weights = []
    for i,food in enumerate(pickup_food):
        data["food_name"].append(food.name)
        data["time"].append(formatted_date)
        data["mood"] = mood
        data["label"].append(sigmoid_weight(score))
        output_list.append((food.name,sigmoid_weight(score)))
    print(output_list)

    return JsonResponse({'status':'success'})
    pass
    