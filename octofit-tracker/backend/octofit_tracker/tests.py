from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Clark Kent", email="clark@dc.com", team="DC")
        self.assertEqual(user.name, "Clark Kent")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.assertEqual(team.name, "Marvel")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name="Bruce Wayne", email="bruce@dc.com", team="DC")
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2024-01-01")
        self.assertEqual(activity.type, "Running")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Push Ups", description="Upper body", difficulty="Easy")
        self.assertEqual(workout.name, "Push Ups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(name="Tony Stark", email="tony@marvel.com", team="Marvel")
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
