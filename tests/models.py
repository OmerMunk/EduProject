from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import RESTRICT


class MetaModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract =True

class Student(MetaModel):
    full_name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=256, null=False, blank=False)
    phone_num = models.CharField(max_length=16, null=False, blank=False)


    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.full_name


class Test(MetaModel):
    name = models.CharField(max_length=64, null=False, blank=False)
    subject = models.CharField(max_length=32, null=False, blank=False)
    questions = models.ManyToManyField('Question', blank=True)


    class Meta:
        db_table = "Test"

    def __str__(self):
        return self.name


class Question(MetaModel):
    question = models.CharField(max_length=256, null=True, blank=True)
    option1 = models.CharField(max_length=256, null=True, blank=True)
    option2 = models.CharField(max_length=256, null=True, blank=True)
    option3 = models.CharField(max_length=256, null=True, blank=True)
    option4 = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = "Question"

    def __str__(self):
        return self.question


class TestExecuted(MetaModel):
    student_id = models.ForeignKey(Student, on_delete=RESTRICT)
    test_id = models.ForeignKey(Test, on_delete=RESTRICT)
    correct = models.IntegerField(null=False, blank=False)
    wrong = models.IntegerField(null=False, blank=False)
    grade = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        null=True,
        blank=True
    )










