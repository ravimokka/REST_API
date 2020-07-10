"""REST_API_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from REST_API_App import views

router = routers.DefaultRouter()
router.register(r'shops', views.ShopsViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'media', views.MediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path(r'^api/(?P<id>\w{0,50})/$', views.FetchAPIData.as_view(), name='FetchAPIData'),
    path('api/product', views.FetchAPIData.as_view(), name='FetchAPIData'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]