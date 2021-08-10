from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()

router.register('CustomerData', views.CustomerDataViewSet, basename='CustomerData')
router.register('BranchData', views.BranchDataViewSet, basename='BranchData')
router.register('CustomerHomeAddressData', views.CustomerHomeAddressDataViewSet, basename='CustomerHomeAddressData')
router.register('CustomerOfficeData', views.CustomerOfficeDataViewSet, basename='CustomerOfficeData')
router.register('LoanAmountData', views.LoanAmountDataViewSet, basename='LoanAmountData')
router.register('CombinedDataViewSet', views.CombinedDataViewSet, basename='CombinedDataViewSet')


urlpatterns = [
    path('apis/', include(router.urls)),
    path('', views.index, name='index')
]
