import os
import django
from main.models import Question, Answer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def add_questions_and_answers():
    """функция для добавления вопросов в бд"""
    questions_data = [
        {
            'text': 'Which of the following is the MOST common purpose of a news report?',
            'answers': [
                {'text': "To express the author's personal opinion.", 'is_correct': False},
                {'text': 'To entertain the reader with a fictional story.', 'is_correct': False},
                {'text': 'To present factual information about current events.', 'is_correct': True},
                {'text': 'To analyze a topic using a highly subjective viewpoint.', 'is_correct': False},
            ]
        },
        
    ]

    for question_data in questions_data:
        question = Question.objects.create(text=question_data['text'])
        for answer_data in question_data['answers']:
            Answer.objects.create(question=question, text=answer_data['text'], is_correct=answer_data['is_correct'])

    print("Вопросы и ответы добавлены в базу данных!")


if __name__ == '__main__':
    add_questions_and_answers()
