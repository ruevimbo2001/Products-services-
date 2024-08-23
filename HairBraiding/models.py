from django.db import models

class HairbraidingService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price =  models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(upload_to='hair_braiding_images/'),
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
