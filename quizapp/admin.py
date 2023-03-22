from django.contrib import admin
from quizapp.models import Question,Answer,Category,Result,Quiz



# Register your models here.

admin.site.register(Category)
admin.site.register(Quiz)
# @admin.register(Category)
# class QuizAdminCategory(admin.ModelAdmin):
#     pass


class QuizAdminAnswer(admin.StackedInline):
    model=Answer
    extra=0



@admin.register(Question)
class QuizAdminQuestion(admin.ModelAdmin):
    inlines=[QuizAdminAnswer]



# admin.site.register(Question,QuestionAdmin)
admin.site.register(Result)





