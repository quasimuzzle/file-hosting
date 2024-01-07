from django.db import models

# модель данных для хранения файла
class File(models.Model):
         name = models.CharField(max_length=100)
         file = models.FileField(upload_to='files/')
         uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
         uploaded_at = models.DateTimeField(auto_now_add=True)


