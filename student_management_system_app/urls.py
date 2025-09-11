from django.urls import path
from student_management_system_app import views

urlpatterns = [
    path('', views.home,name="home"),
    path('registration/', views.registration,name="registration"),
    path('data/', views.data,name="data"),
    path('login/', views.log_in,name="login"),
    path('signup/', views.signup,name="signup"),
    path('logout/', views.log_out,name="logout"),
    path('remove/<int:id>/',views.remove,name="remove"),
    path('update/<int:id>/',views.update,name="update"),
]