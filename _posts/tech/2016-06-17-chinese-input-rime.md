---
layout: post
title: Rime Input Method Deployment on Mac
category: TECH
tags: rime input
keywords: TECH
description: 

---
# <font color="#ff5f2e"><center>鼠鬚管，爲物雖微仍需學習</center></font>

## 奉送原甫侍讀出守永興

嘉祐五年歐陽修

> 酌君以荊州魚枕之蕉
> 贈君以宣城鼠鬚之管
> 酒如長虹飲滄海
> 筆若駿馬馳平坂
> 受君尚少力方豪
> 嗟我久衰歡漸鮮
> 文章驚世知名早
> 意氣論交相得晩
> 魚枕蕉
> 一舉十分當覆盞
> 鼠鬚管
> 爲物雖微情不淺
> 新詩醉墨時一揮
> 別後寄我無辭遠

主要目标：解决alfred不能中文输入的问题。

其他目标：调整外观和扩充词库。

# <font color="#ff5f2e">1. 准备</font>

~~~
cd ~/Library/Rime
~~~
我使用的是简体字。

顺便改一下default：
- default.yaml

comment  out scheme_list: cangjie5
虽然其他的也用不着，但先留着。

# <font color="#ff5f2e">2. 外观和Alfred</font>
- squirrel.yaml 
  修改style
~~~
style:
  color_scheme: lost_temple # native
  horizontal: false
  inline_preedit: false
  corner_radius: 10
  border_height: 0
  border_width: 0
  line_spacing: 1
  spacing: 5  # space between preedit and candidates in non-inline mode
  #candidate_format: '%c. %@ '
  font_face: 'Hiragino Sans GB W3' # 'Lantinghei TC Extralight' # 'Lucida Grande'  # supporting soft cursor '›'
  font_point: 21
  #label_font_face: 'Myriad Pro Light' # 'STHeitiTC-Medium'
  #label_font_point: 17 # 18
~~~
用lost_temple是因为生日回家，在国泰看到的一副岳麓书院。

- app_options:
~~~
app_options:
  #com.alfredapp.Alfred:
  #  ascii_mode: true
  #com.runningwithcrayons.Alfred-2:
  #  ascii_mode: true
  com.blacktree.Quicksilver:
    ascii_mode: true
  com.apple.Terminal:
    ascii_mode: true
    no_inline: true
  com.googlecode.iterm2:
    ascii_mode: true
  org.vim.MacVim:
    ascii_mode: true
    no_inline: true
  #com.apple.dt.Xcode:
  #  ascii_mode: true
~~~

# <font color="#ff5f2e">3. 扩充词库</font>

## 3.1  an extended dict for luna pinyin 

### 3.1.1 基础版
https://bintray.com/rime-aca/dictionaries/luna_pinyin.dict

下载后解压，直接拷贝到目标文件夹即可。注意所使用的mac的中文编码。建议还是用pc端处理词库。

修改luna_pinyin.custom.yaml 为luna_pinyin_simp.custom.yaml



### 3.1.2 升级版
见参考文献4文末的dropbox链接，*推荐*，直接导入即可。

## 3.2 搜狗词库

### 3.2.1 获得 sogou-0.txt
http://pan.baidu.com/share/link?shareid=141610&uk=2902507575&third=0

### 3.2.2 深蓝词库转换，获得sogou-1.txt
https://code.google.com/archive/p/imewlconverter/downloads

注意这是PC端的，所以……

截止到06.17.2016，版本是2.0。

输入为搜狗词库，输出为 Rime。

也可以简繁转换，目前没必要，就不处理了。

### 3.2.3. 制作词库文件

以上两个 txt 复制到~/Library/Rime/

- 将“sogou-0.txt”重命名为：“luna_pinyin.sogou0.dict.yaml”。

并在该文件最上方增加文件信息：

~~~
#  luna_pinyin.sogou.dict.yaml

    ---
    name: luna_pinyin.sogou    #这就是你自定义的词库的名字:sogou，后面还要用到
    version: "2015.XX.XX"        #版本时间，最好填当前时间，要版本控制的意识
    sort: by_weight
    use_preset_vocabulary: true
    ...
#下面就是之前转换好的词库，如：

    釣魚島    diao yu dao    1
    黑瞎子島    hei xia zi dao    1
    南沙羣島    nan sha qun dao    1
    鴻庥島    hong xiu dao    1
    南威島    nan wei dao    1
    景宏島    jing hong dao    1
~~~

- 将“sogou-1.txt”重命名为：“luna_pinyin.sogou1.dict.yaml”

~~~
#  luna_pinyin.sogou.dict.yaml

    ---
    name: luna_pinyin.yourname    #这就是你自定义的词库的名字:yourname，后面还要用到
    version: "2015.XX.XX"        #版本时间，最好填当前时间，要版本控制的意识
    sort: by_weight
    use_preset_vocabulary: true
    ...
~~~

## <font color="#ff5f2e">4. 使词库生效</font>
### 4.1 修改yaml
修改luna_pinyin.extended.dict.yaml的import_tables

~~~
#此處爲明月拼音擴充詞庫（基本）默認鏈接載入的詞庫，有朙月拼音官方詞庫、明月拼音擴充詞庫（漢語大詞典）、明月拼音擴充詞庫（詩詞）、明月拼音擴充詞庫（含西文的詞彙）。如果不需要加載某个詞庫請將其用「#」註釋掉。
#雙拼不支持 luna_pinyin.cn_en 詞庫，請用戶手動禁用。
    import_tables:
        - luna_pinyin
        - luna_pinyin.hanyu
        - luna_pinyin.poetry
        - luna_pinyin.cn_en
        - luna_pinyin.sogou
        - luna_pinyin.yourname
    ...
~~~

## <font color="#ff5f2e">5. 重新部署Deploy!!!</font>

---

## BONUS：词库资料

- 码农场的爬虫

http://www.hankcs.com/nlp/corpus/tens-of-millions-of-giant-chinese-word-library-share.html

- webdict的爬虫

https://github.com/ling0322/webdict

---

##  *附加任务1：建立通讯录词库

luna_pinyin.mycontact.dict.yaml

## *附加任务2：同步词库

- installation.yaml

~~~
sync_dir: “/Users/username/Dropbox/sync/Rime”
~~~

~~~
installation_id: "yourname"    #自定义个人文件夹的名字
~~~

---

# <font color="#ff5f2e">References</font>

1. https://github.com/rime/home/wiki/RimeWithSchemata
2. http://www.dreamxu.com/install-config-squirrel/
3. http://www.jianshu.com/p/cffc0ea094a7
4. https://medium.com/@scomper/%E9%BC%A0%E9%A0%88%E7%AE%A1-%E7%9A%84%E8%B0%83%E6%95%99%E7%AC%94%E8%AE%B0-3fdeb0e78814#.xbbdjkzbb