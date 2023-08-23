from django.db import models
from police.models import Police
from citizen.models import Citizen
from case.models import Case

class Comment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user1 = models.ForeignKey(Police, null=True, blank=True, on_delete=models.SET_NULL)
    user2 = models.ForeignKey(Citizen, null=True, blank=True, on_delete=models.SET_NULL)
    case = models.ForeignKey(Case, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)
