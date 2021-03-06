from django.urls import path, re_path
from . import views

app_name = 'product_api'

urlpatterns = [
	path('server/', views.ServerAvailableView.as_view(), name="server_available"),

	path('players/create/', views.RegisterUserView.as_view(), name="user_register"),
	path('players/login/', views.LoginUserView.as_view(), name="user_login"),
	path('players/logout/', views.LogoutUserView.as_view(), name="user_logout"),

]


"""
path('users/new/', views.CreateUserView.as_view(), name='user_create'),
	path('users/enroll/', views.CreateEmployeeView.as_view(), name='employee_create'),

	path('products/', views.ProductListView.as_view(), name='product_list'),
	path('products/<pk>/', views.ProductDetailsView.as_view(), name='product_details'),

	path('orders/', views.OrderListView.as_view(), name='order_list'),
	path('orders/new/', views.OrderEnrollView.as_view(), name="order_enroll"),
	path('orders/confirm/', views.OrderConfirmView.as_view(), name="order_confirm"),
	path('orders/payment/', views.OrderPaymentView.as_view(), name="order_confirm"),

	path('orders/<pk>/', views.OrderDetailsView.as_view(), name='order_details'),
	path('orders/<from_date>/<to_date>/', views.OrderFilterView.as_view(), name='filter_date'),
	
"""