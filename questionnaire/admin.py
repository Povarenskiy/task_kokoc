from django.contrib import admin
from questionnaire.models import *

from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError

from nested_admin import NestedTabularInline, NestedModelAdmin


class AnswerInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(AnswerInlineFormSet, self).clean()
        
        if len(self.forms) == 1:
            raise ValidationError("There must be more than one answers")


class AnswersInLine(NestedTabularInline):
    formset = AnswerInlineFormSet
    model = Answer
    extra = 0


class TestsInLine(NestedTabularInline):
    model = Question
    inlines = [AnswersInLine]
    extra = 0


class SuiteAdmin(NestedModelAdmin):
    inlines = [TestsInLine]


admin.site.register(Test, SuiteAdmin)
admin.site.register(UserAnswer)

