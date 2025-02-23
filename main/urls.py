from django.urls import path

from main.views import learning_content, educational_and_thematic_plan, glossary, info_author, \
    introductory_info_section, exerc_sect_1

app_name = 'main'


urlpatterns = [
    path('', learning_content, name='start_list'),
    path('/thematic_plan', educational_and_thematic_plan, name='tem_plan'),
    path('/glossary', glossary, name='glossary'),
    path('/info_author', info_author, name='info_author'),
    path('/info_section', introductory_info_section, name='info_section'),
    path('/exerc_sect_1', exerc_sect_1, name='exerc_sect_1'),

]


