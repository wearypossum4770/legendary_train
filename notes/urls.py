from django.urls import path

from notes.views import (
    NoteListView,
    NoteCreateView,
    NoteDeleteView,
    NoteDetailView,
    NoteUpdateView,
    UserNoteListView,
)

urlpatterns = [
    # path('',NoteListView.as_view(), name='blog-home'),
    path("user/<str:username>", UserNoteListView.as_view(), name="user-notes"),
    path("note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
    path("note/new/", NoteCreateView.as_view(), name="note-create"),
    path("note/<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
    # path('about/', views.about, name='blog-about'),
]
