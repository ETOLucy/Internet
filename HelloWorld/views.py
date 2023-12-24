from django.contrib import messages
from django.shortcuts import get_object_or_404, render,HttpResponse
from Drone.models import Drone

# 示例后端处理（使用 Django 框架）
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Drone.models import Drone
from User.models import Order, Users
from decimal import Decimal
import json



def runoob(request):
    views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]
    return render(request, "runoob.html")
def login(request):
    return render(request, "User/login.html")
def index(request):
    username = request.session.get('username')
    if username:
        return render(request, 'index.html', {'username': username})
    else :
        return render(request, 'index.html')
def draft(request):
    return render(request, "draft.html")
def border(request):
    return render(request, "border.html")
def test(request):
    return render(request, "test.html")
def liushuideng(request):
    return render(request, "liushuideng.html")
def img(request):
    return render(request, "img.html")
def button(request):
    return render(request, "button.html")
def text(request):
    return render(request, "text.html")
# def store(request):
#     return render(request, "store.html")
def store(request):
    drones = Drone.objects.all()
    username = request.session.get('username')
    if username:
        return render(request, 'store.html', {'drones': drones,'username': username})
    else :
        return render(request, 'store.html', {'drones': drones})
    
def store_filter(request):
    category = request.GET.get('category', '')
    if category == '':
        drones_filter = Drone.objects.all()
    else:
        drones_filter = Drone.objects.filter(category=category)

    username = request.session.get('username')
    if username:
        return render(request, 'store.html', {'drones': drones_filter,'username': username})
    else:
        return render(request, 'store.html', {'drones': drones_filter})
    


def chat(request):
    username = request.session.get('username')
    if username:
        return render(request, 'chat.html', {'username': username})
    else:
        return render(request,"chat.html")
    
def profile(request):
    username = request.session.get('username')
    if username:
        return render(request, 'profile.html', {'username': username})
    else:
        return render(request, "profile.html")
    
def gooddetail(request, drone_id):
    drone = get_object_or_404(Drone, pk=drone_id)
    username = request.session.get('username')

    
    # if request.method == 'POST':
    #     data = json.loads(request.body.decode('utf-8'))
        
    #     # 获取价格字段
    #     price = data.get('price', None)
    #     if username is not None:
    #         # 获取用户对象
    #         user = Users.objects.get(username=username)
    #         # 检查用户余额是否足够支付
    #         if user.balance >= price:
    #             # 扣除用户余额
    #             user.balance -= price
    #             # user.save()
    #             # # 创建订单
    #             # order = Order.objects.create(
    #             #     user=request.user,
    #             #     product_id=data['productId'],
    #             #     property1=data['property1'],
    #             #     property2=data['property2'],
    #             #     property3=data['property3'],
    #             #     # 其他订单信息...
    #             #     price=price,
    #             # )
    #             return JsonResponse({'status': 'success', 'message': 'Payment processed successfully'})
            
    #         else:
    #             return JsonResponse({'status': 'error', 'message': '余额不足'})
    #     else:
    #         return JsonResponse({'status': 'error', 'message': '请先登录!'})


    if username:
        return render(request, 'gooddetail.html', {'drone': drone, 'username': username})
    else:
        return render(request, "gooddetail.html", {'drone': drone, 'username': username})
def register(request):
    return render(request, "User/register.html")
def Welcome(request):
    return render(request, "Welcome.html")


def Welcome(request):
    Drone.objects.filter(name='bg')
    img = Drone.objects.all()
    return render(request, 'Welcome.html',{'img':img})

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        # 获取价格字段
        price = data.get('price', None)
        # 获取当前登录用户的ID
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            # 获取用户对象
            user = Users.objects.get(id=user_id)
            # 检查用户余额是否足够支付
            if user.balance >= price:
                # 扣除用户余额
                user.balance -= price
                user.save()
                # 创建订单
                order = Order.objects.create(
                    user=request.user,
                    product_id=data['productId'],
                    property1=data['property1'],
                    property2=data['property2'],
                    property3=data['property3'],
                    # 其他订单信息...
                    price=price,
                )
                return JsonResponse({'status': 'success', 'message': 'Payment processed successfully'})
            
            else:
                return JsonResponse({'status': 'error', 'message': '余额不足'})
        else:
            return JsonResponse({'status': 'error', 'message': '请先登录!'})
    return JsonResponse({'status': 'error', 'message': '出错!'})