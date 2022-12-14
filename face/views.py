from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageUploadSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import  status
from .models import UserFace
from django.http import HttpResponse
from recognition_controller import recognition_controller

class ImageUploadView(CreateAPIView):
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data['image'])


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = UserFace.objects.all()
    serializer_class = ImageUploadSerializer


    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        print(request.data,"rq datat")
        results = recognition_controller(request.img_path)
        return HttpResponse(results)
    # def perform_create(self, serializer):
    #     serializer.save()