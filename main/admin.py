# admin.py

from django.contrib import admin
from .models import SurveyQuestion, Option, SurveyResponse, SurveySubmission

class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type')

class OptionAdmin(admin.ModelAdmin):
    list_display = ('value', 'label')

class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'user_response', 'user_ip')

class SurveySubmissionAdmin(admin.ModelAdmin):
    list_display = ('submission_time', 'user_ip')

admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(SurveySubmission, SurveySubmissionAdmin)
