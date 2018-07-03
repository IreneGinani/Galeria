from django.db import models

class Photo(models.Model):

    is_marked = False
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def marked(self):
    	return self.is_marked