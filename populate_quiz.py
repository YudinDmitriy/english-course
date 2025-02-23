import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from main.models import Question, Answer


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
        {
            'text': 'What is bias in an article?',
            'answers': [
                {'text': "The author's use of clear and concise language.", 'is_correct': False},
                {'text': "The author's tendency to favor one viewpoint or perspective over others.", 'is_correct': True},
                {'text': "The author's attempt to present a balanced and neutral account of events.", 'is_correct': False},
                {'text': "The author's focus on providing detailed background information.", 'is_correct': False},
            ]
        },
        {
            'text': 'Which organizational structure is MOST likely to be used in an article that describes a series of events in the order they happened?',
            'answers': [
                {'text': "Chronological Order", 'is_correct': True},
                {'text': "Compare and Contrast", 'is_correct': False},
                {'text': "Cause and Effect", 'is_correct': False},
                {'text': "Problem and Solution", 'is_correct': False},
            ]
        },
        {
            'text': 'If an article presents a problem and then offers potential solutions, what organizational structure is used?',
            'answers': [
                {'text': "Chronological Order", 'is_correct': False},
                {'text': "Compare and Contrast", 'is_correct': False},
                {'text': "Spatial Order", 'is_correct': False},
                {'text': "Problem and Solution", 'is_correct': True},
            ]
        },
        {
            'text': 'Which of the following is the MOST effective way to identify the main idea of a paragraph?',
            'answers': [
                {'text': "Look for transition words.", 'is_correct': False},
                {'text': "Read the first and last sentence carefully.", 'is_correct': True},
                {'text': "Count the number of sentences.", 'is_correct': False},
                {'text': "Highlight all the nouns.", 'is_correct': False},
            ]
        },
        {
            'text': 'What is the best way to avoid plagiarism when writing about an article?',
            'answers': [
                {'text': "Change a few words here and there.", 'is_correct': False},
                {'text': "Copy and paste large sections of text without citing the source.", 'is_correct': False},
                {'text': "Always cite your sources, even when paraphrasing.", 'is_correct': True},
                {'text': "Only use information from one source.", 'is_correct': False},
            ]
        },
        {
            'text': 'What does evaluate the evidence presented in an article mean?',
            'answers': [
                {'text': "To simply accept all the evidence without questioning it.", 'is_correct': False},
                {'text': "To determine the source of the evidence.", 'is_correct': False},
                {'text': "To assess the strength, relevance, and credibility of the evidence.", 'is_correct': True},
                {'text': "To ignore any evidence that doesn't support your viewpoint.", 'is_correct': False},
            ]
        },
        {
            'text': 'When paraphrasing information from an article, what is the most important thing to remember?',
            'answers': [
                {'text': "Express the information in your own words and cite the source.", 'is_correct': True},
                {'text': "Use the exact same wording as the original source.", 'is_correct': False},
                {'text': "Change only a few words to make it slightly different.", 'is_correct': False},
                {'text': "Omit the source to make it appear as your original idea.", 'is_correct': False},
            ]
        },
        {
            'text': 'Which of the following best defines a thesis statement?',
            'answers': [
                {'text': "A brief summary of the article's main points.", 'is_correct': False},
                {'text': "A question that the article seeks to answer.", 'is_correct': False},
                {'text': "A list of sources used in the article.", 'is_correct': False},
                {'text': "The author's main argument or claim.", 'is_correct': True},

            ]
        },
        {
            'text': 'What is the BEST advice for approaching a long and complex article?',
            'answers': [
                {'text': "Break it down into smaller sections, define unfamiliar words, and take notes.", 'is_correct': True},
                {'text': "Give up if you don't understand it after the first read.", 'is_correct': False},
                {'text': "Read it as quickly as possible to get it over with.", 'is_correct': False},
                {'text': "Skim the article without paying attention to the details.", 'is_correct': False},
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
