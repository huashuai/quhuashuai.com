Title: Archlinux下安装Matlab 2008a
Date: 2008-09-11 12:02
Author: Admin
Category: 电脑应用
Tags: linux, matlab
Slug: install-matlab-2008a-on-archlinux

前些日子刚刚从Ubuntu过渡到了Archlinux，自己其实就是瞎凑热闹，别人都说Archlinux比较火，我就也凑过来看看，而且自从Matlab
2008a发布之后还没有尝试过，尽管[自己曾经介绍过][]。现在已经有了Mac和Linux下的2008a的下载，[地址就在这里][]，有兴趣的可以自己去试试看。

</p>

整个安装过程还是比较简单的，基本上和我在[《Ubuntu下安装matlab过程》][]中提到的一样，在这里稍微重复一下：

</p>

1.  挂载iso文件：sudo mount -t iso9660 (iso文件的路径) /media/cdrom -o
    loop。在Archlinux下面可能你需要加载一下loop,也就是sudo modprobe
    loop。因为这个是DVD，所以没有再umount以及换盘的必要了。
2.  建立Matlab安装目录：sudo mkdir /opt/matlab。这样就可以了，matlab
    2008a的破解有些不同，所以这里并不需要拷贝任何的license文件到安装目录下。
3.  终端下运行sudo /media/cdrom/install。使用绝对路径，这样不会出现问题。
4.  安装过程中会提示让你选择注册的方式，一共有两种，在光盘下的crack文件夹下有详细说明，以及license文件，我这里选择的是稍后注册。
5.  安装完成之后，运行sudo
    /opt/matlab/install\_matlab进行一些相关设置，以及启动文件的连接之类工作，一路默认下来就可以了。
6.  当你首次运行matlab的时候，会让你选择license文件所在的目录，这个时候如果你是普通用户运行的话，会无法完成注册，所以记得用root账户来运行matlab，后面的工作就是按照你的注册方式，选择对应的license文件。

</p>

一般来说，在此之后你就可以顺利的运行matlab
2008a了。不过你很有可能象我一样遇到Java的问题，因为matlab使用自己的Java设置，所以尽管你系统里的其他Java程序没有问题，matlab不会理你是怎么设置的，所以启动matlab之后会出现java一类的错误。这样你就需要到/opt/matlab/sys/java/jre/glnx86/目录下：首先删除掉原本的jre1.6.0，然后将系统的link过来，执行起来就是：

</p>

cd /opt/matlab/sys/java/jre/glnx86

sudo mv jre1.6.0/ jre1.6.0-bakcup （稍作备份）

sudo ln -s /opt/java/jre/ jre1.6.0 （我的java是装在/opt下)

</code>

另外还有一个就是可能出现的字体问题，解决方法也很简单，这个基本上一次就可以解决所有的java程序字体，到/opt/java/jre/lib/fonts下建立fallback目录，再到fallback目录下面把你想要使用的中文字体link过来就好了。

</p>

  [自己曾经介绍过]: http://www.quhuashuai.com/2008/03/introduction-to-matlab2008a-and-download/
  [地址就在这里]: http://thepiratebay.org/torrent/4361148/Matlab_7.6_2008a_(intel_only)___crack
  [《Ubuntu下安装matlab过程》]: http://www.quhuashuai.com/2007/08/install_matlab_on_ubuntu/</p><p>%20%20
