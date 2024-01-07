from django.db import models

class File(models.Model):
         name = models.CharField(max_length=100)
         file = models.FileField(upload_to='files/')
         uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
         uploaded_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
