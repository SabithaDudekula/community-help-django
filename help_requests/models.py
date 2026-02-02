from django.db import models
from django.contrib.auth.models import User


class HelpRequest(models.Model):

    CATEGORY_CHOICES = [
        ('Medical', 'Medical'),
        ('Education', 'Education'),
        ('Job', 'Job'),
        ('Financial', 'Financial'),
        ('Food', 'Food'),
        ('Housing', 'Housing'),
        ('Transport', 'Transport'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    # Request Owner
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='requests'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    location = models.CharField(max_length=150)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Open'
    )

    # Helper (Who is helping)
    helper = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='helped_requests'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
