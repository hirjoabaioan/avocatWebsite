# Generated by Django 3.0.8 on 2020-07-20 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20200720_2353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentariu',
            options={'ordering': ('created',), 'verbose_name_plural': 'răspunde la întrebări'},
        ),
        migrations.AlterModelOptions(
            name='postări',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'postările tale'},
        ),
        migrations.AlterModelOptions(
            name='întrebări',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'întrebări primite'},
        ),
        migrations.AlterField(
            model_name='comentariu',
            name='post',
            field=models.ForeignKey(help_text='* Selectează o întrebare din listă.', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Întrebări'),
        ),
        migrations.AlterField(
            model_name='postări',
            name='author',
            field=models.ForeignKey(default='1', help_text='* Va rămâne „1”.', on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postări',
            name='slug',
            field=models.SlugField(help_text='* Se completează automat.', max_length=250, unique_for_date='publicat'),
        ),
        migrations.AlterField(
            model_name='postări',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publicat', 'Publicat')], default='draft', help_text='* Selectează „Publicat” pentru a posta pe site.', max_length=10),
        ),
        migrations.AlterField(
            model_name='postări',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='* O listă de cuvinte cheie separate prin virgulă.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]