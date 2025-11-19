from django.shortcuts import render, redirect, get_object_or_404
from .models import Musique
def musique_list(request):
    # CREATE
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            title = request.POST.get("title")
            artist = request.POST.get("artist")
            duration = request.POST.get("duration")
            genre = request.POST.get("genre")
            Musique.objects.create(title=title, artist=artist, duration=duration, genre=genre)
        elif action == "edit":
            musique_id = request.POST.get("musique_id")
            musique = get_object_or_404(Musique, id=musique_id)
            musique.title = request.POST.get("title")
            musique.artist = request.POST.get("artist")
            musique.duration = request.POST.get("duration")
            musique.genre = request.POST.get("genre")
            musique.save()
        elif action == "delete":
            musique_id = request.POST.get("musique_id")
            musique = get_object_or_404(Musique, id=musique_id)
            musique.delete()
        return redirect("musique_list")

    musiques = Musique.objects.all()
    return render(request, "musique/musique_list.html", {"musiques": musiques})

