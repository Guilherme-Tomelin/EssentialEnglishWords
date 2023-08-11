from django.db import models

class Palavra(models.Model):
    word = models.CharField(max_length=80, null=False, blank=False)
    pronunciation = models.TextField(null=False, blank=False)
    translation = models.CharField(max_length=80, null=False, blank=False)


    def __str__(self):
        return f"Word [{self.word}]"