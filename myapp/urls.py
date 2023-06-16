from django.urls import path
from myapp import views

urlpatterns = [
    path('index/', views.index, name="index"),

    path('category/', views.category, name="category"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),

    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),

    path('', views.adminlogin, name="adminlogin"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),

    path('savecontact/', views.savecontact, name="savecontact"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:dataid>', views.deletecontact, name="deletecontact"),
]
