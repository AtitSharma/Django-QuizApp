
from django.urls import path
from quizapp.views import(check_answer,home,register,
                          Login,Leader_Board,play_quiz_of_types
                          ,display_question_on_quiz_cat
)



app_name="quiz"

urlpatterns = [
    path('',home,name="home" ),
    path("check-answer",check_answer,name="check_answer"),
    # path("play-category/<str:category>/",play_quiz,name="play_quiz"),
    path("play-quiz-by-types/<str:category>/",play_quiz_of_types,name="play-types"),
    path("register/",register,name="register"),
    path("login/",Login.as_view(),name="login"),
    path("leaderboard/",Leader_Board,name="leaderboard"),
    path("display-question/<str:quiztitle>/",display_question_on_quiz_cat,name="display-cat")

]
