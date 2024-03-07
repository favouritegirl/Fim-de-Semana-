from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('password', models.CharField(blank=True, max_length=255)),
             ],
            options={
                'db_table': 'consumidor',
                'managed': True,
            },
        ),
        
    ]