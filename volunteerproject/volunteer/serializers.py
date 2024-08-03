from rest_framework import serializers
from .models import Organization, Opportunity, Volunteer, Application
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {'password':{'write_only': True}}
        
    def create(self,validated_data):
            instance = self.Meta.model(**validated_data)
            password = validated_data.pop('password',None)
            if password is not None:
                instance.set_password(password)
                instance.save()
                return instance         
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields="__all__"

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteer
        fields="__all__"

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Opportunity
        fields="__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields="__all__"