from django.db import models

# Create your models here.

class SlideShow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=150)
    sort = models.CharField(max_length=20)
    class Meta:
        db_table = "slideshows"
        ordering = ['sort']

# class MainDescrioption(models.Model):
#     pass
'''(name, longName, storeNums, specifics, sort, brandId, brandName, safeDay, safeUnit, marketPrice, keywords, safeUnitDesc, categoryId, childId, productId, price, img, isDelete) '''
class Product(models.Model):
    name = models.CharField(max_length=100)
    longName = models.CharField(max_length=150)
    storeNums = models.CharField(max_length=20)
    specifics = models.CharField(max_length=20)
    sort = models.CharField(max_length=20)
    brandId = models.CharField(max_length=20)
    brandName = models.CharField(max_length=200)
    safeDay = models.CharField(max_length=20)
    safeUnit= models.CharField(max_length=20)
    # salesVolume=models.CharField(max_length=20)
    marketPrice = models.CharField(max_length=20)
    keywords = models.CharField(max_length=100)
    safeUnitDesc = models.CharField(max_length=20)
    categoryId = models.CharField(max_length=20)
    childId = models.CharField(max_length=20)
    productId = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table="products"
        ordering=["sort"]
class Maindescription(models.Model):
    categoryId = models.CharField(max_length=20)
    categoryName = models.CharField(max_length=40)
    sort = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    product1 = models.CharField(max_length=20)
    product2 = models.CharField(max_length=20)
    product3 = models.CharField(max_length=20)

    class Meta():
        db_table="mainDescriptions"
        ordering=["sort"]
#分组
class CategoriesGroup(models.Model):
    name = models.CharField(max_length=150)
    categorieId =models.CharField(max_length=20)
    sort = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table="categoriegroups"
        ordering=["sort"]
class ChildGroup(models.Model):
    cid = models.CharField(max_length=20)
    name =models.CharField(max_length=50)
    sort = models.CharField(max_length=20)
    categorie = models.ForeignKey(CategoriesGroup)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table="childgroups"
        ordering=["sort"]

class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(isDelete=False)
class User(models.Model):
    objects = UserManager()
    phoneNum = models.CharField(max_length=20, primary_key=True)
    passwd  = models.CharField(max_length=20, null=True, default=None)
    tokenValue = models.CharField(max_length=100)
    headImg = models.CharField(max_length=200)
    integral = models.IntegerField(default=0)
    vipLevel = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    lastLoginTime = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table = "users"
    def __str__(self):
        return self.phoneNum
    @classmethod
    def create(cls, phoneNum, passwd, tokenValue, headImg):
        return cls(phoneNum=phoneNum, passwd=passwd, tokenValue=tokenValue, headImg=headImg)


'''
地址表   addresses
name          姓名
sex           性别
phoneNum   手机号
postCode   邮编
address    收货地址
province   省份
city       城市
county     区县
street     街道
detailAddress 详细地址
user          所属用户(外键)
'''
class Address(models.Model):
    name = models.CharField(max_length=20)
    sex = models.BooleanField()
    phoneNum = models.CharField(max_length=20)
    postCode = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    province = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    county = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    detailAddress = models.CharField(max_length=200)
    user = models.ForeignKey("User")
    class Meta():
        db_table = "addresses"
    def __str__(self):
        return self.address
    @classmethod
    def create(cls, name, sex, phoneNum, postCode, address, province, city, county, street, detailAddress, user):
        return cls(name=name, sex=sex, phoneNum=phoneNum, postCode=postCode, address=address, province=province, city=city, county=county, street=street, detailAddress=detailAddress, user=user)

class Cart(models.Model):
    user = models.ForeignKey("User")
    product = models.ForeignKey("Product")
    order = models.ForeignKey("Order")
    num = models.IntegerField()
    isOrder = models.BooleanField(default=True)
    isCheck = models.BooleanField(default=True)
    class Meta():
        db_table = "carts"
    @classmethod
    def create(cls, user, product, order, num):
        return cls(user=user, product=product, order=order, num=num)
class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isDelete=False)
class Order(models.Model):
    orders1 = models.Manager()
    orders2 = OrderManager()
    orderId = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey("User")
    address = models.ForeignKey("Address")
    price = models.FloatField()
    flag = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    lastTime = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table = "orders"
    @classmethod
    def create(cls, orderId, user, address, price):
        return cls(orderId=orderId, user=user, address=address, price=price)
