from django.contrib import admin
from .models import Profile, Organization, Opportunity, Volunteer, Application

admin.site.register(Profile)
admin.site.register(Organization)
admin.site.register(Opportunity)
admin.site.register(Volunteer)
admin.site.register(Application)