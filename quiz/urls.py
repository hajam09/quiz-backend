from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [
    path(
        'v1/essay-questions/',
        views.EssayQuestionApiV1.as_view(),
        name='v1-api-essay-questions'
    ),
    path(
        'v1/essay-questions/<int:pk>/',
        views.EssayQuestionDetailApiV1.as_view(),
        name='v1-api-essay-questions-detail'
    ),
    path(
        'v1/multiple-choice-questions/',
        views.MultipleChoiceQuestionApiV1.as_view(),
        name='v1-api-multiple-choice-questions'
    ),
    path(
        'v1/multiple-choice-questions/<int:pk>/',
        views.MultipleChoiceQuestionDetailApiV1.as_view(),
        name='v1-api-multiple-choice-questions-detail'
    ),
    path(
        'v1/true-or-false-questions/',
        views.TrueOrFalseQuestionApiV1.as_view(),
        name='v1-api-true-or-false-questions'
    ),
    path(
        'v1/true-or-false-questions/<int:pk>/',
        views.TrueOrFalseQuestionDetailApiV1.as_view(),
        name='v1-api-true-or-false-questions-detail'
    ),
    path(
        'v1/quizzes/',
        views.QuizApiV1.as_view(),
        name='v1-api-quizzes'
    ),
]
