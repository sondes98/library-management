from rest_framework import serializers
from .models import Adherent, Livre, Auteur, Emprunt

class AdherentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adherent
        fields = '__all__'


class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = '__all__'

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'
