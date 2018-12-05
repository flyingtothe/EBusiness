from django.shortcuts import render

# Create your views here.

# 登陆
def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

# 注册
def Regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')