from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from notes.models import Note
from notes.serializers import NoteSerializer


@csrf_exempt
def note_list(request):
    if request.method == "GET":
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonReponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class NoteListView:
    model = Note
    template = "notes/"
    context_object_name = "notes"
    ordering = ["-date_published"]
    paginate_by = 5
    pass


class NoteDetailView:
    pass


class NoteCreateView:
    pass


class NoteUpdateView:
    pass


class NoteDeleteView:
    pass


class UserNoteListView:
    pass
