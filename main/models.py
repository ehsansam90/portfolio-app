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

class SurveyQuestion(models.Model):
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('rating', 'Rating'),
        ('multiple_choice', 'Multiple Choice'),
    )

    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text

class SurveyOption(models.Model):
    question = models.ForeignKey(SurveyQuestion, related_name='options', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label} ({self.value})"
    
class SurveyResponse(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    user_response = models.CharField(max_length=255)
    user_ip = models.GenericIPAddressField()  # Optional: to store the user's IP address

    def __str__(self):
        return f'{self.question} - {self.user_response}'
    
class SurveySubmission(models.Model):
    submission_time = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField()
    
class Option(models.Model):
    value = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    

    
