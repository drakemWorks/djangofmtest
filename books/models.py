from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(("Title"), max_length=250)
    subtitle = models.CharField(("Subtitle"), max_length=250)
    author = models.CharField(("Author"), max_length=250)
    isbn = models.CharField(("ISBN"), max_length=13)

    def __str__(self):
        return self.title
