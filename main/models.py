from django.db import models

class newyorknearby_trends(models.Model):
    month = models.CharField(max_length=3)  # Assuming 'Apr', 'Aug', etc.

    guttenberg_nj_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    guttenberg_nj_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hoboken_nj_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hoboken_nj_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    jersey_city_nj_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    jersey_city_nj_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    union_city_nj_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    union_city_nj_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    west_new_york_nj_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    west_new_york_nj_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    
class sandiegonearby_trends(models.Model):
    month = models.CharField(max_length=3)  # Assuming 'Apr', 'Aug', etc.

    la_mesa_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    la_mesa_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lemon_grove_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lemon_grove_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    national_city_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    national_city_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    santee_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    santee_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    spring_valley_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    spring_valley_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    
class sanfrancisconearby_trends(models.Model):
    month = models.CharField(max_length=3)  # Assuming 'Apr', 'Aug', etc.

    belvedere_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    belvedere_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    brisbane_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    brisbane_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    colma_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    daly_city_ca_2023 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    daly_city_ca_2024 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

