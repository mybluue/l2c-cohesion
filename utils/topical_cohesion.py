from .knowledge import word2tags
import numpy as np


def get_SO_TTR_RATIO_cohesion(essay_SVO):
	essay_subject = []
	essay_noun_subject = []
	essay_pronoun_subject = []

	for sent_SVO in essay_SVO:
		for subsent_SVO in sent_SVO:
			if len(subsent_SVO) == 6:
				essay_subject.append(subsent_SVO[0])
				
				if subsent_SVO[3] == 'n':
					essay_noun_subject.append(subsent_SVO[0])
				elif subsent_SVO[3] == 'r':
					essay_pronoun_subject.append(subsent_SVO[0])

	subj_n_TTR = len(list(set(essay_noun_subject))) / (len(essay_noun_subject) + 1)
	subj_TTR = len(list(set(essay_subject))) / (len(essay_subject) + 1)
	
	subj_p_RATIO = len(essay_pronoun_subject) / (len(essay_subject) + 1)
	subj_n_RATIO = len(essay_noun_subject) / (len(essay_subject) + 1)

	return subj_TTR, subj_n_TTR, subj_p_RATIO, subj_n_RATIO



def get_SO_lgcohesion(essay_SVO):
	local_subj_cohesion = 0
	global_subj_cohesion = 0
	sent_count = len(essay_SVO)
	for i in range(0,sent_count-1):
		for j in range(i+1,sent_count):
			sent1_subject = [t[0] for t in essay_SVO[i] if t]
			sent2_subject = [t[0] for t in essay_SVO[j] if t]
			subject_overlap = len(list(set(sent1_subject).intersection(set(sent2_subject))))
			if j == i+1:
				local_subj_cohesion += subject_overlap
			global_subj_cohesion += subject_overlap
			
	local_subj_cohesion /= (sent_count + 1)
	global_subj_cohesion /= ((sent_count - 1) * sent_count / 2 + 1)
	
	return local_subj_cohesion, global_subj_cohesion


def get_agregation_cohesion(essay_SVO):
	cur_svo = essay_SVO
	subjs = [subj[0] for sent in cur_svo for subj in sent if subj]
	subjs = [w for w in subjs if w in word2tags.keys()]
	subjs = list(set(subjs))
	subjs_label = [word2tags[subj][0][0] for subj in subjs if subj in word2tags.keys()]

	subj_sc_num = len(set(subjs_label))
	subj_sc_density = round(len(subjs)/subj_sc_num, 3)
	return subj_sc_num, subj_sc_density


def get_subj_density(essay_SVO, essay_words):
	subjs = [subj[0] for sent in essay_SVO for subj in sent if subj]
	words = [w for s in essay_words for w in s]
	return len(subjs) / (len(words)+1)