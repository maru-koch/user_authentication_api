"""auth_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

#: Defining Views for schema and documentation endpoints
PROJECT_TITLE = "User Authentication API"
PROJECT_DESCRIPTION = "A RESTful API to authenticate users"

# schema_view = get_schema_view(title = PROJECT_TITLE)
swagger_view = get_swagger_view(title = PROJECT_TITLE)
doc = include_docs_urls(title = PROJECT_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('account/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration', include('rest_auth.registration.urls')),
    path('swagger-docs/', swagger_view),
    path('docs', doc)

    # django_allauth

]
