from django.urls import path

from .views import anasayfa,bizkimiz,neyapıyoruz,portfolyo


urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('biz-kimiz/', bizkimiz, name="bizkimiz"),
    path('ne-yapıyoruz/', neyapıyoruz, name="neyapıyoruz"),
    path('portfolyo/', portfolyo, name="portfolyo"),
    
]