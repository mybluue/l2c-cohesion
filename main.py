# coding=utf-8
import pandas as pd
from ltp import LTP
from tqdm.auto import tqdm
from utils.text_ltpv4 import text_process_ltp_v4
from utils.knowledge import get_SVO
from utils.cohesion_index import get_cohesion_index

import glob, os, time

'''
This is an example script to process multiple texts
with the L2C Text Cohesion Tool (V2.1)
'''


def get_linguistic_cohesion_indices(input_path, 
                                      ltp_model,
                                      max_process_num=None,
                                      text_length_limit=1000,
                                      output_file=None):
    '''
    input path: str
    max_process_num: int, to limit the max number of texts to process
    text_length_limit: int, truncate for very long texts
    output_file: dict, csv_file or excel_file
    '''

    index_data = {}

    input_files = glob.glob(f'{input_path}/*.txt')

    # input files not found
    if not len(input_files):
        return index_data
    # exceed max document limit
    elif max_process_num and len(input_files) > max_process_num:
        input_files = input_files[:max_process_num]
    
    # start processing multiple documents
    for file in tqdm(input_files, desc=f"Processing Texts", total=len(input_files)):
        try:
            text_id = os.path.split(file)[-1].replace('.txt', '')
            text_cont = open(file, 'r', encoding='utf-8').read()
            # exceed text length limit
            if len(text_cont) > text_length_limit:
                text_cont = text_cont[:text_length_limit]
            # preprocessing
            _, ltp_res = text_process_ltp_v4(text_cont, ltp_model)
            essay_words, essay_pos, essay_dep = ltp_res['words'], ltp_res['pos'], ltp_res['dep']
            essay_svo = get_SVO(essay_words, essay_pos, essay_dep)
            essay_only_noun = [[essay_words[i][j] for j in range(len(essay_words[i])) if essay_pos[i][j]=='n'] for i in range(len(essay_words))]
            # get indices
            
            indices = get_cohesion_index(essay_words, essay_pos, essay_svo, essay_only_noun)
            index_data[text_id] = indices
        except:
            pass

    df_results = pd.DataFrame.from_dict(index_data, orient='index')
    df_results.index.name = 'text_ID'
    
    # return a csv file
    if output_file and output_file.endswith('.csv'):
        df_results.to_csv(output_file)

    # return a excel file
    if output_file and output_file.endswith('.xlsx'):
        df_results.to_excel(output_file)

    return index_data


if __name__ == '__main__':

    # load model
    # ltp_model = LTP(path='models/v4.0_base2_v3')
    ltp_model = LTP(path='base2') 

    # sample input
    input_path = 'data/samples'
    input_path = '/home/pengyiping/src/二语初中高'
    output_path = 'data/result.csv'

    start_time = time.time()

    index_result = get_linguistic_cohesion_indices(input_path,
                                                     ltp_model,
                                                     output_file=output_path)
    end_time = time.time()
    print(f'it takes {end_time - start_time} seconds...')
    # print(index_result)