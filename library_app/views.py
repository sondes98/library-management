
from rest_framework import viewsets
from .models import Adherent, Livre, Auteur, Emprunt
from .serializers import AdherentSerializer, LivreSerializer, AuteurSerializer, EmpruntSerializer
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response

class AdherentViewSet(viewsets.ModelViewSet):
    queryset = Adherent.objects.all().order_by('nom_adh')
    serializer_class = AdherentSerializer


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all().order_by('titre_livre')
    serializer_class = LivreSerializer

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all().order_by('nom_auteur')
    serializer_class = AuteurSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

    @action(detail=False, methods=['get'])
    def most_borrowed_books(self, request):
        most_borrowed_books = (
            Livre.objects.annotate(borrow_count=Count('emprunt'))
                        .order_by('-borrow_count')[:10]
        )
        data = {'most_borrowed_books': [{'titre_livre': book.titre_livre, 'borrow_count': book.borrow_count} for book in most_borrowed_books]}
        return JsonResponse(data)

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

    @action(detail=False, methods=['get'])
    def loans_per_class(self, request):
        loans_per_class = (
            Adherent.objects.values('adherent_class')
                        .annotate(loan_count=Count('emprunt'))
                        .order_by('adherent_class')
        )
        data = {'loans_per_class': [{'adherent_class': adherent_class['adherent_class'], 'loan_count': adherent_class['loan_count']} for adherent_class in loans_per_class]}
        return JsonResponse(data)
