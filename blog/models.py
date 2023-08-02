from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Postări(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',
                            help_text = '* Se completează automat.',)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts',
                              default='1',
                              help_text = '* Va rămâne „1”.',)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',
                              help_text = '* Selectează „Publicat” pentru a posta pe site.',)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager(help_text = '* O listă de cuvinte cheie separate prin virgulă.',)

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = "Postările mele"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Întrebări(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',
                            help_text = '* Pentru a completa câmpul „Slug”, apasă pe câmpul „title”.',)
    author = models.CharField(max_length=250,
                              default="Anonim",
                              help_text = '* Se completează doar dacă este necesar, implicit va fi Anonim.')
    email = models.EmailField(default=None)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',
                              help_text = '* Pentru a publica pe site, selectează „publicat” din listă.')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = "Întrebări primite"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:question_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
        
        
class Comentariu(models.Model):
    
    post = models.ForeignKey(Întrebări,
                             on_delete=models.CASCADE,
                             limit_choices_to={'status':'draft'},
                             related_name='comments',
                             help_text = '* Selectează o întrebare din listă.',
                             )
    name = models.CharField(max_length=80, default='Avocat Petrescu Carmen')
   
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = "Răspunde la întrebări"

    def __str__(self):
        return f'Comentariu de {self.name} pe {self.post}.'
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Pagina de contact"
    
    def __str__(self):
        return self.name + "-" + self.email
