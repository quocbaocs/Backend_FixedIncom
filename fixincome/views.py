from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Treasury_Yield
from .serializers import TreasuryYieldSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class TreasuryYieldViewSet(viewsets.ModelViewSet):
    queryset = Treasury_Yield.objects.all()
    serializer_class = TreasuryYieldSerializer
    authentication_classes =(TokenAuthentication,)
    permission_classed = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes =(TokenAuthentication,)

# Create your views here.



# def fixincome(request):
#   return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
