from rest_framework import serializers,fields
from .models import *

class DashboardDayToDaySerializer(serializers.ModelSerializer):

    class Meta:
        model=DashboardDayToDay
        fields=(
                'id','username',     
                'date',
                'total_downloads',
                'total_drivers',
                'total_active_drivers',
                'active_drivers_to_downloads',
                'total_trips',
                'tota_distance',
                'average_distance_per_trip',
                'total_cashless_payments',
                'total_cash_payments',
                'total_drivers_revenue', 
                'total_meiro_revenue',
                )


class DashboardHourToHourSerializer(serializers.ModelSerializer):

    class Meta:
        model=DashboardHourToHour
        fields=(
               'id','username', 
               'date',
               'hour_slot',
               'total_trips')


class DashboardTripToTripSerializer(serializers.ModelSerializer):

    class Meta:
        model=DashboardTripToTrip
        fields=(
                'id','username', 
                'date',
                'trip_id',
                'trip_status',
                'driver_id',
                'driver_status',
        )
