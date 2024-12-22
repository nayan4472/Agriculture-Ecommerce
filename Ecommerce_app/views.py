from django.shortcuts import render,HttpResponse,redirect
from Ecommerce_app.forms import *
from Ecommerce_app.models import *
from django.contrib import messages
from django.http import JsonResponse

from django.core.mail import send_mail,EmailMessage
from Agriculture_Ecommerce.settings import DEFAULT_FROM_EMAIL
from django.conf import settings
from wsgiref.util import FileWrapper
import mimetypes
import os

import hashlib,math,random

import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template

def index(request):
    return render(request,"index.html")

def detail(request,id):
    data = addItems.objects.filter(iid=id)
    return render(request,"detail.html",{'data':data})

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def bill(request):
    user = request.session['user']
    email = signup.objects.values_list('email',flat=True).filter(user=user)
    value=email.first()
    print(value)
    online = 'online'
    pay = Payment.objects.filter(user=value,pay_mode=online).last()
    value_id = OnlinePayment.objects.values_list('iid',flat=True).filter(user=value)
    iid = value_id.last()
    data = addItems.objects.filter(iid=iid)
    op  = OnlinePayment.objects.filter(user=value).last()
    # data = OnlinePayment.objects.filter(user=value)
    
    # dd = addItems.objects.filter(user=value)
    # item_id = Payment.objects.filte(user=value)
    # # oid = item_id.first()
    # data = Cart.objects.filter(mid=item_id)
    return render(request,"bill.html",{'pay':pay,'data':data,'op':op})

def html_to_pdf(request):
    # Load your HTML template
    user = request.session['user']
    email = signup.objects.values_list('email',flat=True).filter(user=user)
    value=email.first()
    print(value)
    online = 'online'
    pay = Payment.objects.filter(user=value,pay_mode=online).last()
    value_id = OnlinePayment.objects.values_list('iid',flat=True).filter(user=value)
    iid = value_id.last()
    data = addItems.objects.filter(iid=iid)
    op  = OnlinePayment.objects.filter(user=value).last()
    template = get_template('bill.html')
   
    html = template.render({'pay':pay,'data':data,'op':op})
    # Specify the path to wkhtmltopdf executable manually
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, configuration=config)

    # Create a response with PDF content
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="MyBill.pdf";'
    return response

def my_order(request):
    user = request.session['user']
    email = signup.objects.values_list('email',flat=True).filter(user=user)
    value=email.first()
    online = 'online'
    value_id = OnlinePayment.objects.values_list('iid',flat=True).filter(user=value)
    iid = value_id.last()

    pay = Payment.objects.filter(user=value,pay_mode=online).last()
    data = addItems.objects.filter(iid=iid)
    op  = OnlinePayment.objects.filter(user=value).last()
    return render(request,"my_order.html",{'pay':pay,'data':data,'op':op})

def admin_home(request):
    return render(request,"admin_home.html")

def show_users(request):
    data = signup.objects.all()
    return render(request,"show_users.html",{'data':data})

def show_online(request):
    online = 'online'
    data = Payment.objects.filter(pay_mode=online)
    return render(request,'show_online.html',{'data':data})

def show_cod(request):
    online = 'cod'
    data = Payment.objects.filter(pay_mode=online)
    return render(request,'show_cod.html',{'data':data})

def online_payment_page(request):
    user = request.session['user']
    email = signup.objects.values_list('email',flat=True).filter(user=user)
    value=email.first()
    online = 'online'
    data = Payment.objects.filter(user=value,pay_mode=online).last()
    return render(request,'online_payment.html',{'data':data})
    
def addonlinepayment(request):
    if request.method == 'POST':
        user = request.POST['user']
        phone = request.POST['phone']
        tid = request.POST['tid']
        gtotal = request.POST['total']
        iid = request.POST['iid']
        add = OnlinePayment(user=user,phone=phone,tid=tid,gtotal=gtotal,iid=iid)
        add.save()
        del_cart = Cart.objects.filter(user=user)
        del_cart.delete()
        messages.success(request,"Your Order Recived")
        return render(request,'feedback.html')
    else:
        form = addOnlinePayment()
        return render(request,'online_payment.html',{'form':form})


def contact(request):
    return render(request,'contact.html')

def contact_add(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        add = Contact(email=email,message=message)
        add.save()
        messages.success(request,"Thanks to Contact Us.")
        return render(request,'contact.html')
    else:
        form = addContact()
        return render(request,'contact.html',{'form':form})
    return render(request,'contact.html')

def feedback(request):
    user = request.session['user']
    data = signup.objects.filter(user=user)
    return render(request,'feedback.html',{'data':data})

def profile(request):
    user = request.session['user']
    data = signup.objects.filter(user=user)
    return render(request,'profile.html',{'data':data})

def cart(request):
    if 'user' in request.session:
        user = request.session['user']
        email = signup.objects.filter(user=user)
        data = Cart.objects.filter(user=user)
        return render(request,"cart.html",{'data': data,'email':email})
        # messages.warning(request,"Session on")
        # return render(request,"cart.html")
    else:
        # messages.warning(request,"Your Cart is Empty")
        return render(request,"cart.html")

def add_admin_page(request):
    return render(request,'add_admin.html')

def add_item_page(request):
    return render(request,'add_item_page.html')

def demo(request):
    return render(request,'demo.html')

def seed(request):
    cat = 'Seeds'
    data = addItems.objects.filter(category=cat)
    return render(request,'seed.html',{'data': data})

def fertilizer(request):
    cat = 'Fertilizers'
    data = addItems.objects.filter(category=cat)
    return render(request,'fertilizer.html',{'data': data})

def veg(request):
    cat = 'Vegetable Seeds'
    data = addItems.objects.filter(category=cat)
    return render(request,'veg.html',{'data': data})

def order(request):
    seed = 'Seeds'
    fer = 'Fertilizers'
    veg = 'Vegetable Seeds'
    data1 = addItems.objects.filter(category=seed)[:4]
    data2 = addItems.objects.filter(category=fer)[:4]
    data3 = addItems.objects.filter(category=veg)[:4]
    return render(request,'order.html',{'data1': data1,'data2': data2,'data3': data3})

def showItems(request):
    data = addItems.objects.all()
    return render(request,'showItem.html',{'data': data})


def search(request):
    return render(request,'search.html')
# Create your views here.
# REGISTER & LOGIN
def reg(request):
    if request.method == 'POST':
        user = request.POST['user']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1!=pass2:
            messages.warning(request,"both password not match")
            return redirect('/login')
        else:
            check_user = signup.objects.filter(user=user)
            if check_user:
                messages.warning(request,"User Already Exist....!")
                return redirect('/login')
            check_email = signup.objects.filter(email=email)
            if check_email:
                messages.warning(request,"Email Already Exist....!")
                return redirect('/login')
            reg = signup(user=user,email=email,pass1=pass1,pass2=pass2)
            reg.save()
            # messages.success(request,"You are Register Successfully")
            request.session['user'] = user
            return render(request,'home.html')
    else:
        form = signupForm()
    return render(request,'index.html',{'form':form})

def login(request):
    if request.method == 'POST':
        uname = request.POST['user']
        pwd = request.POST['pass1']
      
        role = 1
        check = signup.objects.filter(user=uname,pass1=pwd)
        roll = signup.objects.filter(user=uname,role=role)
        if check :
            if roll :
                request.session['admin'] = uname
                return render(request,'admin_home.html')
            else :
                request.session['user'] = uname
                # request.session['email'] = uname
                return render(request,'home.html')
        else:
            if uname == 'admin' and pwd == 'admin123':
                request.session['admin'] = uname
                return render(request,'admin_home.html')
            else:
                messages.warning(request,"Username OR Password Wrong")
                return redirect('/login')
    form = LoginForm(request.POST)
    return render(request,'index.html',{'form':form})

def user_logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/')
    return redirect('/') 

def del_session(request):
    try:
        del request.session['user']
        del request.session['admin']
    except:
        return redirect('/')
    return redirect('/') 

def admin_logout(request):
    try:
        del request.session['admin']
    except:
        return redirect('/login')
    return redirect('/login') 


# ADD ADMIN
def add_Admin(request):
    if request.method == 'POST':
        user = request.POST['user']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        role = request.POST['role']
        if pass1!=pass2:
            messages.warning(request,"both password not match")
            return redirect('/add_admin_page')
        else:
            check_user = signup.objects.filter(user=user)
            if check_user:
                messages.warning(request,"Admin Already Exist....!")
                return redirect('/add_admin_page')
            check_email = signup.objects.filter(email=email)
            if check_email:
                messages.warning(request,"Email Already Exist....!")
                return redirect('/add_admin_page')
            reg = signup(user=user,email=email,pass1=pass1,pass2=pass2,role=role)
            reg.save()
            messages.success(request,"Admin Successfully Added....!")
            return redirect('/add_admin_page')
    else:
        form = signupForm()
    return render(request,'add_admin_page.html',{'form':form})

# SHOW ADMINS
def show_admin(request):
    data = signup.objects.filter(role=1)[:10,-1]
    return render(request,'show_admins.html',{'data':data})

#Edit And Delete Admin : 
def edit_admin(request,id):
    data = signup.objects.get(id=id)
    form = signupForm(request.POST,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/show_admin')
    else:
        return render(request,"update_admin.html",{'data':data})        

def delete_admin(request,id):
    data = signup.objects.get(id=id)
    data.delete()
    messages.success(request,"Delete Admin Successfully..!")
    return redirect("/show_admin")


#ADD ITEM
def add_item(request):
    if request.method == 'POST':
        image = request.POST['item_image']
        name = request.POST['item_name']
        price = request.POST['price']
        dis = request.POST['dis']
        category = request.POST['category']

        check_image = addItems.objects.filter(item_image=image)
        if check_image:
            messages.warning(request,"Item Already Exist....!")
            return redirect('/add_item_page')
        else:
            add = addItems(item_image=image,item_name=name,price=price,dis=dis,category=category)
            add.save()   
            messages.success(request,"Item Successfully Added....!")
            return redirect('/add_item_page')
    else:
        form = addItemsForm()
    return render(request,'add_item_page.html', {'form': form })


#SHOW ITEM
def showItems(request):
    data = addItems.objects.all()
    return render(request,'showItem.html',{'data': data})

# EDIT AND DELETE ITEMS
def edit(request,iid):
    data = addItems.objects.get(iid=iid)
    return render(request,"update_item.html",{'data':data})

def update(request,iid):
    data = addItems.objects.get(iid=iid)
    form = addItemsForm(request.POST,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/showItems')
    else:
        messages.warning(request,"Ooups..! Data not updated")
    
    return render(request,"update_item.html",{'data':data})        


def delete(request,iid):
    data = addItems.objects.get(iid=iid)
    data.delete()
    return redirect("/showItems")

def add_to_cart(request):
    if request.method == 'POST':
        iid = request.POST['iid']
        img = request.POST['img']
        name = request.POST['name']
        price = request.POST['price']
        if 'user' in request.session:
            user = request.session['user']
            user_check = Cart.objects.filter(user=user)
            if user_check:
                iid_check = Cart.objects.filter(iid=iid,user=user)
                if iid_check:
                    messages.warning(request,"Item Already Exist in Cart")
                    return redirect('/order')
                else:
                    add = Cart(iid=iid,user=user,img=img,name=name,price=price)
                    add.save()   
                    messages.success(request,"Item Successfully Added....!")
                    return redirect('/order')
            else:
                add = Cart(iid=iid,user=user,img=img,name=name,price=price)
                add.save()   
                messages.success(request,"Item Successfully Added....!")
                return redirect('/order')
        else:
            messages.warning(request,"You don't have Login so cant add Item in cart")
            return redirect('/order')
    else:
        form = addCartForm()
    return render(request,'order.html', {'form': form })

def delete_cart(request,cid):
    data = Cart.objects.get(cid=cid)
    data.delete()
    messages.success(request,"Delete Item Successfully..!")
    return redirect("/cart")

def productlistAjax(request):
    items = addItems.objects.filter(item_name=0).values_list('item_name',flat=True)
    itemList = list(items)
    return JsonResponse(itemList, safe=False)


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        data = addItems.objects.filter(item_name=search)
        if data:
            return render(request,'search.html',{'data':data})
        else:
            data = addItems.objects.filter(category=search)
            return render(request,'search.html',{'data':data})
    else:
        return render(request,'order.html', {'form': form })

def buy(request):
    if 'user' in request.session:
        if request.method == 'POST':
            user = request.POST['user']
            phone = request.POST['phone']
            address = request.POST['address']
            pay_mode = request.POST['pay_mode']
            iid = request.POST['iid']
            print(iid)
            htotal = request.POST['htotal']
            if pay_mode == 'online':
                add = Payment(iid=iid,user=user,phone=phone,address=address,pay_mode=pay_mode,total=htotal)
                add.save()
                # return redirect('/send_mail_for_Payment_Attendance')
                # data = Payment.objects.filter(user=user)
                return redirect('/online_payment_page')
            else:
                add = Payment(iid=iid,user=user,phone=phone,address=address,pay_mode=pay_mode,total=htotal)
                add.save()
                del_cart = Cart.objects.filter(user=user)
                del_cart.delete()
                messages.success(request,"We are recive your order thanks to check website")
                return render(request,'feedback.html')
        else:
            return render(request,'cart.html')
    else:
        messages.warning(request,"You have't login")
        return render(request,'cart.html')

#SEND EMAIL FOR ONLINE PAYMENT
def send_mail_for_confirmation(request):
    user = request.POST['email']
    recepient = user
    subject = 'Order Confirmation Mail'
    message = 'You payment Received and your Order Placed.'
    send_mail(
        subject,
        message,
       DEFAULT_FROM_EMAIL, [recepient], fail_silently = False)

    messages.success(request,"Email Sent")
    return redirect('/show_online')

def send_mail_for_Payment_Attendance(request):
    user = request.session['user']
    email = signup.objects.values_list('email',flat=True).filter(user=user)
    value=email.first()
    print(value)
    recepient = email
    subject = 'Payment'
    message = 'You Selected Online Payment Method so we sent attachment you to QR code for Paying.'
    mail = EmailMessage(subject=subject,body=message,from_email=DEFAULT_FROM_EMAIL,to=recepient)
    file_path = f"{settings.BASE_DIR}\static\image\payment.png"
    mail.attach_file(file_path)
    mail.send()
    return render(request,'home.html')


def no_login(request,id):
    messages.warning(request,"You don't have Login so cant add Item in cart")
    data = addItems.objects.filter(iid=id)
    return render(request,"detail.html",{'data':data})

def edit_profile(request):
    user = request.session['user']
    data = signup.objects.filter(user=user)
    return render(request,'update_profile.html',{'data':data})

def save_profile(request,id):
    data = signup.objects.get(id=id)
    form = signupForm(request.POST,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/profile')
    else:
        return render(request,"update_profile.html",{'data':data})  



def forgotpassword(request):
    return render(request, 'forgot.html', {})

def forgotpassword_code(request):
    try:
        ins = signup.objects.get(email=request.POST['email'])
    except signup.DoesNotExist:
        ins = None
    if ins :        
        form = signupForm(request.POST)
        if request.method == "POST":
            email = request.POST['email']
            digits = '0123456789'
            OTP = ''
            for i in range(6) :
                OTP += digits[math.floor(random.random() * 10)] 
       
            subject = 'Ecommerce Agriculture Management System'
            message = 'Your  OTP is %s. Never Share OTP with Anyone. Thanks EAMS' %OTP   
            recepient = email
            send_mail(subject, message, DEFAULT_FROM_EMAIL, [recepient], fail_silently = False)
            request.session['email']=email
            request.session['OTP']= OTP
            return render(request, 'OTP.html', {})
    else:
        messages.warning(request, 'Opps! Your Email is not registered...',fail_silently=True) 
        return render(request, 'forgot.html', {})

def otp_confirm_code(request):
    if request.POST['OTP']==request.session['OTP']:
            return render(request, 'set_password.html', {})
    else:
        messages.warning(request, 'Opps! Wrong OTP Try Again...',fail_silently=True) 
        return render(request, 'OTP.html', {})

def new_password_code(request):
    form = signupForm(request.POST)
    if request.method == "POST":
        email = request.session['email']# get session
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            # hash_obj = hashlib.md5(pass1.encode()) 
            # pass1=hash_obj.hexdigest()
            ins = signup.objects.get(email=email)
            ins.pass1 = pass1 
            ins.pass2 = pass2 
            ins.save()
            messages.success(request, 'Password Updated Successfully...',fail_silently=True)
            return render(request, 'index.html',{})
        else:  
            messages.warning(request, 'Password And Confirm Password must be same...',fail_silently=True)
            return render(request, 'set_password.html',{})
    messages.warning(request, 'Opps! There is some Problem...',fail_silently=True)         
    return render(request, 'set_password.html', {})


def otp_confirm(request):
    return render(request,'OTP.html')