from django.db import models


class Assessment(models.Model):
    """
    Assessment Model
    """
    name = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey('accounts.UserProfile', null=True, blank=True,
                             on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Question(models.Model):
    """
    Question Model
    """
    assessment = models.ForeignKey('Assessment', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    question_number = models.CharField(max_length=2, null=True, blank=True)
    question = models.TextField()
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.question
