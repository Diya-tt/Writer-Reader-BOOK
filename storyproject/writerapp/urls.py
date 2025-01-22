"""
URL configuration for demoproject project.

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
from writerapp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Home.as_view(),name="home_view"),
    path('signup',views.SignUpView.as_view(),name="signup_view"),
    path('',views.SignInView.as_view(),name="signin_view"),
    path('logout',views.SignOutView.as_view(),name="logout_view"),
    path('create',views.CreateStory.as_view(),name="create_view"),
    path('list',views.ListFormView.as_view(),name="list_view"),
    path('delete/<int:id>',views.DeleteFormView.as_view(),name="delete_view"),
    path('detail/<int:id>/',views.StoryDetailView.as_view(), name='story_detail'),
    path('edit/<int:id>/',views.StudEditView.as_view(), name='story_edit'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
