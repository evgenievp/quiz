from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import Group

from quiz.main_page.validators import validate_file_size


class QuizUser(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(6), ],
        null=False,
    )
    password = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        default='somepass'
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )
    profile_image = models.ImageField(
        validators=(validate_file_size,)

    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )


