from django.contrib import admin
from django.urls import path, include
from wiki.views import CreateNoteView, AllNoteView, NoteView


app_name = 'note'
urlpatterns = [
    path('note/create/', CreateNoteView.as_view()),
    path('note/all/', AllNoteView.as_view()),
    path('note/<int:pk>/', NoteView.as_view()),
    # path('note/auth/', include('djoser.urls')),
    # path('note/auth_token/', include('djoser.urls.authtoken')),
]
