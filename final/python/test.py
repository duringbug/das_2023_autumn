'''
Description: 
Author: 唐健峰
Date: 2023-12-19 13:22:23
LastEditors: ${author}
LastEditTime: 2023-12-19 18:45:32
'''
from redis_util.index import get_vectors
from data_util.tf_idf import *
import numpy as np


WORD_DIMENSION = 10

title_vectors, text_vectors, title, text ,herf_data,model= get_vectors(WORD_DIMENSION)


def test_tf_idf():
    # 计算TF-IDF
    tfidf_documents = calculate_tfidf(text)

    # 打印每个文档的关键词及其对应的前三个最大TF-IDF值
    for i, tfidf_doc in enumerate(tfidf_documents):
        if not tfidf_doc:
            print(f"文档 {i + 1} 为空文档，跳过")
            continue

        # 获取前三个最大的关键词及其对应的TF-IDF值
        top3_tfidf_words = sorted(tfidf_doc, key=tfidf_doc.get, reverse=True)[:3]

        print(f"文档 {i + 1} 的链接为: {herf_data[i]}")
        print(f"文档 {i + 1} 的前三大TF-IDF值:")
        for word in top3_tfidf_words:
            print(f"{word}: {tfidf_doc[word]:.4f}")
        print()
