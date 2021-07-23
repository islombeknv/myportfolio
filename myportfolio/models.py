from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class PortfolioModel(models.Model):
    image = models.ImageField(upload_to='portfolio', verbose_name=_('image'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    content = models.CharField(max_length=25, verbose_name=_('content'))
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='portfolio',
                                 verbose_name=_('category')
                                 )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolio')
