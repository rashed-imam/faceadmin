from rest_framework import serializers

from  .models import UserFace


# class UserfaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserFace
#         # fields = ('email', 'phone', 'query', 'type', 'status', 'response')
#


class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserFace
        fields= (
            'name',
            'image'
        )