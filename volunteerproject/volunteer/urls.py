from django.urls import path
from .views import RegisterView, LoginView, LogoutView, OrganizationView, VolunteerView, OpportunityView, ApplicationView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("get_organizations/", OrganizationView.as_view(), name="get_organization"),
    path("create_organization/", OrganizationView.as_view(), name="create_organization"),
    path("update_organization/<int:pk>/", OrganizationView.as_view(), name="update_organization"),
    path("get_volunteers/", VolunteerView.as_view(), name="get_volunteer"),
    path("create_volunteer/", VolunteerView.as_view(), name="create_volunteer"),
    path("update_volunteer/<int:pk>/", VolunteerView.as_view(), name="update_volunteer"),
    path("get_opportunity/", OpportunityView.as_view(), name="get_opportunity"),
    path("create_opportunity/", OpportunityView.as_view(), name="create_opportunity"),
    path("update_opportunity/<int:pk>/", OpportunityView.as_view(), name="update_opportunity"),
    path("get_applications/", ApplicationView.as_view(), name="get_application"),
    path("create_application/", ApplicationView.as_view(), name="create_application"),
    path("update_application/<int:pk>/", ApplicationView.as_view(), name="update_application")
]