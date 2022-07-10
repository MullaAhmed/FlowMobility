from rest_framework import serializers,fields
from .models import *


class Acc_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model=Acc_Data
        fields=(
               'id',
               'date',
               'sensor',
               'timestamp',
               'x',
               'y',
               'z',)

class Loc_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model=Loc_Data
        fields=(
               'id',
               'date',
               'latitude',
               'longitude'
            )

class Stop_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stop_Data
        fields=(
               'latitude',
               'longitude'
            )
