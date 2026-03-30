from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
completed = models.BooleanField(default=False)

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    target_company = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class Topic(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
       ('pending', 'Pending'),
       ('in_progress', 'In Progress'),
       ('completed', 'Completed'),
    )

    DIFFICULTY = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    problem_link = models.URLField(blank=True)

class Company(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    role = models.CharField(max_length=200)
    interview_date = models.DateField(null=True, blank=True)
    preparation_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MockInterview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interviewer_name = models.CharField(max_length=100)
    date = models.DateField()
    feedback = models.TextField(blank=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)