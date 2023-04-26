from django.urls import path
from rest_framework import routers

# from .otp_views import (SendPhoneOTP, 
# 						ValidateOTP, 
# 						Register,
# 						PasswordForgot,
# 						ValidatePassForgotOTP,
# 						ForgotChangePassword,)

# from knox import views as knox_views
from . import views
from .views import VendorListView, VendorDetailView, ProductListView, ProductDetailView, CustomerListView, CustomerDetailView, OrderListView, OrderDetailView, CustomerAddressViewSet, ProductRatingViewSet, CategoryDetailView, CategoryListView


# app_name = 'account'
# router = routers.DefaultRouter()
# router.register(r'user', views.UserView, basename='user')

router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewSet)
router.register('productrating', views.ProductRatingViewSet)

urlpatterns = [
    path('vendor/', VendorListView.as_view(), name="list_vendor"),
    path('vendor-detail/<int:pk>/', VendorDetailView.as_view(), name="detail_vendor"),
    
    path('products/', ProductListView.as_view(), name="Product_list"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="Product_detail"),
    
    path('categories/', CategoryListView.as_view(), name="category_list"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category_detail"),
    
    path('customers/', CustomerListView.as_view(), name="list_of_customers"),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name="customer_detail"),
    
    path('orders/', OrderListView.as_view(), name="order_list"),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order_detail")
    
]

urlpatterns += router.urls
	