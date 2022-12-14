from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from .models import UserFace
from .recognition_controller import recognition_controller, has_face
from .serializers import ImageUploadSerializer


class ImageUploadView(CreateAPIView):
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data['image'])


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = UserFace.objects.all()
    serializer_class = ImageUploadSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        # path = "./face-data/"+self.request.data['image'].name
        path = f".{str(UserFace.objects.last())}"
        print(path)

        if not has_face(path):
            data = {"messages": "No face Found",
                    "isKnown": False,
                    }
            return JsonResponse(data=data, safe=False, status=status.HTTP_404_NOT_FOUND)

        results = recognition_controller(path)
        is_known = True
        if results == "Not Found":
            results = "User Not Found"
            is_known = False

        data = {"messages": results,
                "isKnown": is_known,
                }

        return JsonResponse(data=data, safe=False, status=status.HTTP_200_OK)

    # def perform_create(self, serializer):
    #     path = self.request.data['image'].name
    #     print(path.replace(" ", "_"))
    #     serializer.save(name=path.replace(" ", "_"))
