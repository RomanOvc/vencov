from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

# from progEng.models import Citizen, Income
# from progEng.serializer import CitizenSerializer
#n
#
from rest_framework.views import APIView

from progEng.models import Citizen, Income, Zarplata, Persona

# from progEng.serializer import AlbumSerializer
from progEng.serializer import CitizenSerializer, IncomeSerializer, ZarplataSerializer, PersonaSerializer


class IncomesViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class CitizensViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

    def test(request):
        data = Citizen.objects.all()
        print(CitizenSerializer(data, many=True).data)
        return Response(CitizenSerializer(data, many=True).data)



class ZarplatsViewSet(viewsets.ModelViewSet):
    queryset = Zarplata.objects.all()
    serializer_class = ZarplataSerializer


class PersonsViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def test(request):
        data = Persona.objects.all()
        print(PersonaSerializer(data, many=True).data)
        return Response(PersonaSerializer(data, many=True).data)

