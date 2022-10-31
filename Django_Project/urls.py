"""Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'branches', views.BranchView,'Branch')
router.register(r'employees', views.EmployeeView, 'Employee')
router.register(r'customers', views.CustomerView, 'Customer')
router.register(r'car types', views.CarTypeView,'CarType')
router.register(r'cars', views.CarView, 'Car')
router.register(r'rentals', views.RentalView, 'Rental')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorial.urls')),
    path('api/', include(router.urls)),
]
