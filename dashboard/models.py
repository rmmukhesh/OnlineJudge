from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        limit_choices_to={'is_superuser': True},
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='testcases')
    input_data = models.TextField(help_text="Standard input for this test case.")
    expected_output = models.TextField(help_text="Expected standard output (trim whitespace when comparing).")
    is_public = models.BooleanField(default=False,
        help_text="Public test cases are visible to users; private ones only run on submission.")

    def __str__(self):
        return f"{self.problem.title} - TC #{self.id}"

class Submission(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
        ('E', 'Error'),
        ('T', 'Timed Out'),
    ]

    LANG_CHOICES = [
        ('CPP', 'C++'),
        ('PY', 'Python'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=3, choices=LANG_CHOICES, default='PY', help_text="Select your language")
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    verdict_details = models.TextField(blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.get_status_display()}"