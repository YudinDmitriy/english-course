from django.urls import path

from main.views import learning_content, educational_and_thematic_plan, glossary, info_author, \
    introductory_info_section, exerc_sect_1, exerc_sect_2, exerc_sect_3, results, test_eng, SurveyTemplateView, \
    meta_info

app_name = 'main'


urlpatterns = [
    path('', learning_content, name='start_list'),
    path('thematic_plan', educational_and_thematic_plan, name='tem_plan'),
    path('glossary', glossary, name='glossary'),
    path('info_author', info_author, name='info_author'),
    path('info_section', introductory_info_section, name='info_section'),
    path('exerc_sect_1', exerc_sect_1, name='exerc_sect_1'),
    path('exerc_sect_2', exerc_sect_2, name='exerc_sect_2'),
    path('exerc_sect_3', exerc_sect_3, name='exerc_sect_3'),
    path('test_eng', test_eng, name='test_eng'),
    path('result', results, name='result'),
    path('survey', SurveyTemplateView.as_view(), name='survey'),
    path('meta_info', meta_info, name='meta_info'),

]


