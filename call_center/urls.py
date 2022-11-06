from django.urls import path
from rest_framework import routers
from call_center import views


route = routers.SimpleRouter()

urlpatterns = route.urls

urlpatterns += path('login',views.login),
urlpatterns += path('insertar',views.insertar),
urlpatterns += path('ordenes',views.ordenes),
urlpatterns += path('recibido',views.recibido),

