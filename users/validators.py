from django.core.exceptions import ValidationError

def validate_must_email(value):
    if not value.endswith('@must.ac.ug'):
        raise ValidationError('Only Mbarara University email addresses are allowed.')

def validate(value1,value2):
    if not value2.endswith('_'+value1+'@must.ac.ug'):
        raise ValidationError('Your username must be same as your student no')