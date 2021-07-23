from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class OurClientsModel(models.Model):
    image = models.ImageField(upload_to='client', verbose_name=_('image'))
    name = models.CharField(max_length=50, verbose_name=_('name'))
    position = models.CharField(max_length=300, verbose_name=_('position'))
    info = models.TextField(verbose_name=_('info'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('OurClients')
        verbose_name_plural = _('OurClients')


class OurPartnersmodel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='partner', verbose_name=_('partner'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Ourpartners')
        verbose_name_plural = _('OurPartners')


class TagBlogModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'), null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class CategoryBlogModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'), null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BlogModel(models.Model):
    category = models.ForeignKey(CategoryBlogModel,
                                 on_delete=models.PROTECT,
                                 related_name='category',
                                 verbose_name=_('category')
                                 )
    tags = models.ManyToManyField(TagBlogModel, related_name='blogs')

    image = models.ImageField(upload_to='blog', verbose_name=_('image'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.order_by('-created_on')

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class CommentModel(models.Model):
    post = models.ForeignKey(
        BlogModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('comments')
    )

    name = models.CharField(max_length=80, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('created_on'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('commets')
