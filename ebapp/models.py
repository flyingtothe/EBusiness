from django.db import models

# Create your models here.
# 商品表
class Goods(models.Model):
    # 商品 id
    goods_id = models.AutoField(primary_key=True)
    # 商品名称
    goods_name = models.CharField(max_length=50)
    # 类型
    goods_type = models.CharField(max_length=20)
    # 介绍
    goods_introduce = models.CharField(max_length=150, null=True)
    # 保质期
    goods_shelf_life = models.DateField(null=True)
    # 保修期
    goods_warranty = models.DateField(null=True)
    # 产品参数
    goods_product_parameters = models.CharField(max_length=500)
    # 单价
    goods_unit_price = models.FloatField()
    # 库存
    goods_inventory = models.FloatField()
    # 商户id
    merchants_id = models.IntegerField()

# 用户表
class User(models.Model):
    # 用户id
    user_id = models.AutoField(primary_key=True)
    # 账号
    user_account = models.CharField(max_length=50, null=False)
    # 密码
    user_password = models.CharField(max_length=16, null=False)
    # 姓名
    user_name = models.CharField(max_length=10)
    # 注册时间
    user_create = models.DateField(auto_now_add=True)
    # 上次登录时间
    user_last_login = models.DateField(auto_now=True)
    # 昵称
    user_nick_name = models.CharField(max_length=20)
    # 性别
    user_gender = models.CharField(max_length=2)
    # 生日
    user_birthday = models.DateField(null=True)
    # 星座
    user_constellations = models.CharField(null=True)
    # 居住地
    user_address = models.CharField(max_length=30, null=True)
    # 家乡
    user_home_town = models.CharField(max_length=30, null=True)
    # 收货地址
    user_receiving_address = models.CharField(max_length=30)

# 管理员表
class Manager(models.Model):
    # 用户id
    manager_id = models.AutoField(primary_key=True)
    # 账号
    manager_account = models.CharField(max_length=50, null=False)
    # 密码
    manager_password = models.CharField(max_length=16, null=False)
    # 姓名
    manager_name = models.CharField(max_length=10)
    # 注册时间
    manager_create = models.DateField(auto_now_add=True)
    # 上次登录时间
    manager_last_login = models.DateField(auto_now=True)
    # 昵称
    manager_nick_name = models.CharField(max_length=20)
    # 性别
    manager_gender = models.CharField(max_length=2)
    # 居住地
    manager_address = models.CharField(max_length=30, null=True)
    # 权限（0是系统超级管理员，1是商户超管理员，2商户普通管理员）
    manager_access = models.IntegerField()

# 交易记录
class TransactionRecords(models.Model):
    # 交易id
    transaction_id = models.AutoField(primary_key=True)
    # 商品id
    goods_id = models.IntegerField()
    # 用户id
    user_id = models.IntegerField()
    # 交易开始时间
    transaction_create_time = models.DateField(auto_now_add=True)
    # 交易状态
    transaction_type = models.CharField(max_length=2)
    # 交易结束时间
    transaction_finish_time = models.DateField(auto_now=True)
    #商户id
    merchants_id = models.IntegerField()

# 商户表
class Merchants(models.Model):
    # 商户id
    merchants_id = models.AutoField(primary_key=True)
    # 管理员id
    manager_id = models.IntegerField()
    # 商品id
    goods_id = models.IntegerField()
    # 注册时间
    merchants_create_time = models.DateField(auto_now_add=True)
    # 类型（个人 / 企业）
    merchants_type = models.CharField(max_length=10)
    # 地址
    merchants_address = models.CharField(max_length=30)

# 购物车
class ShoppingCart(models.Model):
    # 用户id
    user_id = models.IntegerField(primary_key=True)
    # 商品id
    goods_id = models.IntegerField()
    # 商户id
    merchants_id = models.IntegerField()
    # 添加时间
    shoppingcart_create_time = models.DateField(auto_now_add=True)
    # 商品详情
    goods_product_parameters = models.CharField(max_length=50)

# 订单
class Order(models.Model):
    # 订单id
    order_id = models.AutoField(primary_key=True)
    # 商品id
    goods_id = models.IntegerField()
    # 用户id
    user_id = models.IntegerField(primary_key=True)
    # 商户id
    merchants_id = models.IntegerField()
    # 订单状态
    order_type = models.CharField(max_length=2)

# 库存
class Inventory(models.Model):
    # 商户id
    # 商品id
    # 库存量
    # 补货时间
    # 补货数量
    pass

# 充值记录
class RefillLog(models.Model):
    pass

# 信息
class Message(models.Model):
    pass