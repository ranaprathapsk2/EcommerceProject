from django.shortcuts import render,redirect
from myapp.models import CategoryDB,ProductDB
from webapp.models import SigninDB, CartDB, CheckoutDB
from django.contrib import messages
# Create your views here.


def home(req):
    data = CategoryDB.objects.all()
    cartdata = CartDB.objects.filter(UserName=req.session['username'])
    return render(req, "home.html",{'data':data,'cartdata':cartdata})

def contact(req):
    data = CategoryDB.objects.all()
    return render(req, "contact.html",{'data':data})

def about(req):
    data = CategoryDB.objects.all()
    return render(req, "about.html",{'data':data})

def product(req, category_name):
    data = CategoryDB.objects.all()
    pro = ProductDB.objects.filter(ProductCategory=category_name)
    return render(req, "product.html",{'pro':pro,'data':data})

def productdetails(req,dataid):
    data = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    singleproduct = ProductDB.objects.get(id=dataid)
    return render(req, "productdetails.html",{'singleproduct':singleproduct,'pro':pro,'data':data})

def signuppage(req):
    return render(req,"register.html")

def signinpage(req):
    return render(req,"login.html")

def savesignup(req):
    if req.method=="POST":
        na = req.POST.get('username')
        em = req.POST.get('email')
        im = req.FILES['image']
        ps = req.POST.get('password')
        obj = SigninDB(Username=na,Email=em,Image=im, Password=ps)
        obj.save()
        return redirect(signuppage)


def usersigin(req):
    if req.method=="POST":
        un = req.POST.get('username')
        pw = req.POST.get('password')
        if SigninDB.objects.filter(Username=un,Password=pw).exists():
            req.session['username'] = un
            req.session['password'] = pw
            return redirect(home)
        else:
            return redirect(signinpage)
    else:
        return redirect(signinpage)


def userlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(signinpage)

def cart(req):
    cdata = CategoryDB.objects.all()
    data = CartDB.objects.filter(UserName=req.session['username'])
    return render(req,"cart.html",{'data':data,'cdata':cdata})

def savecart(req):
    if req.method=="POST":
        un = req.POST.get('username')
        pn = req.POST.get('productname')
        pd = req.POST.get('productdescription')
        pq = req.POST.get('productquantity')
        pp = req.POST.get('productprice')
        tp = req.POST.get('total')
        # pi = req.FILES['productimage']Image=pi
        obj = CartDB(UserName=un,ProductName=pn,ProductDescription=pd,Quantity=pq,price=pp,Total=tp)
        obj.save()
        return redirect(cart)

def deletecart(req,dataid):
    data = CartDB.objects.filter(id=dataid)
    data.delete()
    return redirect(cart)


def checkout(req):

    return render(req,"checkout.html")


def savecheckout(req):
    if req.method=="POST":
        fname= req.POST.get('fname')
        lname= req.POST.get('lname')
        number= req.POST.get('number')
        email= req.POST.get('email')
        country= req.POST.get('country')
        state= req.POST.get('state')
        postcode= req.POST.get('postcode')
        street= req.POST.get('street')
        apartment= req.POST.get('apartment')
        obj = CheckoutDB(FirstName=fname,LastName=lname,Phone=number,Email=email,Country=country,State=state,Pin=postcode,Street=street,Apartment=apartment)
        obj.save()
        messages.success(req, "YOUR ORDER PLACED SUCCESSFULLY")
        return redirect(checkout)