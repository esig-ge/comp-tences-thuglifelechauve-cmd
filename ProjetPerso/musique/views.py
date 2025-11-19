from django.shortcuts import render, redirect, get_object_or_404
from .models import Musique

def musique_list(request):
    musiques = Musique.objects.all()

    # Gestion du formulaire (CREATE ou UPDATE)
    if request.method == "POST":
        musique_id = request.POST.get("musique_id")
        titre = request.POST.get("titre")
        artiste = request.POST.get("artiste")
        duree = request.POST.get("duree")
        genre = request.POST.get("genre")

        if musique_id:  # UPDATE
            musique = get_object_or_404(Musique, id=musique_id)
            musique.title = titre
            musique.artist = artiste
            musique.duration = duree
            musique.genre = genre
            musique.save()
        else:  # CREATE
            Musique.objects.create(
                title=titre,
                artist=artiste,
                duration=duree,
                genre=genre
            )
        return redirect("musique_list")

    return render(request, "musique/musique_list.html", {"musiques": musiques})
