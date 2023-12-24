from django.shortcuts import render,HttpResponse
from Drone.models import Drone
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
    
def gooddetail(request):
    username = request.session.get('username')
    if username:
        return render(request, 'gooddetail.html', {'username': username})
    else:
        return render(request, "gooddetail.html")
def register(request):
    return render(request, "User/register.html")
def Welcome(request):
    return render(request, "Welcome.html")


def Welcome(request):
    Drone.objects.filter(name='bg')
    img = Drone.objects.all()
    return render(request, 'Welcome.html',{'img':img})