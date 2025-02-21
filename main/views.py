from django.shortcuts import render

# Create your views here.


def learning_content(request):
    return render(request, 'main/learning_content.html')


def educational_and_thematic_plan(request):
    return render(request, 'main/education_and_thematic_plan.html')

def glossary(request):
    return  render(request,'main/glossary.html')

