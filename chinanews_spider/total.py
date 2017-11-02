# -*- coding: utf-8 -*-

import pymysql
db = pymysql.connect("localhost","root","qwerlhw9485@","news" )
cur = db.cursor()
ctgys = ['ty', 'yl', 'cj', 'mil', 'auto', 'gj', 'it', 'sh']
#sql = "DROP TABLE IF EXISTS Total;"
#cur.execute(sql)
#sql = "CREATE TABLE Total (`Category` varchar(255) NOT NULL , `Quantity` bigint(8) NOT NULL);"
#cur.execute(sql)

for ctgy in ctgys:
    #sql = "select id from %s where id=(SELECT MAX(id) FROM %s)" % (ctgy, ctgy)
    sql = "select max(id) from %s;" % ctgy
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        print(ctgy, row[0])
db.close()
#sql = """ CREATE TABLE `yl` (
#          `id` int(11) NOT NULL AUTO_INCREMENT,
#          `category` varchar(255) NOT NULL,
#          `content` varchar(255) NOT NULL UNIQUE,
#	      PRIMARY KEY (`id`)
#		  );"""

