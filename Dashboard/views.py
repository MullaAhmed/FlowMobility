from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response



class DashboardDayToDayThisMonthApiView(ViewSet):

    queryset = DashboardDayToDay.objects.filter()

    def list(self, request):
        print(datetime.today().month)
        serializer = DashboardDayToDaySerializer(self.queryset, many=True)
        return Response(serializer.data)



class DashboardDayToDayLastnApiView(ViewSet):
    
    serializer_class=DashboardDayToDaySerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('n')
    def list(self, request):
        n = self.kwargs.get(self.lookup_field)
        week = [datetime.today() - timedelta(days=n),datetime.today()]
        return DashboardDayToDay.objects.filter(date__range=week)


class DashboardDayToDayApiView(ListCreateAPIView):
    serializer_class=DashboardDayToDaySerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return [DashboardDayToDay.objects.filter().last()]


class DashboardHourToHourApiView(ListCreateAPIView):
    serializer_class=DashboardHourToHourSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return [DashboardHourToHour.objects.filter().last()]


class DashboardTripToTripApiView(ListCreateAPIView):
    serializer_class=DashboardTripToTripSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return [DashboardTripToTrip.objects.filter().last()]


class DashboardDayToDayDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=DashboardDayToDaySerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('date')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return DashboardDayToDay.objects.filter(date=uid)


class DashboardHourToHourDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=DashboardHourToHourSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('date')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return DashboardHourToHour.objects.filter(date=uid)


class DashboardTripToTripDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=DashboardTripToTripSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('date')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return DashboardTripToTrip.objects.filter(date=uid)