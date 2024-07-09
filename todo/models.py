from django.db import models
from django.utils import timezone
STATUS = [
    ('INPROGRESS','INPROGRESS'),
    ('DONE','DONE')

]
class ToDo(models.Model):
    title = models.CharField( max_length=50)
    status = models.CharField( max_length=50 ,choices=STATUS)
    created_at = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
