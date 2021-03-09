
# Serializers converted to query's into JSON, XML or other content types.
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import personalInfo


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:    #pylint: disable=too-few-public-methods
        # Return Profile fields.
        model = personalInfo
        fields = "__all__"
