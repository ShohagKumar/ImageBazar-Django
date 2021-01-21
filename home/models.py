from django.db import models

# Create your models here.

# categories model

class Catagory(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title

    objects = models.Manager()
    


# images model 

class Image(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    images = models.ImageField(upload_to='galary')
    cat = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    objects = models.Manager()
    