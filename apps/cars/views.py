from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from .serialiers import CarSerializers, CarSerializers2
from rest_framework import status


class CarListCrateView(APIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializers2(instance=cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarRetriveUpdateDestroyViev(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not found',status=status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        res = CarSerializers(car)
        return Response(res.data, status=status.HTTP_200_OK)
