from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/',views.registration_view,name='register'),
    path('shopregister/',views.shop_view,name='shopregister'),
    path('booking/',views.booking_view,name='booking'),
    path('myaccount/',views.myaccount_view,name='myaccount'),
    path('shops/',views.shops_view,name='shops'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
