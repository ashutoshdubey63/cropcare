from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db import connection
from datetime import datetime
from django.db.models import Q

#create your views here.

def index(request):

    search=request.POST.get("search")

    data=tblcategory.objects.all().order_by("-id")[0:50]

    if search:

        pdata=tblproduct.objects.all().filter(

        Q(title__icontains=search) |

        Q(weight__icontains=search) |

        Q(discounted_price__icontains=search)

        )

    else:

        pdata=tblproduct.objects.all().order_by("-id")[0:24]

    d={

        "cat":data,

        "products":pdata

    }

    return render(request,"index.html",d)

def about(request):
    return render(request,"about.html")

def team(request):
    return render(request,"team.html")

def gallery(request):
    data=tblgallery.objects.all()
    d={"galla":data}
    return render(request,"gallery.html",d)

def category(request):
    return render(request,"category.html")

def services(request):
    return render(request,"services.html")

def product(request):
    search=request.POST.get("search")
    cid=request.GET.get("x")
    cdata=tblcategory.objects.all().order_by("-id")
    pdata=""
    if cid:
     pdata=tblproduct.objects.all().filter(product_category=cid)
    elif search:
       pdata=tblproduct.objects.all().filter(Q(title__icontains=search)|Q(weight__icontains=search)|Q(discounted_price__icontains=search))
    else:
     pdata=tblproduct.objects.all().order_by("-id")
     
    d={"categories":cdata,"products":pdata}
    return render(request,"product.html",d)

from django.shortcuts import render
from django.http import HttpResponse
from .models import tblregister, tblcart

def login(request):

    if request.method == "POST":

        email = request.POST.get("email").strip().lower()
        password = request.POST.get("passwd").strip()

        user = tblregister.objects.filter(
            email=email,
            password=password
        ).first()

        if user:

            request.session["name"] = user.name
            request.session["email"] = user.email

            if user.picture:
                request.session["userpic"] = str(user.picture)

            request.session["cartitems"] = tblcart.objects.filter(
                userid=user.email
            ).count()

            return HttpResponse("""
            <script>
            alert('Login Successful');
            location.href='/product/';
            </script>
            """)

        else:

            return HttpResponse("""
            <script>
            alert('Invalid Email or Password');
            location.href='/login/';
            </script>
            """)

    return render(request, "login.html")

def profile(request):
    email=request.session.get("email")
    if request.method=="POST":
        Name=request.POST.get("uname")
        Address=request.POST.get("uaddress")
        Mobile=request.POST.get("umob")
        Pincode=request.POST.get("upin")
        Landmark=request.POST.get("umark")
        Filename=request.FILES["upic"]
        Password=request.POST.get("upassword")
        user=tblregister.objects.get(email=email)
        user.name=Name
        user.mobile=Mobile
        user.password=Password
        user.pincode=Pincode
        user.landmark=Landmark
        user.address=Address
        user.picture=Filename
        user.save()
        
        request.session["name"]
        return HttpResponse("<script>alert('your profile update successfully');location.href='/profile/'</script>")
    data=tblregister.objects.all().filter(email=email)
    d={"data":data}
    return render(request,"profile.html",d)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tblregister
from datetime import datetime

def register(request):

    if request.method == "POST":

        name = request.POST.get("uname").strip()
        email = request.POST.get("uemail").strip().lower()
        password = request.POST.get("upass").strip()

        mobile = request.POST.get("umob")
        address = request.POST.get("uaddress")
        pincode = request.POST.get("upin")
        landmark = request.POST.get("umark")

        picture = request.FILES.get("upic")

        # Check existing email
        if tblregister.objects.filter(email=email).exists():

            return HttpResponse("""
            <script>
            alert('Email already registered');
            location.href='/register/';
            </script>
            """)

        tblregister.objects.create(
            name=name,
            email=email,
            password=password,
            mobile=mobile,
            address=address,
            pincode=pincode,
            landmark=landmark,
            picture=picture,
            regdate=datetime.now().date()
        )

        return HttpResponse("""
        <script>
        alert('Registration Successful');
        location.href='/login/';
        </script>
        """)

    return render(request, "registration.html")


def services(request):
    return render(request,"services.html")

def cart(request):
    cartid=request.GET.get("cid")
    userid=request.session.get("email")
    d={}
    if userid:
     if cartid:
        tblcart.objects.all().filter(userid=userid,id=cartid).delete()
        a=tblcart.objects.all().filter(userid=userid).count()
        request.session["cartitems"]=a
        return HttpResponse("<script>alert('your item is delete from cart..');location.href='/cart/'</script>")
     cdata=tblcart.objects.all().filter(userid=userid).order_by("-id")
     d={"cartdata":cdata}
     if request.method=="POST":
        qt=int(request.POST.get("qt"))
        pname=request.POST.get("pname")
        pid=request.POST.get("pid")
        pinfo=request.POST.get("pinfo")
        pprice=request.POST.get("pprice")
        dprice=float(request.POST.get("dprice"))
        pweight=request.POST.get("pweight")
        ppicture=request.POST.get("ppicture")
        totalprice=qt*dprice
        if qt==0:
            return HttpResponse("<script>alert('please Increase your items..');location.href='/product/'</script>")
        else:
            tblcart(userid=userid,pid=pid,product_name=pname,product_picture=ppicture,product_info=pinfo,product_price=pprice,discounted_price=dprice,total_price=totalprice,product_weight=pweight,product_quantity=qt,added_date=datetime.now().date()).save()
            cartItems=tblcart.objects.all().filter(userid=userid).count()
            request.session["cartitems"]=cartItems
            return HttpResponse("<script>alert('your item is added in cart');location.href='/product/'</script>")
    return render(request,"cart.html",d)

def orders(request):
    userid=request.session.get("email")
    if userid:
       cursor=connection.cursor()
       cursor.execute("insert into user_tblorder(userid,pid,product_name,product_picture,product_info,product_price,discounted_price,total_price,product_weight,product_quantity,added_date,status) select '"+str(userid)+"',pid,product_name,product_picture,product_info,product_price,discounted_price,total_price,product_weight,product_quantity,'"+str(datetime.now().date())+"','Pending' from user_tblcart where userid='"+str(userid)+"' ")
       tblcart.objects.all().filter(userid=userid).delete()
       a=tblcart.objects.all().filter(userid=userid).count()
       request.session["cartitems"]=a
       return HttpResponse("<script>alert('Your Order Has Been Placed Sucessfully..');location.href='/myorder/'</script>")
    return render(request,"order.html")

def details(request):
    return render(request,"details.html")


def contact(request):
    if request.method=="POST":
     Name=request.POST.get("name")
     Mobile=request.POST.get("mob")
     Email=request.POST.get("email")
     Message=request.POST.get("msg")
     #d={"a":Name,"b":Mobile,"c":Email,"d":Message}
     tblcontact(name=Name,email=Email,mobile=Mobile,message=Message).save()
     return HttpResponse("<script>alert('Data save successfully');location.href='/index/'</script>")
    
    return render(request,"contact.html")

def dashboard(request):
    return render(request,"dashboard.html")


def logout(request):
    user=request.session.get("email")
    if user:
        del request.session["email"]
        del request.session["name"]
        del request.session["userpic"]
        del request.session["cartitems"]
        

        return redirect("/login/")
    return render(request,"logout.html")


def myorders(request):
   userid=request.session.get("email")
   oid=request.GET.get("oid")
   if userid:
      pdata=tblorder.objects.all().filter(userid=userid,status="Pending").order_by("-id")
      sdata=tblorder.objects.all().filter(userid=userid,status="success").order_by("-id")
      ddata=tblorder.objects.all().filter(userid=userid,status="Delivered").order_by("-id")
      if oid:
         tblorder.objects.all().filter(userid=userid,id=oid).delete()
         return HttpResponse("<script>alert('youur order is canceled..')</script>")
      d={"pending":pdata,"success":sdata,"delivered":ddata}
   return render(request,"myorders.html", d)
