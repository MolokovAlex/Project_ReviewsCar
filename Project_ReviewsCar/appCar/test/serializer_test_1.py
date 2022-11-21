import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
from rest_framework import renderers, serializers





# модель "Страна"
class Country:
    def __init__(self, name):
        self.country_name = name

# модель "Производитель"
class Manuf:
    def __init__(self, name, manuf_country: Country):
        self.manuf_name = name
        self.manuf_country=manuf_country

# модель "Автомобиль"
class Car:
    def __init__(self, name, car_manuf: Manuf, date_start_manuf, date_end_manuf):
        self.car_name = name
        self.car_manuf = car_manuf
        self.car_date_start_manuf = date_start_manuf
        self.car_date_end_manuf = date_end_manuf

# модель "Комментарий"
class Comment:
    def __init__(self, email, comment_car: Car, date_publ, text_comment):
        self.comment_email = email
        self.comment_car = comment_car
        self.comment_date_publ = date_publ
        self.comment_text_comment = text_comment


country1 = Country('Russian Federation')
country2 = Country('Germany')
country3 = Country('Japan')
country4 = Country('USA')

manuf1 = Manuf('VAZ' ,country1)
manuf2 = Manuf('GAZ' ,country1)
manuf3 = Manuf('Toyota' ,country3)
manuf4 = Manuf('VW' ,country2)
manuf5 = Manuf('Audi' ,country2)
manuf6 = Manuf('Ford' ,country4)

car1 = Car('VAZ-2110', manuf1, '1980.01.01', '1999.01.01')
car2 = Car('GAZelle', manuf2, '1989.01.01', '2010.01.01')
car3 = Car('Fusion', manuf6, '2007.01.01', '2017.01.01')
car4 = Car('Land Cruiser', manuf3, '1980.01.01', '2022.01.01')

comment1 = Comment('w1@mail.ru', car1, '2020.01.01', 'help')
comment2 = Comment('w2@mail.ru', car3, '2020.01.01', 'good')
comment3 = Comment('w3@mail.ru', car4, '2020.01.01', 'very good')

queryset_country = [country1, country2, country3, country4]
queryset_manuf = [manuf1, manuf2, manuf3, manuf4, manuf5, manuf6]
queryset_car = [car1, car2, car3, car4]
queryset_comment = [comment1, comment2, comment3]


class CountrySerializer(serializers.Serializer):
    country_name = serializers.CharField(max_length=150)

class ManufSerializer(serializers.Serializer):
    manuf_name = serializers.CharField(max_length=150)
    country_name = serializers.CharField(source='manuf_country.country_name', max_length=150)

class CarSerializer(serializers.Serializer):
    car_name = serializers.CharField(max_length=150)
    car_manuf = serializers.CharField(source='car_manuf.manuf_name', max_length=150)
    car_date_start_manuf = serializers.DateField()
    car_date_end_manuf = serializers.DateField()

class CommentSerializer(serializers.Serializer):
    comment_email = serializers.EmailField(max_length=50)
    comment_car = serializers.CharField(source='comment_car.car_name', max_length=150)
    comment_date_publ = serializers.DateField()
    comment_text_comment = serializers.CharField(allow_blank=True)


serializer_obj = CountrySerializer(instance=queryset_country, many=True)
print(serializer_obj.data)
serializer_obj = ManufSerializer(instance=queryset_manuf, many=True)
print(serializer_obj.data)
serializer_obj = CarSerializer(instance=queryset_car, many=True)
print(serializer_obj.data)
serializer_obj = CommentSerializer(instance=queryset_comment, many=True)
print(serializer_obj.data)

# Рендерим данные в json
json_render_for_our_data = renderers.JSONRenderer()
data_in_json = json_render_for_our_data.render(serializer_obj.data)
print(data_in_json)



