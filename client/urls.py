from django.urls import path
from client import views


from django.conf import settings
from django.conf.urls .static import static
urlpatterns = [
    path('',views.signup,name='welcome'),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('loggingoff/',views.loggingoff,name="loggingoff"),
    ]
