# Generated by Django 3.0.8 on 2020-07-20 20:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20200720_2341'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Postări',
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='Întrebări',
        ),
        migrations.AlterModelOptions(
            name='comentariu',
            options={'ordering': ('created',), 'verbose_name_plural': 'comentariu'},
        ),
        migrations.AlterModelOptions(
            name='postări',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'postări'},
        ),
        migrations.AlterModelOptions(
            name='întrebări',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'întrebări'},
        ),
    ]
