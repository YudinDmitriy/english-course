from django.shortcuts import render

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

