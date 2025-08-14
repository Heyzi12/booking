from django.urls import path
from .views import home , room_info

urlpatterns = [
    path('', home, name='home'),
    path('room_info/<int:room_id>', room_info , name="room_info")
]