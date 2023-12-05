from rest_framework import serializers
from .models import Room, Reservation


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='room-detail', lookup_field='pk')

    class Meta:
        model = Room
        fields = '__all__'


class RoomDetailSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='room_detail', lookup_field='pk')

    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

