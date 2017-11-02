# -*- coding: utf-8 -*-

import pymysql
db = pymysql.connect("localhost","root","qwerlhw9485@","news" )
cur = db.cursor()

#cur.execute("DROP TABLE IF EXISTS news")
sql = """ CREATE TABLE `yl` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `category` varchar(255) NOT NULL,
          `content` varchar(255) NOT NULL UNIQUE,
	      PRIMARY KEY (`id`)
		  );"""
	      #) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;"""
cur.execute(sql)
db.close()
