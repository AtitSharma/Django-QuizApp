from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name=("user")
        verbose_name_plural=("users")
    def __str__(self):
        return self.username
    
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True
    

class Category(BaseModel):
    category_name=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.category_name

class Quiz(BaseModel):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Result(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    marks=models.IntegerField(blank=True,null=True,default=0)

    def __str__(self):
        return str(self.user)
    



class Question(BaseModel):
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)
    # category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    


class Answer(BaseModel):
    question=models.ForeignKey(Question,related_name="answers",on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)


    def __str__(self):
        return self.answer

