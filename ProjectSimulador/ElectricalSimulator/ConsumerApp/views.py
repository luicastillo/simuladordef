from msilib.schema import Class
from optparse import Values
from os import times
from sqlite3 import Time
from django.shortcuts import render, redirect
from . models import DeviceModels
from . serializers import DeviceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib import messages
from ProducerApp import views as viewsproducer
import time
from datetime import date
import random
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

producer = viewsproducer.Producerdevice()


#Inicializacion objeto serializer
class DatosSimulador:
    def __init__(self, value):
        self.value = value
        self.create = date.today()

#Obtencion de datos del ProduccerApp

def consumer():
    while True:
        if not producer.cola.empty():
            item = producer.cola.get()
            producer.cola.task_done()
            logging.info(f'Nuevo elemento obtenido {item}')

            #incliyendo datos del simulador en la base de datos
            DateSimulator = DatosSimulador(value=item)
            DiccionarySimu = {"Values":DateSimulator.value, "Time":DateSimulator.create}
            
            #serializamos datos
            Devicesimulator = DeviceSerializer(data = DiccionarySimu)
            
            #validamos y guardamos
            if  Devicesimulator.is_valid():
                Devicesimulator.save()

            time_to_sleep = random.randint(1, 3)
            time.sleep(time_to_sleep)

@api_view(['GET'])
def MainSimulator(request):

    thread_producer = threading.Thread(target=producer.Producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_consumer.start()

    if request.method == 'GET':
        return redirect('/consumerapp/crud/') 



#Metodos API REST
@api_view(['GET','POST'])
def device_api_view(request):

    if request.method == 'GET':
        device = DeviceModels.objects.all()
        device_serializer = DeviceSerializer(device, many=True)
        return Response(device_serializer.data)

    if request.method == 'POST':
        device_serializer = DeviceSerializer(data=request.data)
        if device_serializer.is_valid():
            device_serializer.save()
            return redirect('/consumerapp/crud/')
        #    return Response(device_serializer.data)
        #return Response(device_serializer.errors)
        

@api_view(['POST'])
def Device_api_view_put(request, pk = None):

    if request.method == 'POST':
        device = DeviceModels.objects.filter(id = pk).first()
        device_serializer = DeviceSerializer(device, data=request.data)
        if device_serializer.is_valid():
            device_serializer.save()
            return redirect('/consumerapp/crud/')

    return redirect('/consumerapp/crud/')



def Device_delete(request, pk = None):
        device = DeviceModels.objects.filter(id = pk).first()
        device.delete()
        return redirect('/consumerapp/crud/')

def crud(request):
    Listadosimulador = DeviceModels.objects.all()
    messages.success(request,'¡Simulaciones listadas!')
    return render(request, "crud.html",{"simulador":Listadosimulador})

def editioncrud(request, codigo):
    Listadosimulador = DeviceModels.objects.get(id = codigo)
    return render(request, "ediciondevice.html",{"codigo":Listadosimulador})
