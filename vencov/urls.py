"""vencov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from progEng import views
# from progEng.views import CitizenView
from progEng.views import CitizensViewSet

router = routers.DefaultRouter()
# router.register(r'albums', views.AlbumViewSet)
router.register(r'citizens', views.CitizensViewSet)


router1 = routers.DefaultRouter()
router1.register(r'citizens', views.PersonsViewSet)


# app_name = "progEng"
urlpatterns = [
     path('', include(router.urls)),
     path('roman/', include(router1.urls)),
     path('admin/', admin.site.urls),
    # path('lol/',CitizenView.as_view()),
    #path('test/', views.test),
    # path('all/', views.index),
    # path('', views.index2)
]

