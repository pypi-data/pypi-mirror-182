WheelDecide \_ 转盘决定命运
==================================

|License| |Pypi| |Author| |Github|

安装方法
--------

通过 pip 安装

::

   pip install WheelDecide

更新

::

   pip install WheelDecide --upgrade

使用方法
--------

导入

::

   import WheelDecide

使用

::

   w = WheelDecide.wheel()

   w.setMinsize(300,300) <- 两个int类型，代表窗口的大小（长和宽）

   w.setBtnSize(50) <- 一个int类型，代表元素大小（边长）

   w.setTimeInterval(1) <- 一个int类型，代表时间间隔

   w.setUnselectedBgcolor("white") <- 一个str类型，代表未选中的元素背景颜色

   w.setSelectedBgcolor("red") <- 一个str类型，代表已选中的元素背景颜色

   w.setupwheel(["1","2","3","4","a","b","c","d","!","?","#","%"]) <- 十二个str类型组成的list，代表转盘的元素

**!注意事项!**

*导入*

::

   import WheelDecide #√

   import wheeldecide #×

*使用*

::

   #setMinsize值默认为300,300

   #setBtnSize值默认为50

   #setTimeInterval值默认为1

   #setUnselectedBgcolor值默认为"white"

   #setSelectedBgcolor值默认为"red"

   ### setupwheel永远是最后一条指令！！！ ###
   
关于作者
--------

Author

*Jason4zh*

Email

*13640817984@163.com*

Package

*https://pypi.org/project/WheelDecide/*

Github

*https://github.com/Jason4zh/WheelDecide/*

::

   print("Thank you for using WheelDecide!")



本次更新修改v1.1.2
------------------

1. 修改了rst文件Pypi附图

2. 修改了rst文件文字内容

3. 添加了 *__init__.py* 的库介绍

.. |License| image:: https://img.shields.io/badge/License-BSD-yellow
   :target: https://github.com/Jason4zh/WheelDecide/blob/main/LICENSE
.. |Pypi| image:: https://img.shields.io/badge/Pypi-v1.1-blue
   :target: https://pypi.org/project/WheelDecide
.. |Author| image:: https://img.shields.io/badge/Author-Jason4zh-green
   :target: https://pypi.org/user/Jason4zh
.. |Github| image:: https://img.shields.io/badge/Github-Jason4zh-red
   :target: https://github.com/Jason4zh/WheelDecide
