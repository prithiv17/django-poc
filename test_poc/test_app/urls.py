from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import EmpdetailsView, fileUpload, ListUsers, EmpdashboardView,CustomerDetailsView

# from . import views


app_name = "test_app"


router = DefaultRouter()
router.register(r'empdetails',EmpdetailsView, basename='empdetails')
router.register(r'customerdetails',CustomerDetailsView, basename='customerdetails')
# router.register(r'empdashbord',EmpdashboardView, basename='empdashbord')




# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('fileUpload/', fileUpload, name='fileUpload'),
    path('listusers/', ListUsers.as_view(), name='listusers'),    
    path('empdashbord/', EmpdashboardView.as_view(),name='empdashbord'),

]