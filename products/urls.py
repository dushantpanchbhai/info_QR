from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create',views.create,name='create'),
    path('products/<str:string>/', views.index, name='products'),
    path('',views.main,name='home'),
    path('allInfo/<str:string>/',views.allInfo,name='info'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)