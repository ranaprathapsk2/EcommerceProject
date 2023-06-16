from django.urls import path
from webapp import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('product/<category_name>', views.product, name="product"),
    path('productdetails/<int:dataid>/', views.productdetails, name="productdetails"),
    path('cart', views.cart, name="cart"),

    path('register/', views.signuppage, name="signuppage"),
    path('', views.signinpage, name="signinpage"),
    path('savesignup/', views.savesignup, name="savesignup"),
    path('usersigin/', views.usersigin, name="usersigin"),
    path('userlogout/', views.userlogout, name="userlogout"),

    path('savecart/', views.savecart, name="savecart"),
    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart"),
    path('checkout/', views.checkout, name="checkout"),
    path('savecheckout/', views.savecheckout, name="savecheckout"),


]
