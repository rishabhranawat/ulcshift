from django.db import models

# Create your models here.
class Tutor(models.Model):
	username = models.CharField(max_length = 254, blank = False)
	email = models.EmailField(max_length = 254, blank = False)
	number_of_subs = models.IntegerField(default = 0)

class Subs(models.Model):
	by = models.ForeignKey('Tutor', related_name = 'Who')
	to = models.ForeignKey('Tutor', null = True, related_name = 'Whom')
	where = models.CharField(max_length = 254, blank = False)
	courses = models.CharField(max_length = 254, blank = False)
	time = models.CharField(max_length = 254, blank = False)
	pay = models.NullBooleanField()
