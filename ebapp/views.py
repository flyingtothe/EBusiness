from django.shortcuts import render, redirect, reverse
from django.forms.models import model_to_dict
from ebapp import models, forms
import hashlib

# Create your views here.

def hash_code(s, salt='nicai'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

# 主页
def Index(request):
    good = models.Goods.objects.filter()
    return render(request, 'index.html', {'good': good})

# 登陆
def Login(request):
    if request.session.get('is_login', None):
        return redirect(reverse(viewname='my_index'))
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            account = login_form.cleaned_data['account']
            password = login_form.cleaned_data['password']
            try:
                user = models.Users.objects.get(account=account)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['id'] = user.id
                    request.session['account'] = user.account
                    request.session['nick_name'] = user.nick_name
                    return redirect(reverse(viewname='my_index'))
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())

# 注册
def Regist(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect(reverse(viewname='my_index'))
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            account = request.POST.get('account')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            sex = request.POST.get('sex')
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_account_user = models.Users.objects.filter(account=account)
                if same_account_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                new_user = models.Users()
                new_user.account = account
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.sex = sex
                new_user.save()
                return redirect(reverse(viewname='my_login'))  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())

# 登出
def Logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect(reverse(viewname='my_index'))
    request.session.flush()
    return redirect(reverse(viewname='my_index'))