from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from .models import Food
@csrf_exempt  # 禁用 CSRF 保護，僅用於示例
def my_view(request):
    if request.method == 'GET':
        # data = json.loads(request.body)
        # # 處理數據
        # print(data)
        #selected_dinner = random_choose(data)
        food = Food.objects.all()
        selected_dinner = random_choose(food)
        
        return JsonResponse({'status': 'success', 'data': selected_dinner.name})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def random_choose(data):
    
    return random.choice(data)
    