from django.db import models

class Mymodel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_auto_field = models.BigIntegerField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()

    def __str__(self):
        return f"Name : {self.char_field}"