from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date

class User(AbstractUser):
	phno=models.CharField(null='True',max_length=30)
	address=models.TextField(null='True')
	city=models.CharField(max_length=30,null='True')
	state=models.CharField(max_length=40,null='True')
	pin=models.IntegerField(null='True')
	nameoncard=models.CharField(max_length=30,null='True')
	creditcardnumber=models.IntegerField(null='True')
	Expyear=models.DateField(null='True')
	expmonth=models.CharField(max_length=20,null='True')
	cvv=models.IntegerField(null='True')
	t = (
		(1,'Customer'),
		(2,'Shopkeeper'),
		(3,'Anonymous'),
		)
	role = models.IntegerField(default=1,choices=t)

class Worker(models.Model):
	a=[('Artisan',"Artisan"),('Weaver',"Weaver")]
	profession=models.CharField(max_length=10,choices=a)
	name=models.CharField(max_length=20)
	phno=models.IntegerField()
	b=[('male',"Male"),('female',"Female")]
	gender=models.CharField(max_length=20,choices=b)
	Email=models.EmailField(max_length=100)

class Category(models.Model):
	cname=models.CharField(max_length=20)
	def __str__(self):
		return self.cname

class Product(models.Model):
	pname=models.CharField(max_length=300)
	price=models.IntegerField()
	im=models.ImageField()
	totalquantity=models.IntegerField(default=10)
	description=models.TextField(null=True)
	pid=models.ForeignKey(Category,on_delete=models.CASCADE)
	is_status=models.IntegerField(default=1)
	def __str__(self):
		return self.pname

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=1,null=True)
	amount=models.IntegerField(default=0,null=True)


class Customise(models.Model):
	uname=models.CharField(max_length=10)
	email=models.EmailField()
	phno=models.CharField(max_length=20,null='True')
	a=[('sarees',"sarees"),('decor',"decor"),('toys',"toy"),('shirts',"shirts")]
	category=models.CharField(max_length=20,choices=a)
	im=models.ImageField()
	description=models.TextField(max_length=500)

class Myorders(models.Model):
	pname=models.CharField(max_length=300)
	price=models.IntegerField()
	a=[("product quality issues","product quality issues"),("I want to change address/phone number","I want to change address/phone number"),("I have purchased product somewhere else","I have purchased product somewhere else"),("others","others")]
	cancel=models.CharField(max_length=200,choices=a,null=True)
	im=models.ImageField()
	is_status=models.IntegerField(default=0)
	date=models.DateTimeField(auto_now_add='True',null='True')
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	prod=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

class Rolerest(models.Model):
	t=[(1,'customer'),(2,'anonymous')]
	uname=models.CharField(max_length=30)
	roletype=models.IntegerField(choices=t)
	is_checked=models.BooleanField(default=0)
	uid=models.OneToOneField(User,on_delete=models.CASCADE)