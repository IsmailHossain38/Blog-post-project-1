from django.db import models
from Cetagories.models import Cetagories
from Author.models import Author
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cetagorie = models.ManyToManyField(Cetagories) # ekta post onek cetagory te hote pare abar onk post ekta cetagories er hote
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title