import datetime

from django.db import models
from django.utils import timezone

## Pour gérer les modèles, suivre les 3 étapes:
## ============================================
## 1. Modifiez les modèles (dans models.py).
## 2. Exécutez python manage.py makemigrations pour créer des migrations correspondant à ces changements.
## 3. Exécutez python manage.py migrate pour appliquer ces modifications à la base de données.

## Manage command (django-admin) guide: <https://docs.djangoproject.com/fr/5.2/ref/django-admin/>

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

