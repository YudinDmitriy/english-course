from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Question, Answer


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


def exerc_sect_2(request):
    return render(request, 'main/Exercises Section 2.html')


def exerc_sect_3(request):
    return render(request, 'main/Exercises Section 3.html')


def meta_info(request):
    return render(request, 'main/Meta_information_module.html')


def test_eng(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        total_questions = 2 * len(questions)
        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            try:
                answer = Answer.objects.get(id=selected_answer, question=question)
                if answer.is_correct:
                    score += 2
            except Answer.DoesNotExist:
                pass

        context = {
            'score': score,
            'total_questions': total_questions
        }
        return render(request, 'main/result.html', context)

    context = {
        'questions': questions
    }
    return render(request, 'main/test_eng.html', context=context)


def results(request):
    return render(request, 'main/result.html')


class SurveyTemplateView(TemplateView):
    template_name = "main/survey.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Survey"
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            ex_1_1 = request.POST.get("ex_1_1")
            ex_1_2 = request.POST.get("ex_1_2")
            ex_1_3 = request.POST.get("ex_1_3")
            ex_1_4 = request.POST.get("ex_1_4")
            ex_2_1 = request.POST.get("ex_2_1")
            ex_2_2 = request.POST.get("ex_2_2")
            ex_2_3 = request.POST.get("ex_2_3")
            ex_2_4 = request.POST.get("ex_2_4")
            ex_3_1 = request.POST.get("ex_3_1")
            ex_3_2 = request.POST.get("ex_3_2")
            ex_3_3 = request.POST.get("ex_3_3")
            ex_3_4 = request.POST.get("ex_3_4")
            ex_4_1 = request.POST.get("ex_4_1")
            ex_4_2 = request.POST.get("ex_4_2")
            if ex_1_1 not in ('None', None):
                print(f"Задание №1: 1.{ex_1_1},2.{ex_1_2},3.{ex_1_3},4.{ex_1_4}")
                print(f"Задание №1.2: 1.{ex_2_1},2.{ex_2_2},3.{ex_2_3},4.{ex_2_4}")
            if ex_3_1 not in ('None', None):
                print(f"Задание №3: 1.{ex_3_1},2.{ex_3_2},3.{ex_3_3},4.{ex_3_4}")
            if ex_4_1 not in ('None', None):
                print(f"Задание №4: 1.{ex_4_1},2.{ex_4_2}")
        return HttpResponseRedirect("/survey")
