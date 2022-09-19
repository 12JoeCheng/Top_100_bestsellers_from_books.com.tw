# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class DemoPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('demo_db')
        self.curr = self.conn.cursor()
    

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS top_100_from_books""")
        self.curr.execute("""CREATE TABLE top_100_from_books(
            Ranking INTEGER PRIMARY KEY  AUTOINCREMENT,
            book_name VARCHAR(255),
            author VARCHAR(255),
            NTD_price INTEGER,
            link TEXT
            )""")
    

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        self.curr.execute("""INSERT INTO top_100_from_books (book_name, author, NTD_price, link) VALUES (?,?,?,?)""",(
            item['name'],
            item['author'],
            item['price'],
            item['link']
        ))

        self.conn.commit()
    
