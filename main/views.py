from django.shortcuts import render

# Create your views here.


def learning_content(request):
    return render(request, 'main/learning_content.html')


def educational_and_thematic_plan(request):
    return render(request, 'main/education_and_thematic_plan.html')


def glossary(request):
    return render(request,'main/glossary.html')


def info_author(request):
    return render(request, 'main/info_author.html')


def introductory_info_section(request):
    return render(request, 'main/introductory_information_section.html')


def exerc_sect_1(request):
    return render(request, 'main/Exercises Section 1.html')

