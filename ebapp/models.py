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
    goods_introduce = models.CharField(max_length=150)
    # 保质期
    goods_shelf_life = models.DateField(blank=True)
    # 保修期
    goods_warranty = models.DateField()
    # 产品参数
    goods_product_parameters = models.CharField(max_length=500)
    # 单价
    goods_unit_price = models.FloatField()
    # 库存
    goods_inventory = models.FloatField()
    # 商户id
    my_merchants = models.ManyToManyField(to='Merchants')

    def __str__(self):
        return self.goods_name

# 用户表
class Users(models.Model):
    # 用户id
    user_id = models.AutoField(primary_key=True)
    # 账号
    user_account = models.CharField(max_length=50)
    # 密码
    user_password = models.CharField(max_length=16)
    # 姓名
    user_name = models.CharField(max_length=10)
    # 注册时间
    user_create = models.DateField(auto_now_add=True)
    # 昵称
    user_nick_name = models.CharField(max_length=20)
    # 性别
    user_gender = models.CharField(max_length=2)
    # 生日
    user_birthday = models.DateField()
    # 居住地
    user_address = models.CharField(max_length=30)
    # 收货地址
    user_receiving_address = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

# 管理员表
class Managers(models.Model):
    # 用户id
    manager_id = models.AutoField(primary_key=True)
    # 账号
    manager_account = models.CharField(max_length=50)
    # 密码
    manager_password = models.CharField(max_length=16)
    # 姓名
    manager_name = models.CharField(max_length=10)
    # 注册时间
    manager_create = models.DateField(auto_now_add=True)
    # 性别
    manager_gender = models.CharField(max_length=2)
    # 居住地
    manager_address = models.CharField(max_length=30)
    # 权限（0是系统超级管理员，1是商户超管理员，2商户普通管理员）
    manager_access = models.IntegerField()

    def __str__(self):
        return self.manager_name

# 交易记录
class TransactionRecords(models.Model):
    # 交易id
    transaction_id = models.AutoField(primary_key=True)
    # 商品id
    my_goods = models.ForeignKey(to='Goods', on_delete=models.CASCADE)
    # 用户id
    my_user = models.ManyToManyField(to='Users')
    # 交易开始时间
    transaction_create_time = models.DateField(auto_now_add=True)
    # 交易状态
    transaction_type = models.CharField(max_length=2)
    # 交易结束时间
    transaction_finish_time = models.DateField(auto_now=True)
    # 商户id
    my_merchants = models.ManyToManyField(to='Merchants')

# 商户表
class Merchants(models.Model):
    # 商户id
    merchants_id = models.AutoField(primary_key=True)
    # 商户名称
    merchants_name = models.CharField(max_length=50)
    # 管理员id
    my_manager = models.ForeignKey(to='Managers', to_field='manager_id', on_delete=models.CASCADE)
    # 商品id
    my_goods = models.ManyToManyField(to='Goods')
    # 注册时间
    merchants_create_time = models.DateField(auto_now_add=True)
    # 类型（个人 / 企业）
    merchants_type = models.CharField(max_length=10)
    # 地址
    merchants_address = models.CharField(max_length=30)

    def __str__(self):
        return self.merchants_name

# 购物车
class ShoppingCart(models.Model):
    # 用户id
    my_user = models.ManyToManyField(to='Users')
    # 商品id
    my_goods = models.ManyToManyField(to='Goods')
    # 商户id
    my_merchants = models.ManyToManyField(to='Merchants')
    # 添加时间
    shoppingcart_create_time = models.DateField(auto_now_add=True)
    # 商品详情
    goods_product_parameters = models.CharField(max_length=50)

# 订单
class Order(models.Model):
    # 订单id
    order_id = models.AutoField(primary_key=True)
    # 商品id
    my_goods = models.ManyToManyField(to='Goods')
    # 用户id
    my_user = models.ManyToManyField(to='Users')
    # 商户id
    my_merchants = models.ManyToManyField(to='Merchants')
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