from django.urls import path
from client import views


from django.conf import settings
from django.conf.urls .static import static
urlpatterns = [
    path('',views.signup,name='welcome'),
    path('signup/',views.signup,name="signup"),
    path('client_signup_success/', views.client_signup_success, name="client_signup_success"),
    path('signin/',views.signin,),
    path('loggingoff/',views.loggingoff,name="loggingoff"),

    ]
