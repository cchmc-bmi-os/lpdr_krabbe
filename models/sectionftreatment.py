from django.db import models
from .subjects import *

class SectionFTreatment(models.Model):
    f_child_transplanted = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Was the child transplanted?', choices=[(1, u'Yes'), (2, u'No')])
    f_child_trans_bf_after_symp = models.CharField(max_length=2000, help_text=u'', null=True, verbose_name=u'Was the child transplanted before or after symptoms?', blank=True, choices=[(1, u'Transplant at Birth and prior to symptoms'), (2, u'Transplanted prior to symptoms'), (3, u'Transplanted After Symptoms')]) # This field type is a guess
    f_child_transplanted_where = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where', blank=True)
    f_child_transplanted_when = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'When', blank=True)
    f_transplant_age_months = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age', blank=True)
    f_child_condition_now = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'How is the child now?', blank=True)
    f_transplant_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Transplant Comments', blank=True) # This field type is a guess
    section_f_treatment_complete = models.CharField(max_length=30, help_text=u'', null=True, verbose_name=u'Treatment Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess  
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
         db_table = 'krabbe_f_sectionftreatment'
         app_label = 'krabbe'
