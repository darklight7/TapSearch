from django.urls import path
from demo import views

urlpatterns = [
    path('snippets/', views.SnippetDetail.as_view()),
]
