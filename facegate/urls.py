"""
URL configuration for facegate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie
from graphene_django.views import GraphQLView
from facegate.schema import schema
from consumers.views import recognize_face, user_list, create_user
from consumers.schema import UserQuery
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))),
    path('usuarios/', user_list, name='user_list.html'),
    path('create-user/', create_user, name='create_user.html'),
    path('recognize-face/', recognize_face, name='recognize_face'),
]
