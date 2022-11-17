from django.db import models

# модель "Страна"
class Country(models.Model):
    id_country = models.IntegerField(verbose_name='id_Country', primary_key=True, unique=True)
    country_name = models.CharField(verbose_name='Имя', max_length=150)

    def __str__(self) -> str:
        return self.country_name



# модель "Производитель"
class Manuf(models.Model):
    id_manuf = models.IntegerField(verbose_name='id_Manuf', primary_key=True, unique=True)
    manuf_name = models.CharField(verbose_name='Имя', max_length=150)
    manuf_country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.manuf_name



# модель "Автомобиль"
class Car(models.Model):
    id_car = models.IntegerField(verbose_name='id_Car', primary_key=True, unique=True)
    car_name = models.CharField(verbose_name='Имя', max_length=150)
    car_manuf = models.ForeignKey('Manuf', on_delete=models.PROTECT, null=True)
    car_date_start_manuf = models.DateField(verbose_name='Год начала выпуска' )
    car_date_end_manuf = models.DateField(verbose_name='Год окончания выпуска' )

    def __str__(self) -> str:
        return self.car_name




# модель "Комментарий"
class Comment(models.Model):
    id_comment = models.IntegerField(verbose_name='id_Comment', primary_key=True, unique=True)
    comment_email = models.EmailField(verbose_name='Email автора', max_length=50)
    comment_car = models.ForeignKey('Car', on_delete=models.PROTECT, null=True)
    comment_date_publ = models.DateField(auto_now_add=True, verbose_name='Дата создания', max_length=150)
    comment_text_comment = models.TextField(verbose_name='Текст комментария', max_length=150)

    def __str__(self) -> str:
        return self.comment_email