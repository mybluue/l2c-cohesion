import pickle
from collections import Counter
from random import randint


cilin_word2tags_path = 'resources/word2tags.pkl'

with open(cilin_word2tags_path, 'rb') as f:
    word2tags = pickle.load(f)


def get_MaxLabelWordRel(w1, w2):
    if w1 == w2:
        return 6
    res = 0
    if w1 in word2tags and w2 in word2tags and word2tags[w1] and word2tags[w2]:
        for tag1 in word2tags[w1]:
            for tag2 in word2tags[w2]:
                cur_res = 6
        
                if tag1==tag2:
                    pass
                elif tag1[0:7]==tag2[0:7]:
                    cur_res-=1
                elif tag1[0:5]==tag2[0:5]:
                    cur_res-=2
                elif tag1[0:4]==tag2[0:4]:
                    cur_res-=3
                elif tag1[0:2]==tag2[0:2]:
                    cur_res-=4
                elif tag1[0:1]==tag2[0:1]:
                    cur_res-=5
                else:
                    cur_res-=6
                res = max(cur_res, res)
        return res
    else:
        return 0


def get_SVO(words, pos, dep):
    words = [list(zip([i for i in range(1, len(words[i]) + 1)], words[i])) for i in range(len(words))]
    essaySVO=[]
    for i in range(len(words)):
        id2word = {x[0]: x[1] for x in words[i]}
        id2word[0] = '0'
        id2pos={j+1:pos[i][j] for j in range(len(pos[i]))}
        id2head = {x[0]: x[1] for x in dep[i]}
        id2rel = {x[0]: x[2] for x in dep[i]}
        curSVO=[]
        curPOS=[]
        sentSVO=[]
        for index in id2rel.keys():
            if id2rel[index]=='SBV':
                if curSVO:
                    sentSVO.append(curSVO+curPOS)
                curSVO=[]
                curPOS=[]
                curSVO.append(id2word[index])
                curPOS.append(id2pos[index])
                curSVO.append(id2word[id2head[index]])
                curPOS.append(id2pos[id2head[index]])

                hasObject=False
                for id in id2rel.keys():
                    if id!=index and id2head[id]==id2head[index] and id2rel[id]=='VOB':
                        hasObject=True
                        curSVO.append(id2word[id])
                        curPOS.append(id2pos[id])
                if not hasObject:
                    curSVO.append('--object')
                    curPOS.append('--pos')
                
        sentSVO.append(curSVO+curPOS)
        if sentSVO:
            essaySVO.append(sentSVO)
    return essaySVO


getWordRel = get_MaxLabelWordRel