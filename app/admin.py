from django.contrib import admin

# Register your models here.

from .models import CustomerData, CustomerOfficeData, CustomerHomeAddressData, BranchData, LoanAmountData

mymodels = [CustomerData, CustomerOfficeData, CustomerHomeAddressData, BranchData, LoanAmountData]

admin.site.register(mymodels)

# @admin.register(CustomerData)
# class CustomerDataAdmin(admin.ModelAdmin):
# 	list_display = (customer_name, customer_father_name, customer_profile, loan_amount_no)

# @admin.register(BranchData)
# class BranchDataAdmin(admin.ModelAdmin):
# 	list_display = (customer, zone_name, region_name, area_name, branch_name, branch_data)
#
# @admin.register(CustomerHomeAddressData)
# class CustomerHomeAddressDataAdmin(admin.ModelAdmin):
# 	list_display = (customer, pincode, landmark, address1, address2, address3)
#
# @admin.register(CustomerOfficeData)
# class CustomerOfficeDataAdmin(admin.ModelAdmin):
# 	list_display = (customer, office_pincode, office_landmark, office_address1, office_address2, office_address3)
#
# @admin.register(LoanAmountData)
# class LoanAmountDataAdmin(admin.ModelAdmin):
# 	list_display = (customer, aggrement_data, lrn, tenor, adv_emi, mob)
