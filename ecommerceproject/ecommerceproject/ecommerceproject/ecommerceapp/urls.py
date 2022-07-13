from django.urls import path
from .import views
app_name='ecommerceapp'

urlpatterns = [

    path('',views.allproductcategory,name="allproductcategory"),
    path('<slug:c_slug>/',views.allproductcategory,name="allproductcategory_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetails,name="pro_Details")
]
