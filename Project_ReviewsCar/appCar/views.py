from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class GetCountryInfoView(APIView):
    def get(self, request):
        # Извлекаем набор всех записей из таблицы Country
        queryset_country = Country.objects.all()
        # Создаём сериалайзер для извлечённого наборa записей
        serializer_for_queryset_country = CountrySerializer(
            instance=queryset_country,  
            many=True 
        )
        return Response(serializer_for_queryset_country.data)



def indexPage(request):
    """
    Первая станица. Отображение всех комментариев.
    """
    list_of_country = Country.objects.all()
    context = {'list_of_country': list_of_country}
    return render(
        request=request,
        template_name='appcar\index.html',
        context=context
    )
    
    
    
    # return render(request, 'appcar\index.html')