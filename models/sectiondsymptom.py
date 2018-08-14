from django.db import models
from .subjects import *

class SectionDSymptom(models.Model):
    d_date_of_exam = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of exam', blank=True)
    d_age_month = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age', blank=True)
    d_crying_irritability = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Crying, irritability', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_crying_irritability_age = models.IntegerField(help_text=u'', null=True, max_length=2000, verbose_name=u'Crying, irritability-Onset age', blank=True)
    d_crying_irritability_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Crying, irritability-Comments', blank=True)
    d_poor_feeding = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Poor feeding', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_poor_feeding_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Poor feeding-Onset age', blank=True)
    d_poor_feeding_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Poor feeding-Comments', blank=True)
    d_feeding_tube = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Feeding tube', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_feeding_tube_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Feeding tube-Onset age', blank=True)
    d_feeding_tube_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Feeding tube-Comments', blank=True)
    d_stiffness = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stiffness', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_stiffness_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Stiffness-Onset age', blank=True)
    d_stiffness_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Stiffness-Comments', blank=True)
    d_stopped_smiling = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stopped smiling', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_stopped_smiling_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Stopped smiling-Onset age', blank=True)
    d_stopped_smiling_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Stopped smiling-Comments', blank=True)
    d_fisted_hand = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Fisted hand', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_fisted_hand_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Fisted hand-Onset age', blank=True)
    d_fisted_hand_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Fisted hand-Comments', blank=True)
    d_poor_head_control = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Poor head control', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_poor_head_control_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Poor head control-Onset age', blank=True)
    d_poor_head_control_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Poor head control-Comments', blank=True)
    d_arching = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Arching', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_arching_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Arching-Onset age', blank=True)
    d_arching_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Arching-Comments', blank=True)
    d_loss_of_vision = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Loss of vision', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_loss_of_vision_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Loss of vision-Onset age', blank=True)
    d_loss_of_vision_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Loss of vision-Comments', blank=True)
    d_loss_of_hearing = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Loss of hearing', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_loss_of_hearing_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Loss of hearing-Onset age', blank=True)
    d_loss_of_hearing_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Loss of hearing-Comments', blank=True)
    d_stumbling = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stumbling', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_stumbling_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Stumbling-Onset age', blank=True)
    d_stumbling_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Stumbling-Comments', blank=True)
    d_change_in_gait = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Change in Gait', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_change_in_gait_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Change in Gait-Onset age', blank=True)
    d_change_in_gait_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Change in Gait-Comments', blank=True)
    d_change_description = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Describe the change', blank=True)
    d_unsteady_gait = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Unsteady Gait', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_unsteady_gait_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Unsteady Gait-Onset age', blank=True)
    d_unsteady_gait_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Unsteady Gait-Comments', blank=True)
    d_onesided_weakness = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'One-sided weakness (hemiparesis)', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_onesided_weakness_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'One-sided weakness (hemiparesis)-Onset age', blank=True)
    d_onesided_weakness_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'One-sided weakness (hemiparesis)-Comments', blank=True)
    d_seizures = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Seizures', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_seizures_age = models.IntegerField(help_text=u'', null=True, max_length=2000, verbose_name=u'Seizures-Onset age', blank=True)
    d_seizures_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Seizures-Comments', blank=True)
    d_seizure_description = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Describe the seizures', blank=True)
    d_loss_of_milestones = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Loss of Milestones', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_loss_of_milestones_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Loss of Milestones-Onset age', blank=True)
    d_loss_of_milestones_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Loss of Milestones-Comments', blank=True)
    d_apnea = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Apnea (Irregular breathing)', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_apnea_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Apnea (Irregular breathing)-Onset age', blank=True)
    d_apnea_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Apnea (Irregular breathing)-Comments', blank=True)
    d_cardiac_arrhythmias = models.CharField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cardiac Arrhythmias (irregular heart rate)', choices=[(1, u'Yes'), (2, u'No'), (3, u'N/A')])
    d_cardiac_arrhythmias_age = models.FloatField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cardiac Arrhythmias (irregular heart rate)-Onset age', blank=True)
    d_cardiac_arrhythmias_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cardiac Arrhythmias (irregular heart rate)-Comments', blank=True)
    d_other_symptom = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Other symptom', blank=True)
    d_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Symptoms Comments', blank=True) # This field type is a guess
    section_d_symptoms_complete = models.CharField(max_length=30, help_text=u'', null=True, verbose_name=u'Symptoms Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'krabbe_f_sectiondsymptom'
         app_label = 'krabbe'