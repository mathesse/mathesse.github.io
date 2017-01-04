---
layout: post
title: Archiver and Unarchiver used on Mac
category: tech
tags: self-study
keywords: 有趣
description: 

---
 
## <font color="#fcbe32">Problem</font>

- Tragedy if you use a Mac while your colleagues are using Windows!

- If you extract .zip compressed on Windows with Chinese/Japanese/Korean characters on Mac, one probable problem is that you might face error codes in file names, which makes it impossible to run sometimes.

- If a Mac user transfer compressed file to Windows person... same problem:(

## <font color="#fcbe32">Reason</font>

- Mac OSX use UTF-8, but there is no unicode announcing PKZIP changes in file header (文件头，区别于C中的头文件). 

- Windows use ANSI.

## <font color="#fcbe32">Apps recommended for Mac Users</font>

### <font color="#fcbe32">1. The Unarchiver - use it to extract on Mac</font>

- Supported file formats include Zip, Tar-GZip, Tar-BZip2, RAR, 7-zip, LhA, StuffIt and many other old and obscure formats. 
	
- con: cannot preview contents

- The Archive Browser is expanded version of The Unarchiver.

- [The Unarchiver - download page of all versions](http://wakaba.c3.cx/releases/TheUnarchiver/ "http://wakaba.c3.cx/releases/TheUnarchiver/")

### <font color="#fcbe32">2. Keka - use it to compress on Mac</font>

- The main compression core is p7zip (7-zip port). 
	- Compression formats supported:
7z, Zip, Tar, Gzip, Bzip2, DMG, ISO. 
	- Extraction formats supported: RAR, 7z, Lzma, xz, Zip, Tar, Gzip, Bzip2, ISO, EXE, CAB, PAX

- [A free download from Keka project site](http://www.kekaosx.com/en/ "http://www.kekaosx.com/en/")

- pro(or con?): unique icon!

![Keka](http://www.kekaosx.com/img/keka_icon.png "Keka Icon!")




