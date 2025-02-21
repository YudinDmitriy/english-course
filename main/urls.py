from django.urls import path

from main.views import learning_content, educational_and_thematic_plan, glossary

app_name = 'main'


urlpatterns = [
    path('', learning_content, name='start_list'),
    path('/thematic_plan', educational_and_thematic_plan, name='tem_plan'),
    path('/glossary', glossary, name='glossary'),

]


