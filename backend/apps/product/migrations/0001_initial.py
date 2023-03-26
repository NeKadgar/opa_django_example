# Generated by Django 4.1.7 on 2023-03-26 16:44

from django.db import migrations, models
import django.db.models.deletion

def add_default_categories(apps, schema_editor):
    Category = apps.get_model('product', 'Category')
    Category.objects.create(name='Food', description="Some description")
    Category.objects.create(name='Sneakers', description="Some Sneakers description")
    Category.objects.create(name='Jewelry', description="Some Jewelry description")
    Category.objects.create(name='Clothes', description="Some Clothes description")


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.RunPython(add_default_categories),
    ]
