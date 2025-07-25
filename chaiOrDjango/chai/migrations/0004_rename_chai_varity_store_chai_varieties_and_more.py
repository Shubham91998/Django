# Generated by Django 5.2.4 on 2025-07-17 15:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaireview_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='chai_varity',
            new_name='chai_varieties',
        ),
        migrations.CreateModel(
            name='ChaiCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('chai', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='chai.chaivarity')),
            ],
        ),
    ]
