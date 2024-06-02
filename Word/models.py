from django.db import models

class Word(models.Model):
    day = models.IntegerField()
    eng = models.TextField()
    kor = models.TextField()
    isDone = models.BooleanField(default=False)

    class Meta:
        db_table = 'Word'