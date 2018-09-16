# MasterClassDjango_final

Voici les fichiers de l'exercice fini.

Néanmoins, quelques modifications vous serons nécessaires pour pouvoir le faire fonctionner:

- Vous devez créer un environnement virtuel contenant python 3.6.5 ainsi que django version 2.1 ou plus

!!! SI VOUS N'UTILISEZ PAS POSTGRES:

- Vous devez modifier la partie relative à la base de données du fichier "settings.py" en remplaçant ce qui est présent par ceci:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

- Vous devez ensuite faire une migration pour que l'ORM crée les tables:

        Se placer à la racine du projet et utiliser les commandes suivantes:

        ./manage.py makemigrations
        ./manage.py migrate
