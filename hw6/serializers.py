from django.db.models import Model
from rest_framework import serializers

from hw6.models import New, Publication, Law, Favourite


class FavouriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "id bools link_to_news".split()


class NewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "id title photo text date link".split()

    def to_representation(self, instance):
        data = super(NewListSerializer, self).to_representation(instance)
        bools = Favourite.objects.filter(link_to_news=instance).first()
        if bools:
            data["favourite"] = bools.bools
        else:
            data["favourite"] = False
        return data


class LawListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = "id title text category date".split()


class PublicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "id title text category date".split()


class FavouriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "id bools user link_to_news".split()


class FavouriteSerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField()

    class Meta:
        model = Favourite
        fields = "id news".split()

    def get_news(self, instance):
        n = New.objects.filter(favourite=instance).first()
        news = NewListSerializer(n).data
        return news
