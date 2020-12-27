from django.urls import path
from client import views


from django.conf import settings
from django.conf.urls .static import static
urlpatterns = [
    path('',views.signup,name='welcome'),
    path('signup/',views.signup,name="signup"),
    path('client_signup_success/', views.client_signup_success, name="client_signup_success"),
    path('signin/',views.signin,),
    path('additem/', views.additem, name='additem'),
    path('loggingoff/',views.loggingoff,name="loggingoff"),

    #path('showdata/',views.ShowData.as_view()),
    #path('onedata/<str:unique_id>',views.OneData.as_view()),
    #path('apidata/',views.ApiData.as_view()),
    #path('clientapi/<str:unique_id>',views.ClientApi.as_view()),
    #path('all/',views.allorsingle.as_view()),
    #path('all/<str:id>',views.allorsingle.as_view()),
    #path('purejson/',views.PureJson.as_view())
    #path('clientapidata/<str:unique_id>',views.ClientApiData.as_view()),
    #path('clientapidata/',views.ClientApiData.as_view()),
    #path('singleurl/',views.SingleUrl.as_view())

    #path('list/',views.ListApiAll.as_view()),
    #path('list/',views.ListApiAll.as_view()),
    # path('one/',views.One.as_view())
    path('listapi/', views.ListApi.as_view()),
    path('clientapidata/',views.ClientApiData.as_view()),

    path('listapiall/',views.CreateApiAll.as_view()),
    path('retrieve/<str:unique_id>',views.RetrieveApiView.as_view()),
    path('update/<str:unique_id>',views.UpdateApiView.as_view()),
    path('destroy/<str:unique_id>',views.DestroyApiView.as_view()),
    path('createmixins/',views.ClientListModelMixin.as_view()),
    path('updatemixins/<str:unique_id>',views.ClientRetrieveUpdateDestroyMixins.as_view()),
    path('destroymixins/<str:unique_id>',views.ClientDestroyMixins.as_view()),
    path('joy/',views.Joy.as_view())

    ]
