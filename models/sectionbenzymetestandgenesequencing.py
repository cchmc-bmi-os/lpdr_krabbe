from django.db import models
from .subjects import *

class SectionBEnzymeTestAndGeneSequencing(models.Model):
    b_enzyme_level = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Enzyme level', blank=True)
    b_enzyme_normal_low = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Enzyme normal-low', blank=True)
    b_enzyme_normal_high = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Enzyme normal-high', blank=True)
    b_test_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Test location', blank=True)
    b_gene_mutation = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Gene mutation', blank=True)
    b_mutation_1 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Mutation 1', blank=True)
    b_mutation_2 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Mutation 2', blank=True)
    b_comments_1 = models.TextField(help_text=u'', null=True, verbose_name=u'Enzyme test and Gene sequencing Comments', blank=True) # This field type is a guess
    section_b_enzyme_test_and_gene_sequencing_complete = models.CharField(max_length=30, help_text=u'', null=True, verbose_name=u'Enzyme Test And Gene Sequencing Section Complete', blank=True, choices=[(0, u'Incomplete'), (1, u'Unverified'), (2, u'Complete')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'krabbe_f_sectionbenzymetestandgenesequencing'
         app_label = 'krabbe'
