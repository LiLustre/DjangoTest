# Generated by Django 2.2 on 2021-04-21 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('push_image', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=None,
            state_operations=[
                migrations.CreateModel(
                    name='ArticleTag',
                    fields=[
                        ('id',
                         models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('article',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='push_image.Article')),
                        ('tag',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='push_image.Tag'))
                    ],
                    options={
                        'db_table': 'articles_tags',
                    },
                ),
                migrations.AlterField(
                    model_name='article',
                    name='tags',
                    field=models.ManyToManyField(through='push_image.ArticleTag', to='push_image.Tag'),
                ),
            ]
        )
        ,
        migrations.AddField(
            model_name='articletag',
            name='created_at',
            field= models.DateTimeField(auto_now_add=True),
        )
    ]
