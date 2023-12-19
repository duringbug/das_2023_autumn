'''
Description: 
Author: 唐健峰
Date: 2023-12-14 11:07:06
LastEditors: ${author}
LastEditTime: 2023-12-19 18:31:54
'''
import redis
import jieba
from gensim.models import Word2Vec
import numpy as np


def get_vectors(vec):
    # 创建Redis连接
    redis_host = '127.0.0.1'  # 你的Redis服务器主机地址
    redis_port = 6379         # 你的Redis服务器端口号
    # redis_password = 'Tjf04712'     # 如果有密码，请提供密码
    redis_db = 6              # 你要连接的数据库编号

    # 用于训练Word2Vec模型的文本数据
    title_data = []
    text_data = []
    herf_data = []

    # 使用StrictRedis类创建连接，指定数据库编号
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

    # 获取所有以"news:"为前缀的键，这里假设链接（link）是唯一标识符
    news_keys = r.keys("news:*")

    # 遍历所有键，获取对应的数据
    for key in news_keys:
        # 使用hgetall获取哈希数据
        news_data = r.hgetall(key)
        
        # 输出数据
        # print("News Data:")
        # print(f"Key: {key}")
        # print(f"Title: {news_data['title']}")
        # print(f"Link: {news_data['link']}")
        title_data.append(list(jieba.cut(news_data['title'])))
        text_data.append(list(jieba.cut(news_data['dec'])))
        herf_data.append(news_data['link'])
        # print(f"Image: {news_data['img']}")
        # print(f"Time: {news_data['time']}")
        # print(f"Author: {news_data['auth']}")
        # print("\n")


    # 训练Word2Vec模型
    model = Word2Vec(sentences=text_data + title_data, vector_size=vec, window=5, min_count=1, workers=4)

    # 使用Word2Vec模型将词语列表转换为数字类型的数据
    def word_list_to_vectors(word_list, model):
        vectors = [model.wv[word] for word in word_list if word in model.wv]
        if vectors:
            return vectors  # 直接返回词向量列表
        else:
            return [np.zeros(model.vector_size)]  # 如果词语列表为空，返回包含零向量的列表


    # 将title_data和text_data中的词语列表转换为数字类型的数据
    title_vectors = [word_list_to_vectors(title, model) for title in title_data]
    text_vectors = [word_list_to_vectors(text, model) for text in text_data]
    return title_vectors,text_vectors,title_data,text_data,herf_data,model