Title: Archlinux中配置Okular下缺失的英文字体
Date: 2008-10-09 06:30
Author: Admin
Category: 电脑应用
Tags: linux, 分享
Slug: okular-font-problem-in-archlinux

在解决okular下面部分英文字体缺失之前，一直在用xpdf或者Acroread看pdf文档。可是在这个的同时我已经纳闷了很久，这个okular的英文字体到底是怎么个机制来查找的，试图修改过xpdfrc，没有任何效果，在我尝试了很久之后终于解决了问题。

</p>

先把问题说说看，不知道大家遇到过没有。《Math Into
Latex》这个文档我在用Latex写笔记的时候总会开着，难免忘记了一些什么符号，不过Okular下面的字体惨不忍睹，很多字母重合在一起，先上个图大家看看：

</p>
![配置前的Okular字体][]

简单说下我的系统，Archlinux，FVWM，字体用了Lucida和STHeiti稍作美化，所以修改了\$HOME下的.fonts.conf文件，所以问题也就出在这里。在我解决问题之后，我把\$HOME/.fonts.conf删除后，发现okular会到系统的/usr/share/fonts/TTF下寻找字体，显示的效果是这样的：

</p>
![没有任何配置的Okular字体][]

#### 解决办法：

</p>

如果你在Okular的菜单中找到File -
Properties，然后在Fonts标签下就会看到缺失的字体名称，在这个Math\_Into\_Latex.pdf文件中缺失的便是一系列Galliard字体，包括Galliard-Bold,
Galliard-BoldItalic, Galliard-Italic,
以及Galliar-Roman。首先要解决问题的话必须下载这些字体，我在某个英文站点找到了下载，大家也可以根据自己的情况下载对应的字体。

</p>

第二件事情便是把这些字体放在适当的文件夹下，一般来说放在\$HOME/.fonts/下面就可以，至少我是这样的。在你登录之后，这些字体是可以使用的。

</p>

接下来需要做的便是在\$HOME/.fonts.conf里面添加类似下面的内容：

<coolcode lang="xml">

<match target="pattern" name="family">

<test name="family" qual="any">

<string>Galliard</string>

</test>

<edit mode="assign" name="family">

<string>Galliard BT</string>

</edit>

</match>

</coolcode>

这样Okular在启动之后,
遇到Galliard类的字体，便会自动配对了，否则不一定会找到哪个字体。问题解决之后，再上图看看效果，这次在File
- Properties当中看到的这些Galliard字体都是准确使用的对应字体了。

</p>
![配置后的Okular字体][]

对于Linux，我确实是菜鸟一个，在慢慢学习，都说用linux的人喜欢折腾，我这也算自己折腾出个东西，分享给大家。我觉得如果对于fontconfig很了解的，

应该很快就能解决这个问题，我嘛，就需要很久来尝试了。不管怎么说，这至少也是个原创，呵呵！

</p>

  [配置前的Okular字体]: http://pic.yupoo.com/huashuai/33147651506d/medium.jpg
  [没有任何配置的Okular字体]: http://pic.yupoo.com/huashuai/95488651506e/medium.jpg
  [配置后的Okular字体]: http://pic.yupoo.com/huashuai/95509651506d/medium.jpg
