from django.db import models

# Create your models here.
class CustomerData(models.Model):
	customer_name = models.TextField(max_length=200)
	customer_father_name = models.TextField(max_length=200)
	customer_profile = models.TextField(max_length=200)
	loan_amount_no = models.IntegerField()

class BranchData(models.Model):
	 customer = models.ForeignKey(CustomerData, default = 1, on_delete=models.CASCADE,  null=True, blank=True)
	 zone_name = models.TextField(max_length=200)
	 region_name = models.TextField(max_length=200)
	 area_name = models.TextField(max_length=200)
	 branch_name = models.TextField(max_length=200)
	 branch_code = models.TextField(max_length=200)

class CustomerHomeAddressData(models.Model):
	 customer = models.ForeignKey(CustomerData, default = 1, on_delete=models.CASCADE,  null=True, blank=True)
	 pincode = models.TextField(max_length=200)
	 landmark = models.TextField(max_length=200)
	 address1 = models.TextField(max_length=200)
	 address2 = models.TextField(max_length=200)
	 address3 = models.TextField(max_length=200)

class CustomerOfficeData(models.Model):
	customer = models.ForeignKey(CustomerData, default = 1, on_delete=models.CASCADE,  null=True, blank=True)
	office_pincode = models.TextField(max_length=200)
	office_landmark  = models.TextField(max_length=200)
	office_address1 = models.TextField(max_length=200)
	office_address2 = models.TextField(max_length=200)
	office_address3 =models.TextField(max_length=200)

class LoanAmountData(models.Model):
	customer = models.ForeignKey(CustomerData, default = 1, on_delete=models.CASCADE,  null=True, blank=True)
	aggrement_data = models.DateField()
	lrn = models.TextField(max_length=200)
	tenor = models.TextField(max_length=200)
	adv_emi = models.TextField(max_length=200)
	mob = models.TextField(max_length=200)
