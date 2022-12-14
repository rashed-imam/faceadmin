from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageUploadSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import  status
from .models import Userface
from django.http import HttpResponse

class ImageUploadView(CreateAPIView):
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data['image'])


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Userface.objects.all()
    serializer_class = ImageUploadSerializer


    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        print(request.data,"rq datat")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
    # def perform_create(self, serializer):
    #     serializer.save()