from django.db import models

# Create your models here.

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=False)
    op1 = models.CharField(max_length=200,null=False)
    op2 = models.CharField(max_length=200,null=False)
    op3 = models.CharField(max_length=200,null=False)
    op4 = models.CharField(max_length=200,null=False)
    ans = models.CharField(max_length=200,null=False)
    
    
    def __str__(self):
        return self.question