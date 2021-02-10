from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet, create_token, create_user

router_v1 = DefaultRouter()
router_v1.register('', UsersViewSet)

authpath = [
    path('email/', create_user, name='create_user'),
    path('token/', create_token, name='create_token'),
]

urlpatterns = [
    path('v1/auth/', include(authpath)),
    path('v1/users/', include(router_v1.urls))

]
