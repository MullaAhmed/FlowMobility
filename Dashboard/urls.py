from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'DashboardDayToDayLastn/(?P<n>\d+)', DashboardDayToDayLastnApiView,basename='Last n days request api endpoint')
router.register(r'DashboardDayToDayThisMonth', DashboardDayToDayThisMonthApiView)

urlpatterns = [
    path("DashboardDayToDay/",DashboardDayToDayApiView.as_view(),name="Day to Day"),
    path("DashboardDayToDay/<slug:date>/",DashboardDayToDayDetailApiView.as_view(),name="Day to Day"),
    path("DashboardHourToHour/",DashboardHourToHourApiView.as_view(),name="Hour to Hour"),
    path("DashboardTripToTrip/",DashboardTripToTripApiView.as_view(),name="Trip to Trip"),

    path('', include(router.urls)),
   
    ]