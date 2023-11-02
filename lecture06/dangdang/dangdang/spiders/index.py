'''
Description: 
Author: 唐健峰
Date: 2023-10-31 19:10:43
LastEditors: ${author}
LastEditTime: 2023-11-02 10:05:55
'''
import scrapy
import os
import sqlite3


class IndexSpider(scrapy.Spider):
    name = "index"
    allowed_domains = ["search.dangdang.com"]
    start_urls = [
        f"https://search.dangdang.com/?key=计算机类书籍&act=input&page_index={i}"
        for i in range(1, 21)
    ]

    def __init__(self, *args, **kwargs):
        super(IndexSpider, self).__init__(*args, **kwargs)
        # Define an absolute path for the database file
        db_path = os.path.join(os.getcwd(), 'mydata.db')
        # Establish a connection to the SQLite database
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

        # Create a table to store the data if it doesn't exist
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                price TEXT
            )
        ''')

    def close(self, reason):
        # Close the database connection when the Spider is closed
        self.conn.close()

    def parse(self, response):
        # Using CSS selector to extract <a> tag's title attribute
        titles = response.css(
            'div#search_nature_rg ul.bigimg li a.pic::attr(title)').getall()
        prices = response.css(
            'div#search_nature_rg ul.bigimg li p.price span.search_now_price::text').getall()

        # Insert the titles into the SQLite database
        for title, price in zip(titles, prices):
            self.c.execute(
                "INSERT INTO books (title, price) VALUES (?, ?)", (title, price))
            self.conn.commit()

        # Yield the titles as Scrapy items
        for title in titles:
            yield {'title': title, 'price': price}
