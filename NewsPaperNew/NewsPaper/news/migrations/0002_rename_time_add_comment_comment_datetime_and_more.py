# Generated by Django 4.0.3 on 2022-04-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='time_add_comment',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='time_add_post',
            new_name='create_time',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_rating',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_rating',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_types',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_post',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='header',
            field=models.CharField(default='Заголовок отсутвует', max_length=124),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='Текст отсутствует'),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('PS', 'Статья'), ('NW', 'Новость')], default='PS', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.author'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
