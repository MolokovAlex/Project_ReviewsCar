from rest_framework import serializers



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