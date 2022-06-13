# Generated by Django 4.0.5 on 2022-06-13 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customers_create_at_alter_customers_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='type',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='prosmotir',
        ),
        migrations.RemoveField(
            model_name='category',
            name='protsent',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category'),
        ),
    ]