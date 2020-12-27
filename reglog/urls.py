from django.urls import path
from reglog import views

from django.conf import settings
from django.conf.urls .static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('itemadd/',views.itemadd,name='itemadd'),
    path('result/',views.result),
    path('orderdone/',views.order_done),

    path('signup_success/',views.signupsuccess,name='signupsuccess'),
    path('signin/',views.signin),
    path('signout',views.signout,name='signout'),
    path('signin_success/',views.signinsuccess),
    path("newform/", views.newfrm),
    path('additem/',views.additem,name='additem'),


   # path("login/",views.login),
   # path("name/",views.name),


   # path("ssn_set/",views.ssn_set),
   # path("ssn_worked/", views.ssn_worked),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
