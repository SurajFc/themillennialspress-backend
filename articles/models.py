from django.db import models
from django.urls import reverse
from image_optimizer.fields import OptimizedImageField
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _
from users.models import User
from django.utils.functional import cached_property



class TimeLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Category
class Category(TimeLog):
    name = models.CharField(max_length=50, unique=True)
    image = OptimizedImageField(
        upload_to="category",
        optimized_image_output_size=(240, 320),
        optimized_image_resize_method="thumbnail",
        default="def.png"  # 'thumbnail', 'cover' or None
    )
    slug = models.SlugField(unique=True,default=" ")

    description = models.TextField(default=" ",blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('-updated_at',)



#Articles and others
class Articles(TimeLog):
    title = models.CharField(max_length=255,unique=True)
    subtitle = models.CharField(max_length=255,default=' ',blank=True)
    cover =  OptimizedImageField(
        upload_to="Articles",
        optimized_image_output_size=(400, 320),
        optimized_image_resize_method="cover",
        blank=True  # 'thumbnail', 'cover' or None
    )
    category= models.ForeignKey(Category, verbose_name=_("category_id"), on_delete=models.CASCADE,default=34,related_name='_category')
    tags = ArrayField(models.CharField(max_length=50, blank=True),blank=True)
    content = models.TextField()
    author_name = models.CharField(max_length=40)
    user = models.CharField(max_length=50)
    realease = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,default=" ")

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
      # @staticmethod
    @cached_property
    def get_total_articles(self):
        return Articles.objects.filter(is_active=True).count()


    class Meta:
        db_table = "articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ('-updated_at',)


#Articles Related Images
class ArticleImages(models.Model):
    image = image = OptimizedImageField(
        upload_to="Articles/images/",
        optimized_image_output_size=(400, 320),
        optimized_image_resize_method="cover",
          # 'thumbnail', 'cover' or None
    )
    created_on = models.DateTimeField(auto_now=True)
    added_by = models.CharField(max_length=100)

    class Meta:
        db_table = "articleimage"
        verbose_name = "ArticleImage"
        verbose_name_plural = "ArticleImages"

