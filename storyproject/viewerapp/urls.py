from django.contrib import admin
from django.urls import path
from viewerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1',views.Home1.as_view(),name='home1_view'),
    path('totallist',views.ViewerView.as_view(),name='total_view'),
    path('viewerdetail/<int:id>/',views.ViewerDetailView.as_view(), name='viewer_view'),
    path('comment/<int:id>/',views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:book_id>/', views.CommentListView.as_view(), name='comment_list'),
    
]