from django.db import models


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    class Meta:
        db_table = "library_management_app_books"
