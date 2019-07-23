from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.newBoard, name='newBoard'),
    path('list/', views.listBoard, name='listBoard'),
    path('view/<int:id>/', views.viewBoard, name='viewBoard'),
    path('update/<int:id>/', views.updatepage, name='updatepage'),
    path('updatedel/<int:id>', views.updatedel, name='updatedel'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
