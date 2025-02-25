from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Products

@receiver(post_save,sender=Products)
def post_acton(sender,instance,**kwargs):
     print(sender)
     print(instance)
     print("signaled")