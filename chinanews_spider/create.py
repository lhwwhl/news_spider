# -*- coding: utf-8 -*-

import pymysql
db = pymysql.connect("localhost","root","qwerlhw9485@","news" )
cur = db.cursor()
ctgys = ['ty', 'yl', 'cj', 'mil', 'auto', 'gj', 'it', 'sh']
for ctgy in ctgys:
    sql = "DROP TABLE IF EXISTS %s;" % ctgy
    #print(sql)
    cur.execute(sql)
    sql = "CREATE TABLE %s (`id` bigint(8) NOT NULL AUTO_INCREMENT, `content` varchar(255) NOT NULL UNIQUE, PRIMARY KEY (`id`));" % ctgy
    #print(sql)
    cur.execute(sql)
db.close()
#sql = """ CREATE TABLE `yl` (
#          `id` int(11) NOT NULL AUTO_INCREMENT,
#          `category` varchar(255) NOT NULL,
#          `content` varchar(255) NOT NULL UNIQUE,
#	      PRIMARY KEY (`id`)
#		  );"""

