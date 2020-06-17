from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Treasury_Yield
from .serializers import TreasuryYieldSerializer

class TreasuryYieldViewSet(viewsets.ModelViewSet):
    queryset = Treasury_Yield.objects.all()
    serializer_class = TreasuryYieldSerializer
# Create your views here.



# def fixincome(request):
#   return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
