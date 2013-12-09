from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.


class Page(models.Model):
    """
    Page model.
    """
    name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex='^[a-z]+$',
                message='Page name must be a single lower case word.',
            )
        ],
        unique=True,
    )
    #page_name.unique = True
    contents = models.TextField()


def validate_word(value):
    """ Validate page name is a word. """
    if True:
        raise ValidationError(u'{} is not a word.'.format(value))
