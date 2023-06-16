from django.shortcuts import render, redirect
from myapp.models import CategoryDB, ProductDB, contactDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.views import contact
from django.contrib import messages

# Create your views here.
def index(req):
    return render(req, "index.html")

def category(req):
    return render(req, "category.html")

def savecategory(req):
    if req.method=="POST":
        na = req.POST.get('categoryname')
        de = req.POST.get('categorydescription')
        im = req.FILES['categoryimage']
        obj = CategoryDB(CategoryName=na, CategoryDescription=de, CategoryImage=im)
        obj.save()
        messages.success(req,"SAVEED SUCCESSFULLY")
        return redirect(category)

def displaycategory(req):
    data = CategoryDB.objects.all()
    return render(req, "displaycategory.html",{'data':data})

def editcategory(req,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(req, "editcategory.html",{'data':data})

def updatecategory(req,dataid):
    if req.method=="POST":
        na = req.POST.get('categoryname')
        de = req.POST.get('categorydescription')
        try:
            img = req.FILES['categoryimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).CategoryImage
        CategoryDB.objects.filter(id=dataid).update(CategoryName=na, CategoryDescription=de, CategoryImage=file)
        messages.success(req, "EDITED SUCCESSFULLY")
        return redirect(displaycategory)

def deletecategory(req,dataid):
    data =CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.warning(req, "DELETED")
    return redirect(displaycategory)
##2

def addproduct(req):
    data = CategoryDB.objects.all()
    return render(req,"addproduct.html", {'data':data})

def saveproduct(req):
    if req.method=="POST":
        pc = req.POST.get('productcategory')
        pn = req.POST.get('productname')
        pp = req.POST.get('productprice')
        pd = req.POST.get('productdescription')
        pb = req.POST.get('productbrand')
        pi = req.FILES['productimage']
        obj = ProductDB(ProductCategory=pc, ProductName=pn, ProductPrice=pp, ProductDescription=pd, ProductBrand=pb, ProductImage=pi)
        obj.save()
        return redirect(addproduct)

def displayproduct(req):
    data = ProductDB.objects.all()
    return render(req, "dispalyproduct.html",{'data':data})

def editproduct(req,dataid):
    cdata = CategoryDB.objects.all()
    data = ProductDB.objects.get(id=dataid)
    return render(req,"editproduct.html", {'data':data, 'cdata':cdata})

def updateproduct(req,dataid):
    if req.method=="POST":
        pc = req.POST.get('productcategory')
        pn = req.POST.get('productname')
        pp = req.POST.get('productprice')
        pd = req.POST.get('productdescription')
        pb = req.POST.get('productbrand')
        try:
            pi = req.FILES['productimage']
            fs = FileSystemStorage()
            file = fs.save(pi.name, pi)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=dataid).ProductImage
        ProductDB.objects.filter(id=dataid).update(ProductCategory=pc, ProductName=pn, ProductPrice=pp, ProductDescription=pd, ProductBrand=pb, ProductImage=file)
        return redirect(displayproduct)

def deleteproduct(req,dataid):
    data=ProductDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def adminlogin(req):
    return render(req,"adminlogin.html")

def admin_login(req):
    if req.method == "POST":
        un = req.POST.get('username')
        pw = req.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(req,user)
                req.session['username']=un
                req.session['password']=pw
                messages.success(req, "Login Successfully")
                return redirect(index)
            else:
                messages.error(req, "ERROR")
                return redirect(adminlogin)
        else:
            messages.error(req, "ERROR")
            return redirect(adminlogin)

def logoutpage(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)

def savecontact(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        su = req.POST.get('subject')
        me = req.POST.get('msg')
        obj = contactDB(Name=na,Email=em,Subject=su,Message=me)
        obj.save()
        return redirect(contact)

def displaycontact(req):
    data = contactDB.objects.all()
    return render(req,"displaycontact.html",{'data':data})

def deletecontact(req,dataid):
    data = contactDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)
