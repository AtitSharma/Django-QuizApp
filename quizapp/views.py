from django.shortcuts import render,redirect,reverse
from quizapp.models import Question,Answer,Category,Result,Quiz
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from quizapp.forms import UserRegistaionForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    categories=Category.objects.all()
    quizs=Quiz.objects.all()
    for cat in categories:
        print(cat.id)
    context={
        "categories":categories,
        "quizs":quizs
    }
    return render(request,"quizapp/home.html",context)


def play_quiz_of_types(request,category):
    # quizs=Quiz.objects.filter(pk=quizid)
    quizs=Quiz.objects.filter(category__category_name=category)
    context={
        "quizs":quizs
    }
    return render (request,"quizapp/first_home.html",context)


def display_question_on_quiz_cat(request,quiztitle):
    questions=Question.objects.filter(quiz__title=quiztitle)
    context={
        "questions":questions
    }
    return render(request,"quizapp/hello.html",context)





# def play_quiz(request,category):
#     selected_category_questions=Question.objects.filter(category_name__category_name=category)
#     context={
#         "questions":selected_category_questions,
#         "category":category
#     }
#     return render(request,"quizapp/hello.html",context)


def check_answer(request):

    user_input=request.POST
    answer_ids = list(user_input.values())
    answer_ids=[i for i in answer_ids if i.isnumeric()]  
    # total_question=len(Question.objects.filter(category_name__category_name=category))
    answers=Answer.objects.filter(id__in=answer_ids)  
    # user_done_questions=len(answer_ids)
    marks=0
    correct=0
    incorrect=0
    for ans in answers:
        if ans.is_correct:
            marks+=5
            correct+=1
        else:
            incorrect+=1

    context={
        "marks":marks,
        "correct":correct,
        "incorrect":incorrect,
    } 


    # if request.POST and user_done_questions!=total_question:
    #     messages.add_message(request,messages.INFO,"Please give answer of all questions")
    #     return HttpResponseRedirect(reverse("quiz:play_quiz",args=(category,)))
    return render(request,"quizapp/result.html",context)




def register(request):
    form=UserRegistaionForm(request.POST)
    if form.is_valid():
          form.save()
          return redirect("quiz:login")
          
    context={
         "form":form
    }
    return render(request,"quizapp/register.html",context)
    



class Login(LoginView):
    template_name="quizapp/login.html"

@login_required
def log_out(request):
    logout(request)
    return redirect("quiz:login")
     
def Leader_Board(request):
    results=Result.objects.all()
    context={
        "results":results
    }
    return render(request,"quizapp/leaderboard.html",context)

    
    





    
