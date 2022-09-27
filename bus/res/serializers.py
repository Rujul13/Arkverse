from rest_framework import serializers
from.models import uni

class uniserializer(serializers.ModelSerializer):
    class Meta:
        model = uni
        fields =['id','name','Affliation']