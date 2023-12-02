from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

@csrf_exempt  # 禁用 CSRF 保護，僅用於示例
def my_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # 處理數據
        print(data)
        selected_dinner = random_choose(data)

        return JsonResponse({'status': 'success', 'data': selected_dinner})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def random_choose(data):
    for key,dinner_list in data.items():
        selected_dinner_idx = random.randint(0,len(dinner_list)-1)
    return data["dinner"][selected_dinner_idx]