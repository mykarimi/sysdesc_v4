#!/usr/bin/env python
"""Author: M. Yassine Karimi"""
"""Date: September the 26th, 2015"""
"""Project BiographyNet: "Time Will Tell A Different Story" """
"""VU University Amsterdam"""

import os
import sys
import glob   
import csv
import fileinput
import lxml
import xml.etree.ElementTree as ET
import itertools
from os import listdir

#predefined descriptions
#creates variables of every possible combination    #polarity 	act or prop 	stated by 	applies to 
pos_act_1 = "positive action author subject"		#positive 	action 			author 		subject  				
pos_act_2 = "positive action author other"			#positive 	action 			author 		other	
pos_dscr_act_1 = "positive action extern subject" 	#positive 	action 			extern 		subject	
pos_dscr_act_2 = "positive action extern other"		#positive 	action 			extern 		other	
pos_char_1 = "positive property author subject"		#positive 	property 		author 		subject
pos_char_2 = "positive property author other"		#positive 	property 		author 		other
pos_indrct_1 = "positive property extern subject"	#positive 	property 		extern 		subject
pos_indrct_2 = "positiv property extern other"		#positive 	property 		extern 		other
neg_act_1 = "negative action author subject"		#negative 	action 			author 		subject
neg_act_2 = "negative action author other"			#negative 	action 			author 		other
neg_dscr_act_1 = "negative action extern subject"	#negative 	action 			extern 		subject
neg_dscr_act_2 = "negative action extern other"		#negative 	action 			extern 		other
neg_char_1 = "negative property author subject"		#negative 	property 		author 		subject
neg_char_2 = "negative property author other"		#negative 	property 		author 		other
neg_indrct_1 = "negative property extern subject"	#negative 	property 		extern 		subject
neg_indrct_2 = " negative property extern other"	#negative 	property 		extern 		other

#initiate countvariables
act_pos = 0 
act_neg = 0
char_pos = 0
char_neg = 0
ind_pos = 0
ind_neg = 0
act_descr_pos = 0
act_descr_neg = 0

#start countloop
for files in os.listdir('annotated/'):
	tree = ET.parse('annotated/'+files) 
	root = tree.getroot()

	target = open('counted_anottations.csv','w')

	for descriptions in root.findall('Markables'): 
		for descrip in descriptions.findall('DESCRIPTION'):
			act_prop = descrip.get('action_or_property')
			pol = descrip.get('polarity')
			stator = descrip.get('stated') 
			appl = descrip.get('appliesTo')
			descriptionsentence = "%s %s %s %s" % (pol, act_prop, stator, appl)
			if descriptionsentence == pos_act_1:
				act_pos += 1
			if descriptionsentence == pos_act_2:
				act_pos += 1
			if descriptionsentence == neg_act_1:
				act_neg += 1
			if descriptionsentence == neg_act_2:
				act_neg += 1
			if descriptionsentence == pos_char_1:
				char_pos += 1
			if descriptionsentence == pos_char_2:
				char_pos += 1
			if descriptionsentence == neg_char_1:
				char_neg += 1
			if descriptionsentence == neg_char_2:
				char_neg += 1
			if descriptionsentence == pos_indrct_1:
				ind_pos += 1
			if descriptionsentence == pos_indrct_2:
				ind_pos += 1
			if descriptionsentence == neg_indrct_1:
				ind_neg += 1
			if descriptionsentence == neg_indrct_2:
				ind_neg += 1
			if descriptionsentence == pos_dscr_act_1:
				act_descr_pos += 1
			if descriptionsentence == pos_dscr_act_2:
				act_descr_pos += 1
			if descriptionsentence == neg_dscr_act_1:
				act_descr_neg += 1 
			if descriptionsentence == neg_dscr_act_2:
				act_descr_neg += 1
		target_text = "polarity \t type of description \t count \t \n action: \t positive: \t %s \n action: \t negative: \t %s \n charachter: \t positive: \t %s \n charachter: \t negative: \t %s \n indirect: \t positive: \t %s \n indirect: \t negative: \t %s \n described action: \t positive: \t %s \n described action: \t negative: \t %s \n" % (act_pos, act_neg, char_pos, char_neg, ind_pos, ind_neg, act_descr_pos, act_descr_neg)
		target.write(target_text.encode('utf-8'))	
	target.close()
