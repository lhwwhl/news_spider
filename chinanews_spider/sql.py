# -*- coding: utf-8 -*-

# Define your sql

import pymysql

db = pymysql.connect("localhost", "root", "qwerlhw9485@", "news", use_unicode=True, charset="utf8" )
cur = db.cursor()

class Sql:
    @classmethod
    def insert_news(cls, category, content):
        #sql = ("INSERT INTO table_name" 
		#	   "(category, content)"
		#	   "VALUES (%(category)s, %(content)s)")
        sql = "INSERT INTO %s (content) VALUES ('%s');" % (category, content)
        print(sql)
        #value = {
		#		"category"  :category,
		#		"content"   :content
		#		}
        #print(value)
        try:
            cur.execute(sql)
            #cur.execute(sql, value)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

#if __name__ == '__main__':
#    test = Sql()
#    test.insert_news("yl", "dddorlddd")
