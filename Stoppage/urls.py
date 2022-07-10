from django.urls import path
from .views import *



urlpatterns = [
    path("Acc_Data/",Acc_DataApiView.as_view(),name="Name"),

    path("Loc_Data/",Loc_DataApiView.as_view(),name="Name"),

    path("Stop_Data/",Stop_DataApiView.as_view(),name="Name"),


    path("stoppage/",Detect_StoppageApiView,name="Name"),

    ]