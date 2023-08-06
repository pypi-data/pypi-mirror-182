"""
WheelDecide \_ 转盘决定命运
==================================

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

   w.setTitle("Wheel") <- 一个str类型，代表窗口的标题

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
   
   #setTitle值默认为"Wheel"

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
   
"""

# importations
import tkinter
import time
import threading

# intializations
titv = 1
bsize = 50
uncolor = "white"
secolor = "red"
mwidth = 300
mheight = 300
roottitle = "wheel"

# class
class wheel():
    # thefunctiontoUse↓
    def setupwheel(self, list: list):
        self.root = tkinter.Tk()
        self.root.title(roottitle)
        self.root.minsize(mwidth, mheight)
        self.isloop = False
        self.newloop = False
        self.btn_start = tkinter.Button(
            self.root, text='start', command=self.newtaskT)
        self.btn_start.place(x=bsize+40, y=1.5*bsize+50,
                             width=bsize, height=bsize)

        self.btn_stop = tkinter.Button(
            self.root, text='stop', command=self.newtaskF)
        self.btn_stop.place(x=2*bsize+60, y=1.5*bsize +
                            50, width=bsize, height=bsize)

        self.btn1 = tkinter.Button(self.root, text=list[0], bg=uncolor)
        self.btn1.place(x=20, y=20, width=bsize, height=bsize)

        self.btn2 = tkinter.Button(self.root, text=list[1], bg=uncolor)
        self.btn2.place(x=bsize+40, y=20, width=bsize, height=bsize)

        self.btn3 = tkinter.Button(self.root, text=list[2], bg=uncolor)
        self.btn3.place(x=2*bsize+60, y=20, width=bsize, height=bsize)

        self.btn4 = tkinter.Button(self.root, text=list[3], bg=uncolor)
        self.btn4.place(x=3*bsize+80, y=20, width=bsize, height=bsize)

        self.btn5 = tkinter.Button(self.root, text=list[4], bg=uncolor)
        self.btn5.place(x=3*bsize+80, y=bsize+40, width=bsize, height=bsize)

        self.btn6 = tkinter.Button(self.root, text=list[5], bg=uncolor)
        self.btn6.place(x=3*bsize+80, y=2*bsize+60, width=bsize, height=bsize)

        self.btn7 = tkinter.Button(self.root, text=list[6], bg=uncolor)
        self.btn7.place(x=3*bsize+80, y=3*bsize+80, width=bsize, height=bsize)

        self.btn8 = tkinter.Button(self.root, text=list[7], bg=uncolor)
        self.btn8.place(x=2*bsize+60, y=3*bsize+80, width=bsize, height=bsize)

        self.btn9 = tkinter.Button(self.root, text=list[8], bg=uncolor)
        self.btn9.place(x=bsize+40, y=3*bsize+80, width=bsize, height=bsize)

        self.btn10 = tkinter.Button(self.root, text=list[9], bg=uncolor)
        self.btn10.place(x=20, y=3*bsize+80, width=bsize, height=bsize)

        self.btn11 = tkinter.Button(self.root, text=list[10], bg=uncolor)
        self.btn11.place(x=20, y=2*bsize+60, width=bsize, height=bsize)

        self.btn12 = tkinter.Button(self.root, text=list[11], bg=uncolor)
        self.btn12.place(x=20, y=bsize+40, width=bsize, height=bsize)

        self.turns = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6,
                      self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12]
        self.root.mainloop()

    def setTimeInterval(self, interval: int):
        global titv
        titv = interval

    def setUnselectedBgcolor(self, color: str):
        global uncolor
        uncolor = color

    def setSelectedBgcolor(self, color: str):
        global secolor
        secolor = color

    def setMinsize(self, width: int, height: int):
        global mwidth, mheight
        mwidth = width
        mheight = height

    def setBtnSize(self, size: int):
        global bsize
        bsize = size

    def setTitle(self,title: str):
        global roottitle
        roottitle = title
    
    # thefunctiontoUse↑

    def rounds(self):
        if self.isloop == True:
            return
        i = 0
        while True:
            if self.newloop == True:
                self.newloop = False
                return
            time.sleep(titv)
            for x in self.turns:
                x['bg'] = uncolor
            self.turns[i]['bg'] = secolor
            i += 1
            if i >= len(self.turns):
                i = 0

    def newtaskT(self):
        t = threading.Thread(target=self.rounds)
        t.start()
        self.isloop = True
        self.newloop = False

    def newtaskF(self):
        self.isloop = False
        self.newloop = True
