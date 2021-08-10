from rest_framework import serializers
from .models import CustomerData, BranchData, CustomerHomeAddressData, CustomerOfficeData, LoanAmountData

class CustomerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = '__all__'

class BranchDataSerializer(serializers.ModelSerializer):
    customer = CustomerDataSerializer(read_only=True)
    class Meta:
        model = BranchData
        fields = ['customer_id', 'zone_name', 'region_name', 'area_name', 'branch_name', 'branch_code', 'customer']

class CustomerHomeAddressDataSerializer(serializers.ModelSerializer):
    branch = BranchDataSerializer(many=True, read_only=True)

    class Meta:
        model = CustomerHomeAddressData
        fields = ['customer_id', 'pincode', 'landmark', 'address1', 'address2', 'address3', 'customer', 'brach']

class CustomerOfficeDataSerializer(serializers.ModelSerializer):
    customer_home = CustomerHomeAddressDataSerializer(read_only=True)

    class Meta:
        model = CustomerOfficeData
        fields = ['customer_id', 'office_pincode', 'office_landmark', 'office_address1', 'office_address2', 'office_address3', 'customer', 'customer_home']

class LoanAmountDataSerializer(serializers.ModelSerializer):
    customer_office = CustomerOfficeDataSerializer(read_only=True)
    class Meta:
        model = LoanAmountData
        fields = ['aggrement_data', 'lrn', 'tenor', 'adv_emi', 'mob', 'customer', 'customer_office'  ]

class CombinedSerializer(serializers.Serializer):
    customer = CustomerDataSerializer(read_only=True)
    branch = BranchDataSerializer(read_only=True)
    customer_home = CustomerHomeAddressDataSerializer(read_only=True)
    customer_office = CustomerOfficeDataSerializer(read_only=True)
    loan = LoanAmountDataSerializer(read_only=True)
