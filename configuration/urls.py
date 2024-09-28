"""
URL configuration for configuration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from application import views

urlpatterns = [
    path('', views.main),
    path('/', views.main),
    path('admin/', admin.site.urls),
    path('registration', views.registration),
    path('login', views.login_controller),
    path('logout', views.logout_controller),
    path('account', views.account),
    path('article/<int:article_id>', views.get_article),
    path('articles/<str:topic>', views.get_articles_by_topic),
    path('add-article', views.add_article),
    path('delete-article/<int:article_id>', views.delete_article),
    path('edit-article/<int:article_id>', views.edit_article),
    path('add-comment/<int:article_id>', views.add_comment),
    path('profile/<str:username>', views.get_profile)
]
