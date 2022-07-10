from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.shortcuts import render,HttpResponse
from .serializers import *
from .models import *
import numpy as np
import pandas as pd
from .utils import *


class Acc_DataApiView(ListCreateAPIView):
    serializer_class=Acc_DataSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Acc_Data.objects.filter()

class Loc_DataApiView(ListCreateAPIView):
    serializer_class=Loc_DataSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Loc_Data.objects.filter()


class Stop_DataApiView(ListCreateAPIView):
    serializer_class=Stop_DataSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Stop_Data.objects.filter()


def Detect_StoppageApiView(response):
    df = pd.DataFrame(list(Acc_Data.objects.all().values()))
    print(df)
    
    return HttpResponse(get_detection(df))



