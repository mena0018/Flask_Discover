# Convertit une durée exprimée en minutes en une chaîne de caractères * ayant la
# forme HH:MM
# Si nécessaire, le nombre d'heures peut comporter plus de 2 chiffres.
# param $minutes durée en minutes
# return résultat

def durationToString(minutes: int) -> str:
    heure = minutes // 60
    minutes = minutes % 60

    if heure < 10:
        heure = '0' + str(heure)

    if minutes < 10:
        minutes = '0' + str(minutes)

    return str(heure) + ":" + str(minutes)


# Convertit une note entière comprise entre 0 et $max en une chaîne de caractères
# composée d'étoiles.
# param $rating note comprise entre 0 et $max
# param $max valeur maximale de la note
# return chaîne de caractères composée d'étoiles

def ratingToStars(rating, max=10):
    noir = "\u2605"
    blanc = "\u2606"
    affichage = ''

    if rating >= 0 and rating <= max:
        for i in range(rating):
            affichage += noir
        for i in range(max - rating):
            affichage += blanc
    else:
        affichage = 'ERREUR : Choisissez un nombre compris entre 0 et 8'

    return affichage


# Classe représentant un film.
class Movie:
    def __init__(self, _title: str, _duration: int, _rating: float = 0.0):
        self._title = _title
        self._duration = _duration
        self._rating = _rating

        if _rating < 0 or _rating > 10:
            raise ValueError("Valeur inférieur à 0 ou supérieur à 10")

    # Mise en place de la propriété “title” en lecture seule
    def _getTitle(self) -> str:
        return self._title

    @property
    def title(self) -> str:
        """
        Retourne le titre du film.
        Retour:
        Titre du film
        """
        return self._getTitle()

    # Mise en place de la propriété “duration” en lecture seule
    def _getDuration(self) -> int:
        return self._duration

    @property
    def duration(self) -> int:
        """
        Retourne la durée du film (exprimée en minutes).
        Retour:
        Durée du film
        """
        return self._getDuration()

    # Mise en place de la proprité “rating” en lecture et écriture
    def _getRating(self) -> float:
        return self._rating

    @property
    def rating(self) -> float:
        """
        Retourne la note donnée au film (comprise entre 0 et 10).
        Retour:
        Note du film
        """
        return self._getRating()

    @rating.setter
    def rating(self, r: float) -> None:
        """
        Modifie la note du film.
        La note doit être comprise entre 0 et 10
        Paramètre:
        r: nouvelle note du film (entre 0 et 10)
        """
        self._setRating(r)

    def _setRating(self, rating: float) -> None:
        """
        Modifie la note du film
        Paramètre:
        rating: nouvelle note du film
        Exception:
        ValueError: si la note n’est pas comprise entre 0 et 10
        """
        if not 0.0 <= rating <= 10.0:
            raise ValueError(f"La note {rating} doit être comprise entre 0 et 10")
        self._rating = rating

    def __repr__(self) -> str:
        minutes = durationToString(self.duration)
        return f"{self.title} ({minutes})\n {ratingToStars(9)}"
