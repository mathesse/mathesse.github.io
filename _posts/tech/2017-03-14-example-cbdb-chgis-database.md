---
layout: post
title: Location Distribution of Civil's Basic Affiliation and Moved-to Destinations in Song Dynasty of China (960-1279)
category: TECH
tags: python sql gis
keywords: TECH
description:

---

# <font color="#ff5f2e"><center>Location Distribution of Civil's Basic Affiliation and Moved-to Destinations in Song Dynasty of China (960-1279)</center></font>



## — A Simple Study Case Combing **China Biographical Database** with **China Historical GIS Database** Using **Python**, **DB Browser for SQLite** and **Quantum GIS**



### Databases

- [China Biographical Database (CBDB)]( http://projects.iq.harvard.edu/cbdb):a freely accessible relational database with biographical information about approximately **360,000 individuals as of April 2015**, primarily from the 7th through 19th centuries.
- [China Historical GIS Database (CHGIS)]( https://www.fas.harvard.edu/~chgis/data/):was launched in January 2001 to establish a database of populated places and historical administrative units for the period of Chinese history between *221 BCE* and *1911 CE*.  

### Software

- [DB Browser for SQLite](http://sqlitebrowser.org/): open source tool compatible with SQLite, works for OS X.
- [Quantum GIS (QGIS)](http://www.qgis.org/en/site/):Open Source Geographic Information System (GIS) licensed under the GNU
  General Public License. QGIS is an official project of the Open Source Geospatial Foundation (OSGeo).

### Procedure

#### 1. Download related Databases

- cbdb_sqlite.db from CBDB
- Time-Series Province Boundaries in POLYGONS (25 MB) from CHGIS


- 1996 DEM Background Image - All of China in RASTER (12 MB) from CHGI

#### 2. Use DB Browser for SQLite to View Database (cbdb_sqlite.db) and determine required information

- Information Needed Here

  - Civil's Birth Year and Death Year: to determine if a certain civil was born and died within duration of Song dynasty (960-1279)
  - Civil's Person ID (w/ names)
  - Civil's Address:
    - X and Y coordinates
    - Address type: such as basic affiliation (籍贯), Moved to (遷住地), Ancestral Address (祖籍), Burial Address (葬地) and etc.
    - Here I used
      - Type 1: Basic Affiliation
      - Type 2: Moved To

- Three Related Tables

  - BIOG_MAIN (Table A): **A.c_personid**,A.c_name, A.c_name_chn, A.c_birthyear, A.c_deathyear

  - BIOG_ADDR_DATA (Table B): **B.c_personid**, B.c_addr_type, **B.c_addr_id**

  - ADDR_XY (Table C): **C.c_addr_id**, C.x_coord, C.y_coord

#### 3. Write a Python Script Subtracting Civil's Information in Database

- Python Script: Sqlite3 is embedded within Python

```

#!/usr/bin/env python
# encoding=utf-8

# *----------------------------*
# Title: cbdb-harvard-person-in-dyn.py
# by hessiatrix@gmail.com, Mar 14, 2017
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
```

- Output Example

```
c_personid,c_name,c_name_chn,c_addr_type,c_addr_id,x_coord,y_coord
1,An Dun,安惇,1,100430,106.791330,30.477690
14,Chao Duanyan,晁端彥,5,100429,115.146840,35.924000
14,Chao Duanyan,晁端彥,1,100658,114.335660,34.818340
17,Chen Anshi,陳安石,1,11478,112.785721,34.840869
17,Chen Anshi,陳安石,14,11725,114.345497,36.098343
20,Chen Qizong,陳起宗,1,12696,120.733788,31.646582
……
```
#### 4. Use QGIS to Visualize
- Open New Project
- Add Delimited Text Layer: txt
- Drag shapefile *v4_time_prov_pgn_utf.shp* and geotiff file *v4_dem.tif* in to main window
- Adjust Layer Styling according to need and personal preferences: Lock and Unlock Layers
- Output
  - Zoom current window to preferred scale
  - Project-> New Print Composer
  - Follow this tutorial: [Making a Map: QGIS Tutorials and Tips](http://www.qgistutorials.com/en/docs/making_a_map.html)

![](/public/img/posts/20170314/print-cbdb-song-person.png)
