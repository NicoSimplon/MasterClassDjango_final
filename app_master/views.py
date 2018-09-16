from django.shortcuts import render
from django.contrib import messages
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import (Apprenant, Formateur, Hobbies)

from .forms import (HobbiesForm,)

# @login_required
# def requete(type_hobby, description):
#     with connection.cursor() as cursor:
#         cursor.execute("""
#         INSERT INTO "app_master_hobbies" ("type_hobby", "description") 
#         VALUES (%s, %s)
#         """, [type_hobby, description]
#         )

@login_required
def accueil(request):
    if request.method == 'POST':
        form = HobbiesForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Vous avez créé un nouveau hobby avec succès'
                )
            except:
                messages.add_message(
                    request, 
                    messages.ERROR, 
                    'Une erreur s\'est produite'
                )
    
    else:
        form = HobbiesForm()

        # type_hobby = request.POST.get("type_hobby")
        # description = request.POST.get("description")
        # requete(type_hobby, description)


    hobbies = Hobbies.objects.all()
    return render(request, 'accueil.html', {
        'form':form, 
        'hobbies':hobbies,        
    })

