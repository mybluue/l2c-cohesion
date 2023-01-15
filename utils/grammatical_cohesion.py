prp_li=['我', '我们', '本人', '鄙人', '敝人', '私', '老子', '老娘', '本姑娘', '本小姐', '本少爷', '人家', '本席', '咱', '咱们', '俺', '俺们', '恁爸', '恁祖妈', '人哋', '我哋', '阿拉', '偶', '禾', '小弟', '小妹', '姊', '哥', '洒家', '某家', '予一人', '本王', '寡小君', '小童', '梓童', '本座', '本单位', '本官', '本将', '末将', '下官', '卑职', '在下', '仆', '区区', '某', '某人', '某某', '某甲', '小弟', '愚兄', '小妹', '愚姊', '愚姐','小生', '晚生', '后学', '末学', '不才', '老夫', '老朽', '老叟', '老身', '免贵', '老奴', '老仆', '小女子', '奴家', '奴', '儿', '卬', '姎', '贫道', '小道', '草民', '小人', '小可', '小的', '哀家', '本宫', '你', '你们', '妳', '妳们', '祢', '子', '乃', '他', '他们', '她', '她们', '它', '它们', '祂', '伊', '渠', '佢', '怹', '贵公司', '贵社', '贵府', '贵院', '贵局', '贵处', '贵校', '贵会']

def get_grammatical_cohesion_index(words,pos):
    words_cnt, nouns_cnt, pronouns_count, prp_count, cnj_cnt = 0, 0, 0, 0, 0
    prp_word, pronoun_word, cnj_word = [], [], []
    for i in range(len(words)):
        for j in range(len(words[i])):
            # 排除标点符号
            if pos[i][j]!='wp':
                words_cnt+=1
                if pos[i][j]=='n': nouns_cnt+=1
                if pos[i][j]=='r':
                    pronouns_count+=1
                    pronoun_word.append(words[i][j])
                    if words[i][j] in prp_li:
                        prp_count+=1
                        prp_word.append(words[i][j])
                if pos[i][j]=='c':
                    cnj_cnt+=1
                    cnj_word.append(words[i][j])

    pron_density = pronouns_count / (words_cnt + 1)
    PN_ratio = pronouns_count / (nouns_cnt + 1)    
    PPN_ratio = prp_count / (nouns_cnt + 1)   
    PPP_ratio = prp_count / (pronouns_count + 1)

    PP_TTR = len(list(set(prp_word))) / (len(prp_word) + 1)
    P_TTR = len(list(set(pronoun_word))) / (len(pronoun_word) + 1)
    PSent_ratio = pronouns_count / (len(words)+1)
    PPSent_ratio = prp_count / (len(words)+1)

    conj_density = cnj_cnt / (words_cnt + 1)
    CN_ratio = cnj_cnt / (nouns_cnt+1)
    CSent_ratio = cnj_cnt / (len(words)+1)
    C_TTR = len(list(set(cnj_word))) / (len(cnj_word) + 1)

    return pron_density, PN_ratio, PPN_ratio, PPP_ratio, PP_TTR, P_TTR, PSent_ratio, PPSent_ratio, conj_density, CN_ratio, CSent_ratio, C_TTR
