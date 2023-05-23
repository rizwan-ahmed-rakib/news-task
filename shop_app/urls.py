from  django.urls import path
from  . import views
app_name = 'Shop_App'

urlpatterns =[
    path('',views.Home.as_view(),name='home')

]