from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField
from django.utils.translation import gettext as _


# Create your models here.
class UserProfile(models.Model):
    id = UUIDField(primary_key=True, verbose_name=_("Id"))
    user = models.OneToOneField(User, unique=True, blank=False, null=False, verbose_name=_("Usuario"), related_name='profile')
    image = models.ImageField(upload_to='profile/', default="profile/opennut-default-img.png", null=True, blank=True, verbose_name=_("Actualzar Avatar"))
    
    class Meta:
    	verbose_name = _("Perfil")
    	verbose_name_plural = _('Perfiles')
    
    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
