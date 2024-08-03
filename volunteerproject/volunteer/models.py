from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_ROLES = (
        ('reader','Reader'),
        ('author','Author')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_ROLES)
    
    def __str__(self):
        return f'{self.user}-{self.user_type}'

class Organization(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    bio=models.TextField()
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Opportunity(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    location=models.CharField(max_length=200)
    date=models.DateField()
    volunteers_needed=models.IntegerField()
    organization=models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Application(models.Model):
    volunteer=models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=(("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")))
    opportunity=models.ForeignKey(Opportunity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer.user.username}-{self.opportunity.title}"