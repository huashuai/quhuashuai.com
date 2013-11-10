Title: Archlinux下给T43添加Win键(Super键)
Date: 2009-04-17 12:17
Author: Admin
Category: 电脑应用
Tags: linux
Slug: add-windows-key-to-archlinux-under-T43

为了使用FVWM的需要，Super键，或者说Windows键是必不可少的，可是自己的T43上面只有两个Alt键，所以比较可行的选择就是把右边那个变成Windows键。本来很久之前就已经搞定了，只是最近的一次升级之后，不知道为什么以前的修改失效了，花了点时间改好之后特意记录下来。以前的修改是靠xkeycaps自动完成的，但是估计这个程序是很久以前的，里面有的键盘种类比较少，这次我怎么改都没有成功，所以才开始动手自己寻找解决办法。

<span style=" font-size:large;">需要的工具：</span>

只需要xev以及xmodmap就可以搞定，我不确定是不是系统自带的，如果没有的话，使用pacman或者yaourt自己装一下就好了。

<span style=" font-size:large;">修改原理：</span>

这个修改的工作是由xmodmap完成的，它的功能就是完成键盘的物理键映射到计算机内部的逻辑键，也就是说，如果你愿意，你可以修改任意的按键，完全打乱键盘的次序都没有关系。xmodmap完成键映射的命令格式是：
*xmodmap -e "keycode NUMBER = KEYNAME"* 。其中 *keycode* 是关键字，
*NUMBER* 是键的编号，也即物理名称， *KEYNAME*
是逻辑名称，即计算机内部把序号为 *NUMBER* 的键当 *KEYNAME*
处理。如果需要的话可以可以直接*man xmodmap*查看。

另外我们可以把我们所做的修改写入配置文件当中，比如常用的
*\~/.Xmodmap*，同时我们只需要修改 *\~/.xinitrc*文件，加入*xmodmap
\~/.Xmodmap*这条语句，这样在我们每次启动X之后，你所希望的配置就已经启用了。当然配置文件当中还有一些类似remove和add的语句，很容易理解，大家可以看下后面的过程。

<span style=" font-size:large;">修改步骤:</span>

因为我个人想要把右边的Alt键修改为Super键，所以后面的步骤当中都是在这个基础之上的。

-   在命令行下输入xev，然后在跳出的那个小窗口当中按下右侧的Alt键（或者任何你想要修改的按键），观察终端下面出现的提示信息，在这里我们可以找到*keycode
    NUMBER*以及*KEYNAME，*在我这里输出信息为：

` KeyRelease event, serial 35, synthetic NO, window 0x3800001, root 0x82, subw 0x3800002, time 6287212, (20,28), root:(42,90), state 0x40, keycode 108 (keysym 0xffec, Alt_R), same_screen YES, XLookupString gives 0 bytes: XFilterEvent returns: False `

我们所需要的信息就是keycode 108，以及括号当中的Alt\_R。

-   我们需要查看我们当前的按键配置，在命令行下输入xmodmap，我们可以看到在mod1一行当中有Super\_R,
    Alt\_R，同时在mod4下面有Super\_L，Hyper\_L，知道了当前配置之后我们才可以进行修改。

-   接下来我们需要在\$HOME目录下面建立一个.Xmodmap文件，在里面写入：

</p>
`remove Mod1 = Super_R Alt_R`

remove Mod4 = Super\_L Hyper\_L

keycode 0x6c = Super\_R

add Mod4 = Super\_R</code>

所以第一行我们把Super\_R和Alt\_R从当前的mod1当中删除，第二行把Super\_L以及Hyper\_L从当前的mod4当中删除，第三行将当前的Alt\_R键映射为Super\_R键，值得注意的是keycode之后的0x6c其实是我们之前得到的keycode
108的16进制表示方式，最后一行便是将Super\_R键加入到当前的mod4当中。

-   这样之后我们就可以在FVWM的配置文件中，使用Mod4，也就是Super键了。不过需要说明的是，如果只是为了在fvwm当中使左右的Alt键具有不同的功能，我们需要做的只是在*\~/.Xmodmap*当中将Alt\_L保存在mod1当中，而将Alt\_R保存在mod4中，相信这样就没有问题了，只是你要使用compiz之类的东西的话，需要Super键的存在。

基本上就是这样的过程，希望能够帮上那些和我一样的新手。

</p>

<p>

</p>

<p>

</p>

