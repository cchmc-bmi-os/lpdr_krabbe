from django.db import models
from .subjects import *

class SectionGDeath(models.Model):
    g_death = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Death', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown')])
    g_death_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Death Date', blank=True)
    g_age_at_death_months = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age at death', blank=True)
    g_death_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Death Comments', blank=True) # This field type is a guess
    g_if_alive_current_status = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'If alive, current status', blank=True)
    section_g_death_complete = models.CharField(max_length=30, help_text=u'', null=True, verbose_name=u'Death Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'krabbe_f_sectiongdeath'
         app_label = 'krabbe'
