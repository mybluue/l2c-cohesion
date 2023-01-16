from .lexical_cohesion import *
from .grammatical_cohesion import *
from .topical_cohesion import *
import pandas as pd
import pickle
from tqdm import tqdm


def get_cohesion_index(essay, essay_pos, essay_svo, essay_only_noun):
    local_lexical_cohesion, global_lexical_coheison, local_noun_cohesion, global_noun_cohesion = get_lgcohesion(essay, essay_only_noun)
    central_sent_num, central_sent_ratio = get_central_sent_cohesion(essay)
    pron_density, PN_ratio, PPN_ratio, PPP_ratio, PP_TTR, P_TTR, P_NPS, PP_NPS, conj_density, CN_ratio, C_NPS, C_TTR = get_grammatical_cohesion_index(essay, essay_pos)
    subj_density = get_subj_density(essay_svo, essay)
    subj_TTR, subj_n_TTR, subj_p_RATIO, subj_n_RATIO = get_SO_TTR_RATIO_cohesion(essay_svo)
    local_subj_cohesion, global_subj_cohesion = get_SO_lgcohesion(essay_svo)
    subj_sc_num, subj_sc_density = get_agregation_cohesion(essay_svo)
    
    essay_index = locals()
    essay_index = {k: v for k, v in essay_index.items() if k[:5]!='essay'}
    return essay_index


def ltp2index(ltp_file, svo_file, index_file):
    with open(ltp_file,'rb') as f:
        id2ltp=pickle.load(f)
    with open(svo_file,'rb') as f:
        id2ltpsvo = pickle.load(f)

    id2index = {}
    i = 1
    for e_id in tqdm(id2ltp.keys()):
        essay, essay_pos, essay_svo = id2ltp[e_id]['words'], id2ltp[e_id]['pos'], id2ltpsvo[e_id]
        essay_only_noun = [[essay[i][j] for j in range(len(essay[i])) if essay_pos[i][j]=='n'] for i in range(len(essay))]
        id2index[e_id] = get_cohesion_index(essay, essay_pos, essay_svo, essay_only_noun)	
        i += 1

    df_li = list()
    for e_id,e_index in id2index.items():
        cur_li = [e_id] + list(e_index.values())
        df_li.append(cur_li)
    random_id = list(id2ltp.keys())[0]
    head = ['id'] + list(id2index[random_id].keys())
    df = pd.DataFrame(df_li, columns=head)
    df.to_excel(index_file, index=False)