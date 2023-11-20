from rest_framework import serializers
from home.models import *


class TodoSerializers(serializers.ModelSerializer):
    """
    This Class for serialize todo model for create API.
    """

    user = serializers.SerializerMethodField()
    url_task = serializers.SerializerMethodField

    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        """
        This code takes the ID of the current user
        when creating a task and puts her ID in the user field
        """
        request = self.context["request"]
        validated_data["user"] = request.user.id
        return super().create(validated_data)


    def get_url_task(self, obj):
        """
        For show task url 
        """
        request = self.context["request"]
        return request.build_absolute_uri(obj.pk)
