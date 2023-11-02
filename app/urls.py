from django.urls import path
from .views import UserListView,UserViewDetails,UserRegisterView

urlpatterns = [
    
    path('view/', UserListView.as_view(), name='view'),
    path('register/', UserRegisterView.as_view(), name='view'),
    path('view/<int:id>', UserViewDetails.as_view(), name='view_list'),
  

    
]