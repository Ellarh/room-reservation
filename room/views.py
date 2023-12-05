from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Room, Reservation
from rest_framework.decorators import action
from .serializer import RoomSerializer, ReservationSerializer,RoomDetailSerializer
from rest_framework.renderers import TemplateHTMLRenderer


class RoomView(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = Room.objects.all()
    template_name = 'index.html'

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return RoomSerializer
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            return RoomDetailSerializer
        return RoomSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'room': serializer.data})

# Retrieve is a standard DRF method used for detail views
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        context = {'room_detail': serializer.data}
        return render(request, 'room_detail.html', context=context)


class ReservationView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(detail=False, methods=['POST', 'GET'])
    def reserve_booking(self, request):
        if request.method == 'POST':
            print(request.data)
            serializer = ReservationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return render(request, 'booking.html')


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        context = {'reservations': serializer.data}  # Update variable name to 'reservations'
        return render(request, 'booking.html', context=context)
