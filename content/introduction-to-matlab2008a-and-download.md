Title: Matlab 2008a介绍以及下载地址
Date: 2008-03-23 22:25
Author: Admin
Category: 电脑应用
Tags: matlab
Slug: introduction-to-matlab2008a-and-download

<!--- google_ad_section_start --->

自从开始博客的时候，介绍了那篇[《Ubuntu下安装Matlab过程》][]之后，就再也没有写过Matlab的内容，因为自己不想把这里写成一个关于Matlab的技术学习博客，哈哈！今天是因为找到了Matlab
2008a的下载地址，所以决定分享出来，大家一起来加速吧！

</p>

话说Mathworks现在每年都会推出a，b两个版本，大概是在3月和9月的样子，今年也是在3月推出了非常重要的一个新版本Matlab
2008a，也叫做Matlab
7.6，在这个版本当中加入了一些重要的功能。大家不妨先看看一些新功能的介绍，以下应用了大牛林达华的博客-[笑对人生，傲立寰宇][]中的一些介绍。

</p>
<!--- google_ad_section_end --->

1、完全实现面向对象编程。其实，在MATLAB的早期版本里面，也有class的概念，不过大家如果使用过的话，可能知道那是一种不太好的设计。功能不强，过程繁琐，而且，很多很tricky的地方，尤其是重载numel,
subsref这类函数的时候。而新的设计抛开了历史包袱，现在写出来的类和在python里面写的长得差不多，舒服多了。这套设计，吸取（或者“抄袭”）了Python和C\#的优点，除了支持封装(encapsulation)，继承(inheritance)，和多态(polymorphism)
这些基本特性以外，还支持了一些新兴的特性，包括属性(property)，事件(event)，和静态方法(static
method)。

2、支持Handle类型——用另外一种说法，就是支持函数调用传引用。以前matlab传递参数只有一种方法，copy
on
write。就是说，当你传一个东西进去，如果它要发生改变，那么，这个东西会整个copy一份，然后修改会在副本上生效。这使得实现动态数据结构变得非常困难。比如一个列表，如果每添加一个元素，都要拷贝整个列表一次，将是什么效果呢？因此，传统上matlab擅长于以矩阵为基础的算法，但是对于以经典动态数据结构为基础的算法，比如动态列表，哈希表，搜索树，图等，就力不从心了。这个新版本终于引入了对引用的支持，这将使MATLAB实现经典数据结构和算法变得前所未有的轻松。现在，数值和统计算法与经典算法越来越多地合流，很多应用都需要同时使用两方面的算法，MATLAB的这个变化正好适应了这种需求。

3、引入了名空间的管理。以前，MATLAB所有的函数都在同一个global的名空间下面。比如两个工具包里面出现了同名函数，解决起来很麻烦。比如现在有两个算法叫LDA，一个是Latent
Dirichlet Allocation，一个是Linear Discriminant
Analysis，在一个应用中需要同时用到两个算法，而写这两个算法的人各自把它们命名为lda.m，那么问题就出来了。一种naive的方法是改名字，不过会直接破坏掉那些toolbox里面对那个函数的依赖。而这个版本，它借鉴其它高级语言的经验，终于引入了namespace，给这个问题一个很好的解决。

在林达华的博客上还有一些包括工具箱的介绍，有兴趣的话可以去看看。不过要是真想体验2008a的话，相信还是自己下载来的实在。**现在网上有2008a的破解出现，地址分别是：[Mininova][]以及[TPB][]，有兴趣的朋友可以赶紧去看看。**不过Linux下的破解版本应该还没有出现，毕竟是破解的，所以版权问题大家自己斟酌就好了。

</p>

**更新两个下载地址，但是有一定限制，在smth上面看到的：**

</p>
1、水木上一个哥们做的公网分流，因为服务器承受能力原因，所以有一定限制，大家看看rp吧，一般连不上，呵呵！

ftp地址：[ftp://alpher.cn][]

用户名: temp

密码: temp

限速150k，最大链接数5 users, 2 users/ip

有效期：两周之内

2、清华晨光bt，一样有限制，估计只有清华的ip可以访问，亦或教育网ip，具体情况不得而知，大家可以试试。

地址:[http://thubt.cn][]

**Update again: 留言中[conge][]说在TFL Server
40上可以下到，不过需要论坛的账号才可以。另外conge还说可以在迅雷上面找到下载，相信这样很多朋友都可以下到了。**

</p>
<?php if(get_option('backlinks_key')) : ?>

<p>
<li>
#### 赞助链接

</p>
<?php backlinks_links() ?>

<p>
</li>
</p>
<?php endif; ?>

  [《Ubuntu下安装Matlab过程》]: http://www.quhuashuai.com/2007/08/install_matlab_on_ubuntu/
  [笑对人生，傲立寰宇]: http://dahua.spaces.live.com/
  [Mininova]: http://www.mininova.org/tor/1261430
  [TPB]: http://thepiratebay.org/tor/4092904/Mathworks.Matlab.R2008a.DVD.ISO-TBE
  [ftp://alpher.cn]: ftp://alpher.cn
  [http://thubt.cn]: http://thubt.cn
  [conge]: http://congel.blogspot.com/
