from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField

# Create your models here.
class Perfil(models.Model):
    id = UUIDField(primary_key=True, verbose_name="Id")
    user = models.OneToOneField(User, unique=True, blank=False, null=False, verbose_name="Usuario", related_name='profile')
    image = models.ImageField(upload_to='profile/', default=None, null=True, blank=True, verbose_name="Foto de Perfil")
    
    class Meta:
    	verbose_name = "Perfil"
    	verbose_name_plural = 'Perfiles'
    
    def __unicode__(self):
        return self.user.username
