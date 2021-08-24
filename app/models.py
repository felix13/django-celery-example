from django.db import models


class Comment(models.Model):
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
