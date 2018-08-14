from django.db import models

class Subject(models.Model):
    patient_number = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient Number', blank=True)
    patient_number_anonymous = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient Number', blank=True)

    class Meta:
        app_label = 'krabbe'
        db_table = 'krabbe_s_subject'


class Record(models.Model):
    record = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Record ID', blank=True)
    patient_number = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient Number', blank=True)
    fam_id = models.CharField(help_text=u'', verbose_name=u'Family Id', max_length=10)
    subject = models.ForeignKey(Subject, blank=True, null=True, related_name='record')

    class Meta:
        app_label='krabbe'
        db_table = 'krabbe_s_record'
