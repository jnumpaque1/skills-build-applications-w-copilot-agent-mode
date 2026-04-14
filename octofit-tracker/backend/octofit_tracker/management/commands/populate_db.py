from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Eliminando datos existentes...'))
            Leaderboard.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Agregando equipos...'))
            marvel = Team.objects.create(name='Marvel', description='Equipo Marvel')
            dc = Team.objects.create(name='DC', description='Equipo DC')

            self.stdout.write(self.style.SUCCESS('Agregando usuarios...'))
            users = [
                User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name),
                User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name),
                User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name),
                User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name),
            ]

            self.stdout.write(self.style.SUCCESS('Agregando actividades...'))
            Activity.objects.create(user=users[0], type='Correr', duration=30, date='2024-04-01')
            Activity.objects.create(user=users[1], type='Nadar', duration=45, date='2024-04-02')
            Activity.objects.create(user=users[2], type='Bicicleta', duration=60, date='2024-04-03')
            Activity.objects.create(user=users[3], type='Yoga', duration=20, date='2024-04-04')

            self.stdout.write(self.style.SUCCESS('Agregando rutinas...'))
            Workout.objects.create(name='Push Ups', description='Flexiones de brazos', difficulty='Fácil')
            Workout.objects.create(name='Pull Ups', description='Dominadas', difficulty='Media')

            self.stdout.write(self.style.SUCCESS('Agregando leaderboard...'))
            Leaderboard.objects.create(user=users[0], score=100, rank=1)
            Leaderboard.objects.create(user=users[1], score=90, rank=2)
            Leaderboard.objects.create(user=users[2], score=80, rank=3)
            Leaderboard.objects.create(user=users[3], score=70, rank=4)

            self.stdout.write(self.style.SUCCESS('¡Base de datos poblada con datos de prueba!'))
