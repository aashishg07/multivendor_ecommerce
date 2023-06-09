from .models import User
from django.db import models
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

User =  get_user_model()


class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "Customer_User", null=True)


	def __str__(self):
		return f'{self.user}'


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        if instance.is_customer == True:
        	Customer.objects.create(user = instance)


class Vendor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "Vendor_User", null=True)

	def __str__(self):
		return f'{self.user}'


@receiver(post_save, sender=User)
def create_vendor(sender, instance, created, **kwargs):
    if created:
    	if instance.is_vendor == True:
        	Vendor.objects.create(user = instance)




