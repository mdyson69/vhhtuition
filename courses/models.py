from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    level = models.CharField(max_length=10)
    pdf_url = models.CharField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    course_views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
