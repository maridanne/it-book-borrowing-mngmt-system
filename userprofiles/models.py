from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10)
    course = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='uploads/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username