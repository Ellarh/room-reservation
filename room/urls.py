from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomView, ReservationView

router = DefaultRouter()

router.register('room', RoomView, basename='room')
router.register('reservation', ReservationView, basename='reservations')

urlpatterns = [
    path('room_reservation/', include(router.urls)),
    path('room/<int:pk>/', RoomView.as_view({'get': 'retrieve'}), name='room_detail'),
    path('reserve/', ReservationView.as_view({'post': 'reserve_booking', 'get': 'list'}),
         name='reserve_booking'),
]
