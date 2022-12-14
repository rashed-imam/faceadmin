from rest_framework import serializers

from  .models import Userface


# class UserfaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Userface
#         # fields = ('email', 'phone', 'query', 'type', 'status', 'response')
#


class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Userface
        fields= (
            'name',
            'image'
        )