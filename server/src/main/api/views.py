from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Car, Workshop, Project, Member, Timeline, Organiser
from .serializers import (CarModelSerializer, WorkshopModelSerializer, ProjectModelSerializer,
                            MemberModelSerializer, TimelineModelSerializer, OrganiserModelSerializer)


class CarListAPIView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarModelSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

