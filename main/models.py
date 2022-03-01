from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.TextField(verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at '))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class PostModel(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    header = models.CharField(max_length=100, verbose_name=_('header'))
    image = models.ImageField(upload_to='post/', verbose_name=_('image'))
    username = models.CharField(max_length=50, verbose_name=_('username'))
    body = models.CharField(max_length=200, verbose_name=_('body'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    status = models.SmallIntegerField(default=STATUS_ACTIVE, choices=(
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive")
    ))

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
