from django.urls import path
from reglog import views

from django.conf import settings
from django.conf.urls .static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("ap",views.ProductViewset)
router.register("product",views.ViewsetProduct)

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.home,name='home'),
    path('reg/',views.reg,name='reg'),

    path('register/',views.register,name='register'),



    path('itemadd/',views.itemadd,name='itemadd'),

    path('result/',views.result),
    path('result/orderdone/',views.order_done),
    path('orderdone/',views.order_done,name='order_done'),
    path('todays/orderdone/', views.order_done, name='order_done'),
    path('dokan_offer/orderdone/',views.order_done),


    path('signup_success/',views.signupsuccess,name='signupsuccess'),
    path('signin/',views.signin),
    path('signout',views.signout,name='signout'),
    path('signin_success/',views.signinsuccess),
    path("newform/", views.newfrm),
    path("viewset/",include(router.urls)),
    path('obtain_token/',obtain_jwt_token),#username and password{in body postman}
    path('refresh_token/',refresh_jwt_token),#postman :headres content type-application-json,body token-ecikjdjdoosk
    path('verify_token/',verify_jwt_token),
    path('listap/',views.ListProductApi.as_view()),#headers Authorization-JWT kjkdkdbshsshj
    path('gettoken/',obtain_auth_token),
    path('demo/',views.DempApi.as_view()),

    path('todays/',views.today,name='todays'),
    path('todays_deal/',views.todays_deal,name='todays_deal'),


    path('dokan_offer/',views.dokan_offer,name='dokan_offer'),
    path('dkn/',views.dkn,name="dkn"),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
