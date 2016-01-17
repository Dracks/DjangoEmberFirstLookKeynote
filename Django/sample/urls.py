from django.conf.urls import url, include
from rest_framework import routers
from sample import views

router = routers.DefaultRouter()
router.register('samples', views.SampleViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
