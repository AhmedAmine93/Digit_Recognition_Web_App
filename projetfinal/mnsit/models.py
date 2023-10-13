from django.db import models


class Note(models.Model):
    title = models.CharField(
        max_length=50
    )  # Corrigé Charfield à CharField et max_lengt à max_length

    text = models.TextField()  # Corrigé TextFields à TextField et tesxt à text

    def __str__(self):
        return self.title
