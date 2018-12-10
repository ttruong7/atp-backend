# Generated by Django 2.1.4 on 2018-12-10 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('key', models.CharField(editable=False, max_length=64, unique=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Blueprint Name')),
                ('cloud_region', models.CharField(blank=True, choices=[('westus2', 'US West 2'), ('southeastasia', 'Asia Southeast'), ('westeurope', 'Europe West')], max_length=100, null=True)),
                ('vm_size', models.CharField(blank=True, max_length=100, null=True, verbose_name='Azure VM Size')),
                ('image_id', models.CharField(blank=True, max_length=300, null=True, verbose_name='Azure Image')),
                ('allow_internet_outbound', models.BooleanField(default=False, verbose_name='Allow Outbound Internet Access')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blueprints', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Course Title')),
                ('short_name', models.CharField(editable=False, max_length=60, verbose_name='Course Short Name')),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Pod Name')),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('number', models.IntegerField(editable=False)),
                ('status', models.CharField(choices=[('undeployed', 'Undeployed'), ('deploying', 'Deploying'), ('started', 'Started'), ('starting', 'Starting'), ('stopped', 'Stopped'), ('stopping', 'Stopping'), ('restarting', 'Restarting'), ('delete', 'DELETE'), ('error', 'ERROR')], default='undeployed', max_length=100)),
                ('public_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='Public IP Address')),
                ('hostname', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hostname')),
                ('next_stop', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('access_token', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pod', to='rest.AccessToken')),
                ('blueprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pod', to='rest.Blueprint')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pods', to='rest.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, error_messages={'invalid': 'Invalid email format!'}, max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='pod',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pods', to='rest.Student'),
        ),
    ]