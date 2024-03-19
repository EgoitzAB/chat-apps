from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_index, name='chat_index'),
    path('<str:room_name>/', views.room, name='room'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
