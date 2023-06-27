from django.db import models

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extension)

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    # image = models.ImageField(upload_to=image_upload)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'recipe_table'

    