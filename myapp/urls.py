from django.urls import path
from . import views
urlpatterns = [
    path('test1',views.testfunc1,name='test1'),
    path('test2',views.testfunc2,name='test2'),
    path('login',views.testfunc3,name='login')
]