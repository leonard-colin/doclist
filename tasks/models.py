from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    @classmethod
    def get_default_collection(cls):
        collection, _ = cls.objects.get_or_create(name="Défaut", slug="_default")
        return collection

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
