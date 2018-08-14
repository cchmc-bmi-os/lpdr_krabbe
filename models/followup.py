from django.db import models
from .subjects import *

class Followup(models.Model):
    censor_age = models.IntegerField(help_text=u'', null=True, verbose_name=u'Age at Follow-up with family (months)', blank=True)
    censor_date_2 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of follow-up with family', blank=True)
    censor_notes = models.TextField(help_text=u'', null=True, verbose_name=u'Summary of follow-up', blank=True) # This field type is a guess
    followup_complete = models.CharField(max_length=30, help_text=u'', null=True, verbose_name=u'Followup Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'krabbe_f_followup'
         app_label = 'krabbe'
