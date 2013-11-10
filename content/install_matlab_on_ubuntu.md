Title: Ubuntu下安装matlab过程
Date: 2007-08-15 07:35
Author: Admin
Category: 个人发展
Tags: matlab, ubuntu, 学习
Slug: install_matlab_on_ubuntu

在这里要谢谢yilingr0.spaces.live.com的内容，我把自己的安装过程写在这里，一是为了方便以后
再装的时候方便查阅，其次也是为了方便很多和我一样的菜鸟可以在这里查阅东西.
过程开始：

</p>

**更新内容：对于最新版本的2007b进行了一些更新。如果你在安装过程中，或者下载方面有任何问题，欢迎留言告诉我。**

</p>

1.  下载matlab for linux，我是用amule在veryCD上面下载的，一个for
    Mac和linux的版本，**现在最新的matlab
    2007b的链接在这里：ed2k://|file|Mathworks.Matlab.R2007b.UNIX.DVD.-TBE.iso|3594958848|58E5A99B5C4E921D0FDCC51B4F827765|/**，大家可以一起去加速了。
2.  挂载iso文件: sudo mount -t iso9660 (iso文件的路径和文件名)
    /media/cdrom -o
    loop。最新版本的下载下来是DVD的镜像文件，所以不需要再换盘了。如果你使用别的安装文件，安装过程中提示换盘的时候,
    先umount: sudo umount /media/cdrom，再用上面的挂载方法，挂上其它盘.
3.  建立安装matlab的目录：我是装在 /opt/matlab，命令：sudo mkdir
    /opt/matlab，然后把license文件拷贝到安装目录下面。

    -   如果版本是2006b,
        可以下载一个license的压缩包。里面有一个license\_lock,
        一个license\_server, 无论使用哪一个,
        拷贝到/opt/matlab/license.dat
    -   如果版本是2007b，在crack文件夹下面，可以找到两个license的文件，以及一个简单的安装说明，将其中任意一个拷贝到/opt/matlab/license.dat

4.  打开终端，sudo
    /media/cdrom/install。注意当前路径不要放在/media/cdrom，然后直接使用install，这样会提示有问题。所以上面命令用绝对路径.
    安装过程中遇到问题就看看上面的英文提示，正常情况下不会有太多问题的.
5.  安装路径: 提示你选择安装路径的时候就是你刚在建立的那个目录了.
6.  然后就会提示你选择要安装的组件，全选就可以了.
7.  提示换盘时，按我上面说的挂载上去就行.
8.  最后OK就行了.
9.  运行：sudo
    /opt/matlab/install\_matlab进行一些相关的设置，就按照默认的就行了.

</p>
~~如果进入matlab之后提示一些错误的话，如果是opengl方面的，最好就更新一下自己的显卡驱动；如果是java方面的话（我重装了以后点击一些yes,no,cancel之类的按钮就会crash,这种情况的话就在terminal下面运行：export
MATLAB\_JAVA=/usr/lib/jvm/java-1.5.0-sun-1.5.0.08/jre
(具体的路径请看自己的系统).
等号后面的是你的jre的目录，但是这么做也有不好的地方，就是只能在当前的terminal下面运行matlab，如果
另外打开一个terminal，还要再运行一遍上面的命令.
如果想以后不用再费劲的话，就编辑一下\~/.bashrc下面的内容，把上面的命令添加进去，
这样每次运行terminal的时候，这条指令就是自动执行的了，现在试试直接输入matlab吧~~!

**对于最新的matlab 2007b的一些问题更新如下：**

我个人使用kde，没有任何不正常现象，不过在网上见到有些朋友使用gnome的，运行matlab后，只有一个外框能正确显示，其它的都是一片白。同时转载过来见到的解决办法（实在不知道出处了，如果有朋友知道，不妨告诉我，Hugh一定注明）

</p>

1.  办法1：在matlab安装目录下的bin/matlab文件中（一堆注释后面）添加：

    </p>
    `export AWT_TOOLKIT=MToolkit`

    该方法可以解决显示问题，但会经常出现无法输入的问题。比如调用plot函数后，command窗口就

    无法输入新字符了，只能通过依次点击Current Directory 和
    Workspace解决。。依次点击后就可以

    <p>
    继续输入字符了。

2.  方法2：安装sun-java6-jre。具体方法为

    </p>
    `sudo apt-get install sun-java6-jre`

    然后在matlab安装目录下的bin/matlab文件中（一堆注释后面）添加：

    `export MATLAB_JAVA=/usr/lib/jvm/java-6-sun/jre/`

    <p>
    注意，不需要添加export
    AWT\_TOOLKIT=MToolkit了，这样修改以后就没有输入的问题。

</p>

如果你的matlab不能显示中文，那么你需要在File-Preference-Fonts中指定中文字体。如果你为了让字体显示效果更好一些的话，不妨选中下面的Use
antialiasing to smooth fonts，然后重启，开始你的matlab之旅吧！
