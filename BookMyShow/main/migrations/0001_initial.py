# Generated by Django 4.2.3 on 2024-05-08 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('ACTION', 'ACTION'), ('COMEDY', 'COMEDY'), ('HORROR', 'HORROR'), ('ROMANCE', 'ROMANCE'), ('THRILLER', 'THRILLER'), ('DRAMA', 'DRAMA'), ('ANIMATION', 'ANIMATION'), ('FANTASY', 'FANTASY'), ('SCI_FI', 'SCI_FI'), ('MYSTERY', 'MYSTERY'), ('CRIME', 'CRIME'), ('DOCUMENTARY', 'DOCUMENTARY'), ('FAMILY', 'FAMILY'), ('ADVENTURE', 'ADVENTURE')], max_length=255)),
                ('actor', models.ManyToManyField(to='main.actor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('seat_status', models.CharField(choices=[('BROKEN', 'BROKEN'), ('AVAILABLE', 'AVAILABLE'), ('FILLED', 'FILLED')], max_length=255)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.auditorium')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('show_features', models.CharField(blank=True, choices=[('TWO_D', '2D'), ('THREE_D', '3D'), ('AC_HALL', 'AC_HALL')], max_length=255)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.auditorium')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowSeat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('show_seat_status', models.CharField(choices=[('BOOKED', 'BOOKED'), ('LOCKED', 'LOCKED'), ('AVAILABLE', 'AVAILABLE'), ('UNAVAILABLE', 'UNAVAILABLE')], max_length=255)),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.FloatField()),
                ('ticket_status', models.CharField(choices=[('CANCELLED', 'CANCELLED'), ('PENDING', 'PENDING'), ('PAYMENT_DONE', 'PAYMENT_DONE')], max_length=255)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.show')),
                ('show_seat', models.ManyToManyField(to='main.showseat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowSeatType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('seat_type', models.CharField(choices=[('GOLD', 'GOLD'), ('SILVER', 'SILVER')], max_length=255)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='showseat',
            name='show_seat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.showseattype'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_status', models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('FAILED', 'FAILED'), ('PENDING', 'PENDING')], max_length=255)),
                ('payment_type', models.CharField(choices=[('CASH', 'CASH'), ('CREDIT_CARD', 'CREDIT_CARD'), ('UPI', 'UPI')], max_length=255)),
                ('payment_time', models.DateTimeField()),
                ('reference_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='auditorium',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.theatre'),
        ),
    ]
