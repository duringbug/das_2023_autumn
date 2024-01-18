'''
Description: 
Author: 唐健峰
Date: 2023-12-14 11:06:48
LastEditors: ${author}
LastEditTime: 2024-01-18 14:30:53
'''
from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) 

@app.route('/api/data', methods=['GET'])
def get_data():
    # 创建或连接到 SQLite 数据库文件
    conn = sqlite3.connect('/Volumes/TJF_YINGPAN/class/DaSE导论/dase-2023-autumn/final/python/data/data.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 执行查询语句
    query = 'SELECT * FROM word_tfidf'
    cursor.execute(query)

    # 获取查询结果
    rows = cursor.fetchall()

    # 处理查询结果
    data_list = []
    for row in rows:
        data_dict = {
            'word': row[0],  # 替换为实际列名
            'tfidf': row[1],  # 替换为实际列名
            # 添加其他列...
        }
        data_list.append(data_dict)

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()

    # 将查询结果转换为 JSON 格式并返回
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)
