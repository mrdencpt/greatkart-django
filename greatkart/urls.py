"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

 สร้าง ดักเก็บข้อมูล ip คนเแฮ็กข้าในนาม หน้า admin  /admin
    1. ต้อง pip install django-admin-honeypot ก่อนใส่ admin_honeypotที่ settings.py INSTALLED_APPS 
    2. ตามด้วย python manage.py migrate ด้วย ถึงจะใช้งาน admin_honeypot
    ตาม vdo เกิด Error ให้ pip install django-admin-honeypot-updated-2021 แทน migrate ผ่าน
"""
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    # ORDERS
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

