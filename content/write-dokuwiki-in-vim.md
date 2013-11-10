Title: 在vim中管理dokuwiki
Date: 2008-10-01 02:41
Author: Admin
Category: 电脑应用
Tags: vim, wiki, 知识管理
Slug: write-dokuwiki-in-vim

原来在[《如何进行个人知识管理》][]里面提到过使用[dokuwiki][]，这也是自己最近开始做的一件事情，在空间上架了一个wiki，然后准备把平时各方面收集的资料，以及个人的一些经验慢慢的组织起来。今天想介绍给大家的就是[dokuvimki][]这个vim的插件。因为新版本的[dokuwiki][]提供了试用的xml-rpc接口，这样远程编辑就变成了可能。

</p>

这里是最新版本的[dokuvimki下载地址][]。如果你平时也是用vim，也是尝试dokuwiki，那么你应该赶紧来试试看。你所需要做的就是把插件解压到\~/.vim/目录下面，然后在你的\~/.vimrc文件中加入以下的设置，这样在你编辑dokuwiki的时候，vim就会自动检测，将文件类型设定为dokuwiki。

</p>
<coolcode>

fun IsDokuWiki()

if match(getline(1,20),'\^ \\=\\(=\\{2,6}\\).\\+\\1 \*\$') \>= 0

set textwidth=0

set wrap

set linebreak

set filetype=dokuwiki

endif

endfun

" 检查当前Buffer是否为dokuwiki

autocmd BufWinEnter \*.txt call IsDokuWiki()

syntax on

</coolcode>

另外，还有一些关于你的dokuwiki的用户名，地址之类的设定，也是加入到\~/.vimrc中：

<coolcode>

" 登录dokuwiki的用户名

let g:DokuVimKi\_USER = 'username'

" 登录密码

let g:DokuVimKi\_PASS = 'password'

" 远程wiki的地址(不需要最后的"/")

let g:DokuVimKi\_URL = 'https://yourwikidomain.org'

" 是否在打开vim的时候连接远程wiki

let g:DokuVimKi\_AUTOCONNECT = 'no'

" dokuwiki页面树显示宽度

let g:DokuVimKi\_TREEWIDTH = '40'

" 页面树窗口中文件列的宽度

let g:DokuVimKi\_FOLDCOLWIDTH = '10'

</coolcode>

这样的话就算基本上设置好了。这个插件提供了几个命令，便于你编辑以及管理dokuwiki:

<coolcode>

:DWEdit <pagename> 编译页面，如果页面不存在的话就会建立该页面。

:DWSend <summary> 发送当前buffer中的页面到远程wiki

:DWList <pattern> 列出当前的所有页面。

:DWAuth 编辑之前验证身份，基本你刚才设定的登录信息

</coolcode>

当然还有其他的一些命令，关于页面修改记录，页面树以及反向链接等等，如果有兴趣的大家可以自己去看看。另外就是插件本身还有一个dokuwiki语法的快捷键，在\~/.vim/plugin/dokuvimki.vim当中可以找到相关的部分，大家可以根据自己的喜好或者需要修改。

另外，经过作者的更新，现在的版本对于中文支持的非常不错，不过要在utf8环境下面，大家可以试验以下，如果有问题的话不妨直接向作者反馈！

  [《如何进行个人知识管理》]: http://www.quhuashuai.com/2008/03/how-to-do-personal-knowledge-management/
  [dokuwiki]: http://wiki.splitbrain.org/wiki:dokuwiki
  [dokuvimki]: http://www.chimeric.de/projects/dokuwiki/dokuvimki
  [dokuvimki下载地址]: http://www.chimeric.de/_media/projects/dokuwiki/dokuvimki/dokuvimki-2008-05-20.tgz
