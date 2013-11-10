Title: Archlinux下启用Thinkpad功能键
Date: 2008-10-15 17:39
Author: Admin
Category: 电脑应用
Tags: linux, ubuntu
Slug: enable-fn-in-thinkpad-under-archlinux

不知道是Thinkpad的问题，还是Archlinux的问题，自从由Ubuntu换到了Archlinux之后，我的T43就没有成功搞定过Thinkpad的这些功能键，所以Fn这个键就成了个摆设，每次需要开启蓝牙或者关闭屏幕的时候，我能做的事情就是敲一些命令，实在有点烦。今天在网上找了一些，确实是有解决办法的，而且并不复杂，我们需要做的事情就是修改/etc/acpi/handler.sh这个问题，在这里面配置下功能键对应的命令。

</p>

开始之前，先确定你已经在/etc/rc.conf里面加载了ibm\_acpi这个Module。这是我们进行修改和配置的先决条件，接下里将原本的/etc/acpi/handler.sh备份一下，尽管来说很多时候并不是需要这么做，鉴于我们都是新手，防止出现意外还是备份一下比较安全。这些都搞定之后，把下面的这段代码保存为新的/etc/acpi/handler.sh。

</p>

<coolcode linenum="no">

\#!/bin/sh

\# Default acpi script that takes an entry for all actions

\# NOTE: This is a 2.6-centric script. If you use 2.4.x, you'll have to

\# modify it to not use /sys

set \$\*

case "\$1" in

ibm/hotkey)

case "\$2" in

HKEY)

case "\$4" in

​00001002) \# Lock screen

xscreensaver-command -lock

;;

​00001003) \# swithing display off

xset dpms force off

;;

​00001004) \# Suspend to RAM

/usr/sbin/pm-suspend

;;

​00001005) \# Switch Bluetooth

if [ "\$(grep "status.\*enabled" /proc/acpi/ibm/bluetooth)" ]; then

echo "disable" \> /proc/acpi/ibm/bluetooth

else

echo "enable" \> /proc/acpi/ibm/bluetooth

fi

;;

​00001007) \# Toggle external display

if [ "\$(xrandr -q | grep "VGA connected")" ]; then

if [ "\$(xrandr -q | grep "VGA connected [0-9]")" ]; then

xrandr --output VGA --off

else

xrandr --output VGA --auto

fi

else

xrandr --output VGA --off

fi

;;

\#00001008) \# Toggle Trackpoint/Touchpad

\# ;;

\#00001009) \# Eject from dock

\# ;;

0000100c) \# Hibernate

/usr/sbin/pm-hibernate

;;

\#00001014) \# Toggle zoom

\# ;;

\#00001018) \# ThinkVantage button

\# ;;

esac

;;

esac

;;

button/lid)

case "\$2" in

LID)

case "\$3" in

​00000080) \# Lid opened/closed

grep open /proc/acpi/button/lid/LID/state || hibernate -F
/etc/hibernate/ususpend-ram.conf

;;

esac

;;

esac

;;

ac\_adapter)

case "\$2" in

AC)

case "\$4" in

​00000001) \# AC plugged

echo -n performance \>
/sys/devices/system/cpu/cpu0/cpufreq/scaling\_governor

;;

​00000000) \# AC unplugged

echo -n ondemand \>
/sys/devices/system/cpu/cpu0/cpufreq/scaling\_governor

;;

esac

;;

esac

;;

video)

case "\$2" in

LCD0)

case "\$3" in

​00000086) \# Brightness up

brightness +

;;

​00000087) \# Brightness down

brightness -

;;

esac

;;

esac

;;

esac

</coolcode>

在保存好之后，其实你可以根据自己的需要修改一些对应的命令，进而调整一些功能键。在我的这个配置下面，Fn+F2是使用xscreensaver锁定屏幕；Fn+F3是关闭显示屏幕；Fn+F4是挂起，这里我使用的是pm-suspend；Fn+F5是切换蓝牙的开关；Fn+F7是启动外接显示器或者投影仪之类的；Fn+F12是休眠。基本上就是这样，同时还启用了调整屏幕亮度，打开上面小灯等功能。至少在我的T43上面这些功能都没有问题。

</p>

这些都搞定之后你只需要sudo /etc/rc.d/acpi
restart，重启启动acpi就好了，现在赶紧来试试看吧，那些你熟悉的功能键是不是都找回来了？

</p>

*本文主要参考[Arch Linux Forum][]*

  [Arch Linux Forum]: http://bbs.archlinux.org/viewtopic.php?id=45710
