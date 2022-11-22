from rest_framework import serializers
from ..models import Country, Manuf , Car, Comment


class ManyfSer(serializers.ModelSerializer):
    class Meta:
        model = Manuf
        fields = ('id_manuf', 'manuf_name')

class CountrySerializer(serializers.ModelSerializer):
    manyf = ManyfSer(many=True, read_only=True)
    # manyf = serializers.CharField(source='manuf_name', max_length=150)
    class Meta:
        model = Country
        # fields = ('id_country', 'country_name')#, 'manyf')
        fields = ('id_country', 'country_name', 'manyf')

# class ManufSerializer(serializers.Serializer):
#     manuf_name = serializers.CharField(max_length=150)
#     country_name = serializers.CharField(source='manuf_country.country_name', max_length=150)
class ManufSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manuf
        fields = ('id_manuf', 'manuf_name', 'manuf_country')


# class CarSerializer(serializers.Serializer):
#     car_name = serializers.CharField(max_length=150)
#     car_manuf = serializers.CharField(source='car_manuf.manuf_name', max_length=150)
#     car_date_start_manuf = serializers.DateField()
#     car_date_end_manuf = serializers.DateField()
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id_car', 'car_name', 'car_manuf', 'car_date_start_manuf', 'car_date_end_manuf')


# class CommentSerializer(serializers.Serializer):
#     comment_email = serializers.EmailField(max_length=50)
#     comment_car = serializers.CharField(source='comment_car.car_name', max_length=150)
#     comment_date_publ = serializers.DateField()
#     comment_text_comment = serializers.CharField(allow_blank=True)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id_comment', 'comment_email', 'comment_car', 'comment_date_publ', 'comment_text_comment')