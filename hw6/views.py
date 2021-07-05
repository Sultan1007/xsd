from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, viewsets
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from hw6.models import New, Law, Publication, Favourite
from hw6.serializers import NewListSerializer, LawListSerializer, PublicationListSerializer, FavouriteListSerializer, \
    FavouriteCreateSerializer, FavouriteSerializer


class NewsView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewListSerializer


class NewsViewItem(APIView):

    def get(self, request, pk):
        queryset = New.objects.filter(id=pk).first()
        serializer = NewListSerializer(queryset)
        return Response(serializer.data)


class LawView(generics.ListAPIView):
    queryset = Law.objects.all()
    serializer_class = LawListSerializer


class LawViewItem(APIView):

    def get(self, request, pk):
        queryset = Law.objects.filter(id=pk).first()
        serializer = LawListSerializer(queryset)
        return Response(serializer.data)


class PublicationView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationListSerializer


class PublicationViewItem(APIView):

    def get(self, request, pk):
        queryset = Publication.objects.filter(id=pk).first()
        serializer = PublicationListSerializer(queryset)
        return Response(serializer.data)


class FavouriteView(generics.ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            self.serializer_class = FavouriteSerializer
        elif self.request.method == "POST":
            self.serializer_class = FavouriteCreateSerializer
        return self.serializer_class
