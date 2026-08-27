# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Telefono')
    address = models.CharField(max_length=250, blank=True, verbose_name='Indirizzo')
    postal_code = models.CharField(max_length=10, blank=True, verbose_name='CAP')
    city = models.CharField(max_length=100, blank=True, verbose_name='Città')
    province = models.CharField(max_length=2, blank=True, verbose_name='Provincia')
    country = models.CharField(max_length=100, default='Italia', verbose_name='Paese')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Data di nascita')
    newsletter = models.BooleanField(default=False, verbose_name='Iscritto alla newsletter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Profilo utente'
        verbose_name_plural = 'Profili utente'
    
    def __str__(self):
        return f'Profilo di {self.user.username}'
    
    def get_full_address(self):
        """Restituisce l'indirizzo completo"""
        parts = [self.address, f'{self.postal_code} {self.city}', self.province, self.country]
        return ', '.join(part for part in parts if part)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Crea automaticamente il profilo quando viene creato un utente"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Salva il profilo quando viene salvato l'utente"""
    instance.profile.save()