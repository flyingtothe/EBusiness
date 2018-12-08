from django.db import models

# Create your models here.
# 商品表
class Goods(models.Model):

    name = models.CharField(max_length=128)         # 商品名称
    type = models.CharField(max_length=64)          # 类型
    introduce = models.TextField()                  # 介绍
    shelf_life = models.DateField(blank=True)       # 保质期
    warranty = models.DateField(blank=True)         # 保修期
    product_param = models.TextField()              # 产品参数
    price = models.FloatField()                     # 单价
    inventory = models.FloatField()                 # 库存
    # 商户id
    my_merchants = models.ManyToManyField(to='Merchants')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

# 用户表
class Users(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    account = models.CharField(max_length=50, unique=True)                  # 账号
    password = models.CharField(max_length=256)                             # 密码
    c_time = models.DateTimeField(auto_now_add=True)                        # 注册时间
    nick_name = models.CharField(max_length=20)                             # 昵称
    sex = models.CharField(max_length=32, choices=gender, default="男")     # 性别
    birth = models.DateField(null=True)                                     # 出生日期
    address = models.CharField(max_length=30)                               # 居住地
    receive_address = models.CharField(max_length=30)                       # 收货地址

    def __str__(self):
        return self.account

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

# 管理员表
class Managers(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    aces = (
        ('o_manager', '订单管理员'),
        ('t_manager', '交易管理员'),
        ('s_manager', '商户管理员'),
    )

    account = models.CharField(max_length=50, unique=True)                        # 账号
    name = models.CharField(max_length=10)                                        # 姓名
    password = models.CharField(max_length=256)                                   # 密码
    c_time = models.DateTimeField(auto_now_add=True)                              # 注册时间
    sex = models.CharField(max_length=32, choices=gender, default="男")           # 性别
    address = models.CharField(max_length=30)                                     # 居住地
    access = models.CharField(max_length=32, choices=aces, default="订单管理员")  # 权限（0是系统超级管理员，1是商户超管理员，2商户普通管理员）

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "管理员"
        verbose_name_plural = "管理员"

# 交易记录
class TransactionRecords(models.Model):

    types = (
        ('start', '交易开始'),
        ('finish', '交易结束'),
    )

    my_goods = models.ForeignKey(to='Goods', on_delete=models.CASCADE)           # 商品
    my_user = models.ManyToManyField(to='Users')                                 # 用户
    c_time = models.DateField(auto_now_add=True)                                 # 交易开始时间
    type = models.CharField(max_length=32, choices=types, default="交易结束")    # 交易状态
    f_time = models.DateField(auto_now=True)                                     # 交易结束时间
    my_merchants = models.ManyToManyField(to='Merchants')                        # 商户id

    def __str__(self):
        return self.type

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "交易记录"
        verbose_name_plural = "交易记录"

# 商户表
class Merchants(models.Model):

    name = models.CharField(max_length=50)                                   # 姓名
    my_goods = models.ForeignKey(to='Goods', on_delete=models.CASCADE)       # 商品
    c_time = models.DateField(auto_now_add=True)                             # 注册时间
    type = models.CharField(max_length=10)                                   # 类型（个人 / 企业）
    my_manager = models.ForeignKey(to='Managers', on_delete=models.CASCADE)  # 管理员id
    address = models.CharField(max_length=30)                                # 地址

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "商户"
        verbose_name_plural = "商户"

# 购物车
class ShoppingCart(models.Model):

    my_user = models.ManyToManyField(to='Users')            # 用户
    my_goods = models.ManyToManyField(to='Goods')           # 商品
    my_merchants = models.ManyToManyField(to='Merchants')   # 商户
    add_time = models.DateField(auto_now_add=True)          # 添加时间
    count = models.IntegerField()                           # 数量

    class Meta:
        ordering = ["-add_time"]
        verbose_name = "购物车"
        verbose_name_plural = "购物车"

# 订单
class Order(models.Model):

    types = (
        ('start', '订单开始'),
        ('finish', '订单结束'),
    )

    my_goods = models.ManyToManyField(to='Goods')                               # 商品
    my_user = models.ManyToManyField(to='Users')                                # 用户
    my_merchants = models.ManyToManyField(to='Merchants')                       # 商户
    type = models.CharField(max_length=32, choices=types, default="交易结束")   # 订单状态
    c_time = models.DateField(auto_now_add=True)                                # 交易开始时间
    f_time = models.DateField(auto_now=True)                                    # 交易结束时间

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "订单"
        verbose_name_plural = "订单"

# 库存
# class Inventory(models.Model):
#     # 商户id
#     # 商品id
#     # 库存量
#     # 补货时间
#     # 补货数量
#     pass
#
# # 充值记录
# class RefillLog(models.Model):
#     pass
#
# # 信息
# class Message(models.Model):
#     pass