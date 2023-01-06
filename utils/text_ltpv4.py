'''
implement the ltp 4.1 text processing module
''' 

def text_process_ltp_v4(text, ltp_model, batch_size=32):

    '''
    text preprocessing with ltp v4.1
    '''

    text_dict = {}
    paras = text.split('\n') # para split

    # para split
    all_sents = []
    for para in paras:
        para = para.strip()
        if len(para) < 3:
            continue
        sents = ltp_model.sent_split([para])
        sents = [sent for sent in sents if len(sent) >= 3] # sent length limit
        all_sents.extend(sents)
 
    ltp_res = {
        'words': [],
        'pos': [],
        'dep': []
    }
            
    # parallel processing
    sent_id = 0
    for i in range(0, len(all_sents), batch_size):
        batch_sents = all_sents[i: i+batch_size]
        wordlists, hidden = ltp_model.seg(batch_sents)
        poslists = ltp_model.pos(hidden)
        deplists = ltp_model.dep(hidden)
        
        ltp_res['words'].extend(wordlists)
        ltp_res['pos'].extend(poslists)
        ltp_res['dep'].extend(deplists)  

        for j, sent in enumerate(batch_sents):
            wl, pl, dl = wordlists[j], poslists[j], deplists[j]
            wplist = []
            for w, p in zip(wl, pl):
                wplist.append(w + '/' + p)

            worddict = {}
            for k, arc in enumerate(dl):
                token, pos = wl[k], pl[k]
                parent = arc[1] - 1  # 原为从1开始编号，现从0开始编号
                relate = arc[2]
                worddict[k] = {'cont': token, 'pos': pos, 'parent': parent, 'relate': relate}

            text_dict[sent_id] = {'wordlist': wl, 'wplist': wplist, 'worddict': worddict, 'sent': sent}
            sent_id += 1

    return text_dict, ltp_res