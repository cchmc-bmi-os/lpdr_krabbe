from django.db import models
from .subjects import *

class SectionCNeurologicExam(models.Model):
    c_visiting_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Visiting date', blank=True)
    c_age_months = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age', blank=True)
    c_development = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Development', choices=[(1, u'Normal'), (2, u'Abnormal')])
    c_abnormal_specify = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal development', blank=True) # This field type is a guess
    c_cranial_nerves_done = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cranial Nerves done', choices=[(1, u'Yes')])
    c_cranial_nerves_other_specify = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cranial Nerves-Other, specify', blank=True)
    c_motor_exam_done = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Motor Exam done', choices=[(1, u'Yes')])
    c_cranial_nerves = models.CharField(max_length=300, blank=True, help_text=u'', null=True, verbose_name=u'Cranial Nerves', choices=[(0, 'Unknown'), (1, u'Normal'), (2, u'Smiling'), (3, u'Optic atrophy'), (4, u'Nystagmus'), (5, u'Facial disparesis'), (6, u'Decreased hearing'), (7, u'Blind'), (8, u'Estropia'), (9, u'Decreased vision'), (10, u'Other')])
    c_motor_increase_tone = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Motor Exam-increased tone', choices=[(0, u'Unknown'), (1, u'Peripheral'), (2, u'Axial'), (3, u'Appendages'), (4, u'Lower')])
    c_motor_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Motor Exam Comments', blank=True)
    c_deep_tend_reflx_done = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Deep Tendon Reflexes done', choices=[(1, u'Yes')])
    c_deep_tend_reflx_clonus = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Deep Tendon Reflexes-Clonus', choices=[(0, u'Unknown'), (1, u'Bilateral'), (2, u'Unilateral'), (3, u'Sustained'), (4, u'Unsustained')])
    c_cerebellar = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cerebellar (1yr+)', choices=[(1, u'Normal'), (2, u'Truncal ataxia'), (3, u'Dysmetria'), (4, u'Tremor')])
    c_sits = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Sits', choices=[(0, 'Unkown'), (1, u'Yes'), (2, u'No')])
    c_sits_age_months = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Sits-age', blank=True)
    c_walk_age_months = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Walk-Age', blank=True)
    c_speaking_age_months = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Speaking-Age', blank=True)
    c_head_circ_cm = models.FloatField(help_text=u'', null=True, verbose_name=u'Head circumference at time of neurologic exam', blank=True)
    c_head_circ_percentile = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Head circumference percentile at time of neurologic exam (in cm)', blank=True)
    c_weight_kg = models.FloatField(help_text=u'', null=True, verbose_name=u'Weight at time of neurologic exam (in kg)', blank=True)
    c_weight_percentile = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Weight percentile at time of neurologic exam', blank=True)
    c_height_cm = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Height at time of neurologic exam (in cm)', blank=True)
    c_height_percentile = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Height percentile at time of neurologic exam', blank=True)
    c_neurologic_exam_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Neurologic Exam Comments', blank=True) # This field type is a guess
    c_cranial_nerves_summary = models.CharField(help_text=u'1, Normal | 2, Smiling | 3, Optic atrophy | 4, Nystagmus | 5, Facial disparesis | 6, Decreased hearing | 7, Blind | 8, Estropia | 9, Decreased vision | 10, Other', null=True, max_length=2000, verbose_name=u'Cranial Nerves', blank=True)
    c_motor_exam_summary = models.CharField(help_text=u'1, Normal | 2, Normal (1yr+) | 3, Opisthotonus | 4, Poor head control | 5, Fisting | 6, Increased tone | 7, Decreased tone | 8, Hemiparesis | 9, diplegia | 10, Paraparesis | 11, Quadriparesis | 12, Pes Cavus | 13, Jittery', null=True, max_length=2000, verbose_name=u'Motor Exam', blank=True)
    c_motor_decrease_tone_summary = models.CharField(help_text=u'1, Peripheral | 2, Axial | 3, Trunk | 4, Central', null=True, max_length=2000, verbose_name=u'Motor Exam-decreased tone', blank=True)
    c_deep_tend_reflx_summary = models.CharField(help_text=u'1, Normal | 2, Increased | 3, Decreased', null=True, max_length=2000, verbose_name=u'Deep Tendon Reflexes', blank=True)
    c_deep_tend_reflx_babinski_summary = models.CharField(help_text=u'1, Yes | 2, No | 3, Equivocal', null=True, max_length=2000, verbose_name=u'Deep Tendon Reflexes-Babinski', blank=True)
    c_gait_summary = models.CharField(help_text=u'1, Normal | 2, Hemiparetic | 3, Ataxic | 4, diplegia | 5, Widebased | 6, Wheelchair', null=True, max_length=2000, verbose_name=u'Gait (1yr+)', blank=True)
    c_walk_summary = models.CharField(help_text=u'1, Yes | 2, No', null=True, max_length=2000, verbose_name=u'Walk', blank=True)
    c_speaking_summary = models.CharField(help_text=u'1, Yes | 2, No', null=True, max_length=2000, verbose_name=u'Speaking', blank=True)
    section_c_neurologic_exam_complete = models.CharField(max_length=30, help_text=u'', null=True, verbose_name=u'Neurologic Exam Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'krabbe_f_sectioncneurologicexam'
         app_label = 'krabbe'

class ccerebellar(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cerebellar (1yr+)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cerebellar (1yr+)', choices=[(1, u'Normal'), (2, u'Truncal ataxia'), (3, u'Dysmetria'), (4, u'Tremor')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_ccerebellar'
         app_label = 'krabbe'

class ccranialnerves(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cranial Nerves', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cranial Nerves', choices=[(1, u'Normal'), (2, u'Smiling'), (3, u'Optic atrophy'), (4, u'Nystagmus'), (5, u'Facial disparesis'), (6, u'Decreased hearing'), (7, u'Blind'), (8, u'Estropia'), (9, u'Decreased vision'), (10, u'Other')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_ccranialnerves'
         app_label = 'krabbe'


class cmotorexam(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Motor Exam', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Motor Exam', choices=[(1, u'Normal'), (2, u'Normal (1yr+)'), (3, u'Opisthotonus'), (4, u'Poor head control'), (5, u'Fisting'), (6, u'Increased tone'), (7, u'Decreased tone'), (8, u'Hemiparesis'), (9, u'diplegia'), (10, u'Paraparesis'), (11, u'Quadriparesis'), (12, u'Pes Cavus'), (13, u'Jittery')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_cmotorexam'
         app_label = 'krabbe'


class cmotordecreasetone(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Motor Exam-decreased tone', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Motor Exam-decreased tone', choices=[(1, u'Peripheral'), (2, u'Axial'), (3, u'Trunk'), (4, u'Central')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_cmotordecreasetone'
         app_label = 'krabbe'


class cdeeptendreflx(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Deep Tendon Reflexes', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Deep Tendon Reflexes', choices=[(1, u'Normal'), (2, u'Increased'), (3, u'Decreased')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
        db_table = 'krabbe_sc_cdeeptendreflx'
        app_label = 'krabbe'


class cdeeptendreflxbabinski(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Deep Tendon Reflexes-Babinski', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Deep Tendon Reflexes-Babinski', choices=[(1, u'Yes'), (2, u'No'), (3, u'Equivocal')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_cdeeptendreflxbabinski'
         app_label = 'krabbe'


class cgait(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Gait (1yr+)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Gait (1yr+)', choices=[(1, u'Normal'), (2, u'Hemiparetic'), (3, u'Ataxic'), (4, u'diplegia'), (5, u'Widebased'), (6, u'Wheelchair')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_cgait'
         app_label = 'krabbe'


class cwalk(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Walk', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Walk', choices=[(1, u'Yes'), (2, u'No')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_cwalk'
         app_label = 'krabbe'


class cspeaking(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Speaking', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Speaking', choices=[(1, u'Yes'), (2, u'No')])
    sectioncneurologicexam = models.ForeignKey(SectionCNeurologicExam)

    class Meta:
	 db_table = 'krabbe_sc_cspeaking'
         app_label = 'krabbe'
