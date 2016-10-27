---
layout: post
title: Import and Manage Kindle Clippings to Mac OSx
category: 读书
tags: Kindle
keywords: 阅读 Kindle
description: 

---


Two ways to import and manage kindle clippings.

## <font color="#fcbe32">1. Use a simple python program </font>

```Python
import os
note_path='/Volumes/Kindle/documents/My Clippings.txt'
f=open(note_path,'r+')
digest_path='/Users/Hessiatrix/Documents/kindle-digest'
os.mkdir(digest_path)
while True:
    onenote=[]
    for i in range(0,5):
        line=f.readline()
        if not line:
            exit()
        onenote.append(line)
    book_note=open('%s%s.txt'%(digest_path,onenote[0]),'a+')
    book_note.write(onenote[3]+'\n')
    book_note.close() 
 ```
 
Source: [Kindle标注的重点和笔记可以导出吗？](https://www.zhihu.com/question/23031778# "zhihu.com")

## <font color="#fcbe32">2. KindleMate-标注笔记及生词本管理器: import clippings to local folder</font>

- Kindle Mate is a software to import clippings to local folder. 

	- download page: [Kindle Mate](http://kmate.me "download")

- Kindle Mate currently (up to 2016-10-27) has a wrapped version (winskine) for Mac.

	- pan.baidu download: [Kindle Mate for Mac (wineskin)](https://pan.baidu.com/s/1i3Hocol "pan.baidu")

<font color="red">Problem: Kindle Mate does not support Chinese characters. </font>

<font color="red">Solution: install Chinese (zh-CN/zh-TW) fonts for Wineskin. </font>

### Wineskin

- Wineskin is a tool used to make ports of Windows software to Mac OS X.  The ports are in the form of normal Mac application bundle wrappers.  It works like a wrapper around the Windows software, and you can share just the wrappers if you choose.

### Install Chinese fonts for Wineskin

#### 1. prepare Font file

- open the wrapped package->Show packages; 

![](/public/img/posts/20161027/kindle-mate-1.png)

- copy the Fonts file (.tcc) to drive_c/windows/Fonts

![](/public/img/posts/20161027/kindle-mate-6.png)
	
#### 2. open the wrapped package: Show packages -> Wineskin.app -> Advanced -> tools -> Registry Editor

![](/public/img/posts/20161027/kindle-mate-2.png)

![](/public/img/posts/20161027/kindle-mate-3.png)

#### 3. Modify MS Shell Dlg and MS Shell DLg 2

- find HKEY_LOCALE_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\FontSubstitutes

- now you will see MS Shell Dlg and MS Shell Dlg 2 at the right side.

![](/public/img/posts/20161027/kindle-mate-7.png)

- just change the value for these two items. The value matches the font name which is copied to c:\windows\fonts of Wineskin app. Careful that the font name is not the font's file name, open the font and you can see the name from the font manager. You can copy any fonts here for your own use (I dragged the fonts from Windows). In zh_CN it will be Simsun (simsun.ttc). 

#### 4. set custom commands

- set Custom Commands (Show packages -> Wineskin.app -> Advanced -> Configuration) to "export LANG=zh_CN.UTF-8"(this is for Simplified Chinese, without quotes and Case Sensitive)

#### 5. run cjkfonts
- search and run cjkfonts at Advanced -> Tools -> Winetricks. 

![](/public/img/posts/20161027/kindle-mate-4.png)

![](/public/img/posts/20161027/kindle-mate-5.png)

#### 6. Test run, and the application will launch in Chinese.

![](/public/img/posts/20161027/kindle-mate-8.png)

### Use Kindle Mate to export clippings

![](/public/img/posts/20161027/kindle-mate-9.png)

## <font color="#fcbe32">[References]</font>

1. [Kindle Mate 1.35 for Mac测试](https://www.douban.com/group/topic/89966767/ "Douban.com")

2. [Wineskin Newbie - Need help running Asian EXE](http://portingteam.com/topic/5094-wineskin-newbie-need-help-running-asian-exe/ "portingteam.com")

3. Fonts lib for Chinese

	- [](http://www.fontke.com)
	- [](http://www.touwenzi.com)
	- [](http://wiki.ubuntu.org.cn/免费中文字体)


