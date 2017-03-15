#!/usr/bin/env python
# encoding=utf-8

# *----------------------------*
# Title: cbdb-harvard-person-in-dyn.py
# by Shanshan S.(hessiatrix@gmail.com), Mar 14, 2017
# *----------------------------*

import sys
from os import path
import sqlite3

conn = sqlite3.connect(r"/Users/hessiatrix/Desktop/cbdb-harvard/cbdb_sqlite.db")
cursor = conn.cursor()

# 从表A根据年份选出宋代期间的人物，得到id和姓名；根据id从表B得出地理信息；根据c_add_id从表C得到xy座标
# Duration of North Song dynasty: 960-1126;South Song: 1127-1279 (靖难1127.03.20)
cursor.execute('select A.c_personid,A.c_name, A.c_name_chn,B.c_addr_type,B.c_addr_id,C.x_coord,C.y_coord from BIOG_MAIN A, BIOG_ADDR_DATA B, ADDR_XY C where A.c_personid = B.c_personid and B.c_addr_id = C.c_addr_id and A.c_birthyear >= ? and A.c_deathyear <= ?',(960,1279))
person_info = cursor.fetchall()

with open('song-person-xy-event.txt','w') as output:
	output.write("c_personid,c_name,c_name_chn,c_addr_type,c_addr_id,x_coord,y_coord\n")
	for row in person_info:
		print row
		output.write("%i,%s,%s,%i,%i,%f,%f\n" % (row[0],row[1].encode('utf-8'),row[2].encode('utf-8'),row[3],row[4],row[5],row[6] ))
output.close()


# FILE END
conn.close()