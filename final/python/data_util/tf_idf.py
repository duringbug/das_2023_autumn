'''
Description: 
Author: 唐健峰
Date: 2023-12-19 18:38:26
LastEditors: ${author}
LastEditTime: 2023-12-19 18:38:42
'''

import math
from collections import Counter
from tqdm import tqdm


def calculate_tf(word_list):
    # 计算词频（TF）
    tf = Counter(word_list)
    total_words = len(word_list)
    tf_normalized = {word: count / total_words for word, count in tf.items()}
    return tf_normalized

def calculate_idf(documents, word):
    # 计算逆文档频率（IDF）
    num_documents_containing_word = sum(1 for doc in documents if word in doc)
    if num_documents_containing_word > 0:
        return math.log(len(documents) / num_documents_containing_word)
    else:
        return 0.0

def calculate_tfidf(documents):
    # 计算TF-IDF
    tfidf_documents = []
    total_documents = len(documents)

    for doc in tqdm(documents, desc="Calculating TF-IDF", unit="document", total=total_documents):
        tfidf_doc = {}
        tf = calculate_tf(doc)

        for word in doc:
            idf = calculate_idf(documents, word)
            tfidf = tf[word] * idf
            tfidf_doc[word] = tfidf

        tfidf_documents.append(tfidf_doc)

    return tfidf_documents