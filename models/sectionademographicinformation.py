from django.db import models
from .subjects import *

class SectionADemographicInformation(models.Model):
    # id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'ID', blank=True)
    # patient_number = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient Number', blank=True)
    a_mothers_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Mother's Name", blank=True)
    a_fathers_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Father's Name", blank=True)
    a_childs_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Child's Name", blank=True)
    a_guardians_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Guardian's Name", blank=True)
    a_address = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Address', blank=True)
    a_phone = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Phone Number', blank=True)
    a_email = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Email', blank=True)
    a_dob = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Patient's Date of Birth", blank=True)
    a_gender = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Gender', choices=[(1, u'M'), (2, u'F')])
    a_birth_state = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Place of Birth-state/province', blank=True)
    a_birth_city = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Place of Birth-city', blank=True)
    a_birth_country = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Place of Birth-country', blank=True)
    a_birth_weight_kg = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Birth Weight-kg', blank=True)
    a_birth_length_cm = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Birth Length-cm', blank=True)
    a_birth_length_in = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Birth Length-in', blank=True)
    a_full_term = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Full Term', choices=[(1, u'Yes'), (2, u'No')])
    a_gestation_age = models.IntegerField(help_text=u'', null=True, max_length=2000, verbose_name=u'Gestation age-wks', blank=True)
    a_age_diagnosed_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age diagnosed-comments', blank=True)
    a_age_diagnosed_in_months = models.IntegerField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age diagnosed-months', blank=True)
    a_symp_appear_age_in_months = models.IntegerField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age symptoms appear-month', blank=True)
    a_anyone_else_have_krabbe = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anyone else has Krabbe', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown')])
    a_relationship = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Relation', blank=True)
    a_sib_age_of_onset = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age of onset', blank=True)
    a_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Demographic Comments', blank=True) # This field type is a guess
    a_time_in_life = models.IntegerField(max_length=2000, help_text=u'', null=True, verbose_name=u'Phenotype', blank=True, choices=[(1, u'EIKD'), (2, u'LIKD'), (3, u'Adolescent'), (4, u'Adult'), (5, u'LOKD'), (6, u'Pre-symp EIKD'), (7, u'Pre-symp LOKD'), (8, u'Unaffected'), (9, u'High Risk')]) # This field type is a guess
    a_weight_percentile = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Weight percentile', blank=True)
    a_height_percentile = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Height percentile', blank=True)
    a_head_circ_percentile = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Head circumference percentile', blank=True)
    section_a_demographic_information_complete = models.IntegerField(max_length=30, help_text=u'', null=True, verbose_name=u'Demographic Information Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'krabbe_f_sectionademographicinformation'
         app_label = 'krabbe'
