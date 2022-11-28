from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from .serialiers import CarSerializers, CarSerializers2


class CarListCrateView(APIView):

    def get(self,*args,**kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializers2(instance=cars, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
