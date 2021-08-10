from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CombinedSerializer, CustomerDataSerializer, BranchDataSerializer, CustomerHomeAddressDataSerializer, CustomerOfficeDataSerializer, LoanAmountDataSerializer
from .models import CustomerData, CustomerHomeAddressData, BranchData, CustomerOfficeData, LoanAmountData

# Create your views here.

def index(request):
    return render(request, 'index.html')

class CustomerDataViewSet(viewsets.ModelViewSet):
    queryset  = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer

class BranchDataViewSet(viewsets.ModelViewSet):
    queryset = BranchData.objects.all()
    serializer_class = BranchDataSerializer

class CustomerHomeAddressDataViewSet(viewsets.ModelViewSet):
    queryset = CustomerHomeAddressData.objects.all()
    serializer_class = CustomerHomeAddressDataSerializer

class CustomerOfficeDataViewSet(viewsets.ModelViewSet):
    queryset = CustomerOfficeData.objects.all()
    serializer_class = CustomerOfficeDataSerializer

class LoanAmountDataViewSet(viewsets.ModelViewSet):
    queryset = LoanAmountData.objects.all()
    serializer_class = LoanAmountDataSerializer

class CombinedDataViewSet(viewsets.ViewSet):
    serializer_class = CombinedSerializer
