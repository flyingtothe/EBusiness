from django.shortcuts import render, redirect
from ebapp.models import Users

# Create your views here.

# 登陆
def Login(request):
    return render(request, 'login.html')

# 注册
def Regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    else:
        print(request.session.get('account'))
        ct = {}
        ct['user_account'] = request.POST['account']
        return redirect(request, 'login.html', context=ct)