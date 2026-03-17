import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework import viewsets
from .models import Jugador
from .serializers import JugadorSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

@api_view(['GET'])
def partidos_argentinos(request):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {'x-apisports-key': settings.FOOTBALL_API_KEY}

    # Estrategia para Plan Gratis:
    # 1. Usamos una fecha específica de 2024 (donde hubo mucho movimiento)
    # 2. No usamos 'last' porque tu plan lo bloquea.
    # 3. Filtramos por la Liga Profesional (128) o Primera Nacional (129)
    querystring = {
        "league": "128", 
        "season": "2024",
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Si la fecha específica no trae nada, la API devuelve []
        raw_response = data.get('response', [])

        partidos = []
        # Limitamos a 5 en el loop de Python para no sobrecargar el Front
        for item in raw_response[:5]:
            partidos.append({
                'id': item['fixture']['id'],
                'liga': item['league']['name'],
                'fecha': item['fixture']['date'],
                'estado': item['fixture']['status']['short'],
                'local': item['teams']['home']['name'],
                'local_logo': item['teams']['home']['logo'],
                'visitante': item['teams']['away']['name'],
                'visitante_logo': item['teams']['away']['logo'],
                'goles_local': item['goals']['home'],
                'goles_visitante': item['goals']['away'],
            })

        return JsonResponse(partidos, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)