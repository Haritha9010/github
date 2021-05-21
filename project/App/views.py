from django.shortcuts import render,redirect
from django.http import HttpResponse
from App.forms import RegForm,ChpwdForm,WorkerForm,CustomiseForm,CategoryForm,ProductForm,RoleR,RoleUp,UpPrf,Procustom
from django.contrib.auth.decorators import login_required
from App.models import User,Worker,Category,Customise,Product,Cart,Myorders,Rolerest
from django.core.mail import send_mail
from project import settings
from django.contrib import messages
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
import tempfile
from django.template.loader import get_template
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.

def home(request):
	d=Category.objects.all()
	return render(request,'html/home.html',{'data':d})

def register(request):
	d=Category.objects.all()
	if request.method=="POST":
		q=RegForm(request.POST)
		if q.is_valid():
			q.save()
			return redirect('/lg')
	q=RegForm()
	return render(request,'html/register.html',{'u':q,'data':d})

def about(request):
	d=Category.objects.all()
	return render(request,'html/aboutus.html',{'data':d})
# @login_required
# def hc(request):
# 	if request.method=="POST":
# 		j=CraftsForm(request.POST,request.FILES)
# 		if j.is_valid():
# 			i=j.save(commit=False)
# 			i.uid_id=request.user.id
# 			i.save()
# 			return redirect('/hcft')
# 	j=CraftsForm()
# 	k=HandiCrafts.objects.filter(uid_id=request.user.id)
# 	return render(request,'html/handcrafts.html',{'u':j,'y':k})


def profile(request):
	d=Category.objects.all()
	return render(request,'html/profile.html',{'data':d})

def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepwd.html',{'t':c})

def delete(request,st):
	hc=HandiCrafts.objects.get(id=st)
	hc.delete()
	return redirect('/hcft')

def update(request,up):
	t=HandiCrafts.objects.get(id=up)
	if request.method=="POST":
		y=CraftsForm(request.POST,instance=t)
		if y.is_valid():
			y.save()
		return redirect('/hcft')
	y=CraftsForm(instance=t)
	return render(request,'html/updateitem.html',{'f':y})


def showdata(req):
	if req.method=="POST":
		b=WorkerForm(req.POST)
		if b.is_valid():
			b.save()
		return redirect('/sd')
	b=WorkerForm()
	a=Worker.objects.all()
	return render(req,'html/showdata.html',{'wd':a,'info':b})


def women(request,id):
	d=Category.objects.all()
	p=Product.objects.filter(pid_id=id)
	paginator=Paginator(p,4)
	page=request.GET.get('page')
	try:
		p=paginator.page(page)
	except PageNotAnInteger:
		p=paginator.page(1)
	except EmptyPage:
		p=paginator.page(paginator.num_pages)
	return render(request,'html/product.html',{'da':p,'data':d})
def custom(request):
	d=Category.objects.all()
	if request.method=="POST":
		j=CustomiseForm(request.POST,request.FILES)
		f=request.FILES['im']
		if j.is_valid():
			subject='Order Confirmed'
			body="thank you "+request.POST['uname']+" our designer will contact you soon!!!"+'\n'+"Description ::"+request.POST['description']
			receiver=request.POST['email']
			sender=settings.EMAIL_HOST_USER
			t=EmailMessage(subject,body,sender,[receiver])
			t.content_subtype='html'
			t.attach(f.name,f.read())
			t.send()
			j.save()
			messages.success(request,"Successfully sent to your mail ")
			return redirect('/')
	j=CustomiseForm()
	k=Customise.objects.all()
	return render(request,'html/custom.html',{'u':j,'data':d})


def cart(request,id):
	a=Product.objects.get(id=id)
	if request.method=="POST":
		c=Cart(user_id=request.user.id,product_id=a.id)
		c.save()
		return redirect("/crtcnt")
	return render(request,'html/cart.html',{'crt':a})

def cartcount(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/viewcart.html',{'data':d,'sum':sum,'count':count})

def cartdetails(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/cartdetails.html',{'sum':sum,'count':count,'data':d,'cart':c})

def remove(request,id):
	c=Cart.objects.get(id=id)
	c.delete()
	return redirect('/cartdata')

def placeorder(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/placeorder.html',{'sum':sum,'count':count,'data':d,'cart':c})

def pdf(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	template_path="html/pdfpage.html"
	dic={}
	for i in c:
		dic[i.id]=i.product.pname,i.product.price
	var=dic.values()
	dic2={'var':var,'sum':sum}
	response=HttpResponse(content_type="application/pdf")
	response["Content-Disposition"]="attachment;filename='productsreport.pdf'"
	template=get_template(template_path)
	html=template.render(dic2)
	pisa_status=pisa.CreatePDF(html,dest=response)
	if pisa_status.err:
		return HttpResponse("wrong")
	return response

def checkout(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	if request.method=="POST":
		m=request.user.email
		receiver=m
		l=[]
		x=[]
		sum=0
		for i in c:
			sum=sum+i.product.price
			l.append(i.product.pname)
			x.append(i.product.im)
			des=i.product.description
		message='Ordered items ::\n'+' ,'.join(l)+'\n'+ ' will be delivered within 15 days.\n'+'Total amount paid: Rs.'+str(sum)+'\n'+'THANK YOU for Shopping!! \n'+"DESCRIPTION::\n"+str(des)
		subject='Order confirmed'
		sender=settings.EMAIL_HOST_USER
		if c:
			at=EmailMessage(subject,message,sender,[receiver])
			at.content_subtype='html'
			for i in x:
				at.attach(i.name,i.read())
				at.send()
			for i in c:
				sum=sum+i.product.price
				a=Myorders(pname=i.product.pname,price=i.product.price,im=i.product.im,user_id=request.user.id)
				a.save()
				he=Product.objects.filter(id=i.product_id)
				for i in he:
					i.totalquantity-=1
					i.save()
			c.delete()
			return redirect('msg')
		return redirect('msg1')
	return render(request,'html/placeorder.html')

def msg(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/message.html',{'data':d,'count':count})

def msg1(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/message1.html',{'data':d,'count':count})

def myorders(request):
	my=Myorders.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in my:
		count=count+1
		sum=sum+i.price
	return render(request,'html/myorders.html',{'sum':sum,'my':my,'data':d})

def addproduct(request):
	if request.method=="POST":
		j=ProductForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.uid_id=request.user.id
			i.save()
			return redirect('/hcft')
	j=ProductForm()
	k=Product.objects.all()
	return render(request,'html/addproduct.html',{'u':j,'y':k})
def permissions(request):
	ty=User.objects.all()
	return render(request,'html/givpermissions.html',{'q':ty})

@login_required
def rolreq(request):
	if request.method== "POST":
		k =RoleR(request.POST)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			s.save()
			return redirect('/pf')
	k=RoleR()
	return render(request,'html/rolereq.html',{'a':k})
@login_required
def giveper(request,k):
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=RoleUp(request.POST,instance=r)
		if k.is_valid():
			e=k.save(commit=False)
			e.save()
			return redirect('/per')
	k2= RoleUp(instance=r)
	return render(request,'html/approvepermissions.html',{'y':k2})


def updateprofile(request):
	if request.method== "POST":
		p=UpPrf(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/pf')
	p= UpPrf()
	return render(request,'html/updateprofile.html',{'e':p})

def prodcust(request,si):
	d=Category.objects.all()
	x=Product.objects.get(id=si)
	j=Procustom(request.POST,instance=x)
	if request.method=="POST":
		if j.is_valid():
			j.save()
			return redirect('/')
	j=Procustom(instance=x)
	return render(request,'html/procust.html',{'data':d,'prod':j})