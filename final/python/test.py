
'''
Description: 
Author: 唐健峰
Date: 2023-12-19 13:22:23
LastEditors: ${author}
LastEditTime: 2024-01-18 12:53:32
'''

from redis_util.index import get_vectors
from data_util.tf_idf import *
import numpy as np


WORD_DIMENSION = 10

title_vectors, text_vectors, title, text ,herf_data,model= get_vectors(WORD_DIMENSION)


def test_tf_idf():
    # 计算TF-IDF
    tfidf_documents = calculate_tfidf(text)

    conn = sqlite3.connect('/Volumes/TJF_YINGPAN/class/DaSE导论/dase-2023-autumn/final/python/data/data.db')
    cursor = conn.cursor()

    # 创建表（如果不存在）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS text_idf (
            herf TEXT PRIMARY KEY,
            count REAL
        )
    ''')

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
        cursor.execute('INSERT OR REPLACE INTO text_idf (herf, count) VALUES (?, ?)', (herf_data[i], top3_tfidf_words))
        print()
    # 提交更改并关闭连接
    conn.commit()
    conn.close()


def test_print():
    import sqlite3
    from sklearn.feature_extraction.text import TfidfVectorizer

    # 将二维列表转换为字符串列表
    documents = [' '.join(doc) for doc in text]

    # 创建TF-IDF向量化器
    vectorizer = TfidfVectorizer()

    # 计算TF-IDF矩阵
    tfidf_matrix = vectorizer.fit_transform(documents)

    # 获取特征词
    features = vectorizer.get_feature_names_out()

    # 计算每个词的TF-IDF值并排序
    word_tfidf = list(zip(features, tfidf_matrix.sum(axis=0).A1))
    word_tfidf.sort(key=lambda x: x[1], reverse=True)

    # 打印前n个热度词
    n = 50
    top_n_words = word_tfidf[:n]

    conn = sqlite3.connect('/Volumes/TJF_YINGPAN/class/DaSE导论/dase-2023-autumn/final/python/data/data.db')
    cursor = conn.cursor()
    # 创建表（如果不存在）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS word_tfidf (
            word TEXT PRIMARY KEY,
            count REAL
        )
    ''')

    for word, tfidf in top_n_words:
        cursor.execute('INSERT OR REPLACE INTO word_tfidf (word, count) VALUES (?, ?)', (word, tfidf))
        print(f"{word}: {tfidf}")
    # 提交更改并关闭连接
    conn.commit()
    conn.close()

test_tf_idf()

test_print()