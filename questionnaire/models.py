from django.db import models
from users.models import *


class Test(models.Model):
    topic = models.TextField(max_length=255, verbose_name='Тема теста')
    reward = models.IntegerField(verbose_name='Награда за прохождение')

    def __str__(self):
        return f'{self.topic.capitalize()}'


class Question(models.Model):
    text = models.TextField(max_length=255, verbose_name='Текст вопроса')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'Вопрос id {self.id} по теме "{self.test}"'


class Answer(models.Model):
    text = models.TextField(max_length=255, verbose_name='Текст ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ответ id {self.id} на вопрос id {self.question_id}'


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE) 

    def __str__(self):
        return f'Ответ пользователя {self.user} на вопрос id {self.question_id}'

