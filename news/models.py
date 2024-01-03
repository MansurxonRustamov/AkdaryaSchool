from django.db import models



class NewsSchool(models.Model):
    title = models.CharField(max_length=250)
    about = models.TextField()
    hashtag = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='news/images/')
    video = models.FileField(upload_to='news/videos/', null=True, blank=True)
    time = models.DateTimeField()

    def __str__(self):
        return self.title
    

