from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    age = models.IntegerField()
    retired = models.BooleanField()

    def __str__(self):
        return (f"Author {self.first_name} {self.last_name}, "
                f"pseudonym {self.pseudonym}, age {self.age}")
