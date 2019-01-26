from django.urls import path, include
from . import views

from rest_framework import routers # restful api version

app_name = 'rest_api_example'

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]