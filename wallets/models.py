from django.db import models
from django_bitcoin import Wallet

# Create your models here.

class InstaWallet(models.Model):
    """A wallet model"""

    uuid = models.CharField(blank=True, max_length=50)
    wallet = models.ForeignKey(Wallet, null=True)

    def __unicode__(self):
        return u"Wallet "+self.uuid+" "+self.name

    def url(self):
        return "/wallet/"+self.uuid

