from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthorModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('full name'))
    image = models.ImageField(upload_to='auther_images/', verbose_name=_('image'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class BlogTagModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogPostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    main_image = models.ImageField(upload_to="blog_post_img/", verbose_name=_('main image'))
    banner = models.ImageField(upload_to="blog_post_img/", verbose_name=_('banner'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    author = models.ForeignKey(AuthorModel, on_delete=models.RESTRICT, related_name='posts', verbose_name=_('author'))
    tags = models.ManyToManyField(BlogTagModel, related_name='posts', verbose_name=_('tags'))

    def __str__(self):
        return f"{self.title[:100]} ..."

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')