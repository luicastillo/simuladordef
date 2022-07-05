from optparse import Values
from sqlite3 import Time
from rest_framework import serializers
from ConsumerApp.models import DeviceModels

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModels
        fields = '__all__'

#class SimulatorSerializer(serializers.Serializer):
#    Values = serializers.IntegerField()
#    Time = serializers.DateField()

#    class Meta:
#       model = DeviceModels
#        fields = '__all__'    