from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Profile, Organization, Volunteer, Opportunity, Application
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import jwt, datetime
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,OrganizationSerializer, VolunteerSerializer, OpportunitySerializer, ApplicationSerializer
from django.shortcuts import get_object_or_404

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile(user=user, user_type = request.data.get('user_type'))
            profile.save()
            return Response({'message':"Signup Sucessfull", 'user_details': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message':"Invalid Credentials"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        print(username,password,user)
        if user is None:
            return Response({'message':'User not Regitsered, Please Signup'}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.check_password(password):
            return Response({'message':'wrong password, Please try again'}, status=status.HTTP_400_BAD_REQUEST)
        
        login(request,user)
        payload = {
            'id':user.id,
            'exp': datetime.datetime.now(datetime.UTC)+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.now(datetime.UTC)
        }
        token = jwt.encode(payload,'cap1.4b', algorithm='HS256')
        print(token)
        response = Response()
        response.data = {'message':'login sucessfull','token':token}
        response.satus = status.HTTP_200_OK
        response.set_cookie(
            key='jwt',
            value=token,
            httponly=False,
            samesite=None,
            secure=None
        )
        return response
    
class LogoutView(APIView):
    
    def post(self, request):
        logout(request)
        response=Response()
        response.delete_cookie("jwtoken")
        response.data={"message":"logedout..."}
        return response
    
class OrganizationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        organization_id = kwargs.get('pk')
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):        
        organization_id = kwargs.get('pk')
        organization = get_object_or_404(Organization, id=organization_id)
        serializer = OrganizationSerializer(organization, data=request.data, partial =True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Organization Updated', "updated_organization": serializer.data}, status=status.HTTP_200_OK)
        return Response({'message':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):        
        organization_id = kwargs.get('pk')
        organization = get_object_or_404(Organization, id=organization_id)
        organization.delete()
        return Response({'message':'Organization Deleted'}, status=status.HTTP_200_OK)
    
class VolunteerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        volunteer_id = kwargs.get('pk')
        volunteers = Volunteer.objects.all()
        serializer = VolunteerSerializer(volunteers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):        
        volunteer_id = kwargs.get('pk')
        volunteer = get_object_or_404(Volunteer, id=volunteer_id)
        serializer = VolunteerSerializer(volunteer, data=request.data, partial =True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Volunteer Updated', "updated_volunteer": serializer.data}, status=status.HTTP_200_OK)
        return Response({'message':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):        
        volunteer_id = kwargs.get('pk')
        volunteer = get_object_or_404(Volunteer, id=volunteer_id)
        volunteer.delete()
        return Response({'message':'Volunteer Deleted'}, status=status.HTTP_200_OK)
    
class OpportunityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        opportunity_id = kwargs.get('pk')
        opportunities = Opportunity.objects.all()
        serializer = OpportunitySerializer(opportunities, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OpportunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):        
        opportunity_id = kwargs.get('pk')
        opportunity = get_object_or_404(Opportunity, id=opportunity_id)
        serializer = OpportunitySerializer(opportunity, data=request.data, partial =True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Opportunity Updated', "updated_opportunity": serializer.data}, status=status.HTTP_200_OK)
        return Response({'message':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):        
        opportunity_id = kwargs.get('pk')
        opportunity = get_object_or_404(Opportunity, id=opportunity_id)
        opportunity.delete()
        return Response({'message':'Opportunity Deleted'}, status=status.HTTP_200_OK)
    
class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        application_id = kwargs.get('pk')
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):        
        application_id = kwargs.get('pk')
        application = get_object_or_404(Application, id=application_id)
        serializer = ApplicationSerializer(application, data=request.data, partial =True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Application Updated', "updated_application": serializer.data}, status=status.HTTP_200_OK)
        return Response({'message':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):        
        application_id = kwargs.get('pk')
        application = get_object_or_404(Application, id=application_id)
        application.delete()
        return Response({'message':'Application Deleted'}, status=status.HTTP_200_OK)