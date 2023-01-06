from .knowledge import getWordRel


def get_SentCo(sent1, sent2):
    sentco = 0
    for w1 in sent1:
        for w2 in sent2:
            sentco += getWordRel(w1, w2)
    return sentco


def get_lgcohesion(essay, essay_only_noun):
    sent_count = len(essay)
    local_lexical_cohesion = 0
    global_lexical_coheison = 0
    local_noun_cohesion = 0
    global_noun_cohesion = 0

    for i in range(0, sent_count-1):
        for j in range(i+1, sent_count):
            if j==i+1:
                local_lexical_cohesion += get_SentCo(essay[i], essay[j])
                local_noun_cohesion += get_SentCo(essay_only_noun[i], essay_only_noun[j])
            global_lexical_coheison += get_SentCo(essay[i], essay[j])
            global_noun_cohesion += get_SentCo(essay_only_noun[i], essay_only_noun[j])

    local_lexical_cohesion /= sent_count + 1
    global_lexical_coheison /= (sent_count - 1) * sent_count / 2 + 1
    local_noun_cohesion /= sent_count + 1
    global_noun_cohesion /= (sent_count - 1) * sent_count / 2 + 1
    return local_lexical_cohesion, global_lexical_coheison, local_noun_cohesion, global_noun_cohesion


def get_central_sent_cohesion(essay):
	sent_count = len(essay)     
	sentco_sum = 0      
	none_zero_sent_cnt = 0      
	central_sent_count = 0      
	for i in range(sent_count):
		sentco_sum = 0
		none_zero_sent_cnt = 0
		for j in range(sent_count):
			if j != i and get_SentCo(essay[i], essay[j]) > 0:
				sentco_sum += get_SentCo(essay[i], essay[j])
				none_zero_sent_cnt += 1
		if none_zero_sent_cnt and sentco_sum // none_zero_sent_cnt > 80:
			central_sent_count += 1
	central_sent_ratio = central_sent_count / (sent_count + 1)
	return central_sent_count, central_sent_ratio