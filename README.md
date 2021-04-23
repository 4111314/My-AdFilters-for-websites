# My-AdFilters-for-websites
对于一些网站的屏蔽列表，支持Ublock Origin和X浏览器等

一、项目原因与目标

在网上浏览时，遇到某些网页实在是恶心，想要屏蔽它们。

屏蔽分两部分，一部分是屏蔽网站本身，让这些网站本身就打不开；另一方面是在搜索引擎（特别是谷歌）的搜索结果中屏蔽这些网站的链接。

二、使用的工具介绍

使用的工具包括Ublock Origin，uBlacklist，X浏览器和AC-baidu脚本

Ublock Origin是一款浏览器扩展，支持桌面端主流浏览器（旧版Microsoft Edge，新版Microsoft Edge，Safari，Chrome，Firefox，Opera等）和安卓端部分浏览器（Firefox完全适配；Kiwi经测试应该完全兼容；Yandex没试过）。它本身是用于广告拦截的，但是可以通过拦截域名来实现对网站的拦截，我这里就使用了这个功能。

安装请移步：
https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak 
https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm
https://addons.mozilla.org/zh-CN/firefox/addon/ublock-origin/
https://addons.opera.com/zh-cn/extensions/details/ublock/

uBlacklist是桌面端谷歌浏览器的一个扩展，可以拦截谷歌搜索的结果，使之在搜索结果中不出现。该扩展同时也会对DuckDuckGo和Startpage起作用。

X浏览器只支持安卓端，拥有非常强大的广告拦截功能，但不完全兼容Adblock Plus的语法。

AC-baidu脚本有许多功能，具体介绍请移步：https://greasyfork.org/zh-CN/scripts/14178-ac-baidu-%E9%87%8D%E5%AE%9A%E5%90%91%E4%BC%98%E5%8C%96%E7%99%BE%E5%BA%A6%E6%90%9C%E7%8B%97%E8%B0%B7%E6%AD%8C%E5%BF%85%E5%BA%94%E6%90%9C%E7%B4%A2-favicon-%E5%8F%8C%E5%88%97

桌面端浏览器可使用Ublock Origin，uBlacklist和AC-baidu脚本；安卓端可使用X浏览器、Ublock Origin和uBlacklist（如果支持的话），目前没找到在安卓端使用AC-baidu脚本的办法。

Ublock Origin和X浏览器用于拦截网站，AC-baidu脚本和uBlacklist用于拦截搜索引擎（特别是谷歌）的搜索结果。

三、屏蔽列表介绍

1.txt里面是长年炮制假新闻，反华反共反人类的网站、恐怖组织、邪教组织或者是作为意识形态传播工具的政治战心理战部队、媒体、NGO等

2.txt里面是一些著名的流氓导航网页，或者是一些流氓软件等臭名昭著的、看到了就心烦的那种

3.txt里面是一些内容农场，那种到处复制粘贴一大堆不相干的东西，骗人进去打广告的那种。

4.txt里面是一些会在移动端(特别是安卓手机端)有流氓行为(比如无法回退，震动，自动下载安装包等)的网站

以上是为Ublock Origin准备的。

Xbrowser_n.txt是专为X浏览器准备的。X浏览器不是Ublock Origin，经过实际测试，似乎不能只输入一个短的域名就拦截所有的类似网站。所以搞一个完整版的。

uBlacklist_n.txt就为uBlacklist这个扩展准备的。但我已经决定采用AC-baidu脚本来解决这个问题，而且github上已经有人为这个扩展准备了屏蔽内容农场的列表。

可以移步去那个项目：https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist

按照项目中的描述，他已经收集了四年多，我看了一下，超过1000个，绝对比我现在收集的更全。我准备如果我又发现内容农场，我就去那个项目那边告诉他。

所以这个文件现在已经停止更新。

因为桌面端和移动端进行拦截的工具和原理都不一样，包括需要应对的威胁也不一样，所以两边的不完全通用。

附加说明

以下均以example.com,123.example.com和123.example.com/456 这三个域名为例。纯粹只是举个例子，如果确实存在如上的网站，纯属偶然。

如果将example.com添加到Ublock Origin屏蔽列表中，那么example.com,123.example.com和123.example.com/456都会被拦截。

如果将example.com添加到uBlacklist屏蔽列表中（但是要注意语法！），那么example.com,123.example.com和123.example.com/456在谷歌搜索引擎的结果中都会被屏蔽。

如果将example.com添加到X浏览器屏蔽列表中，那么example.com会被拦截，但123.example.com和123.example.com/456不会被拦截。

如果将example.com添加到AC-baidu脚本屏蔽列表中，那么example.com,123.example.com和123.example.com/456在谷歌搜索引擎的结果中都会被拦截。

四、具体操作

Ublock Origin（待续）

uBlacklist请移步https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist

X浏览器（待续）

AC-baidu脚本请移步https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist

五、其他

如果有人想订阅规则的话，可以直接用。

如果想转载，请注明出处。

如果有其他网站符合描述的情况的话，可以在issues里通知我，我看到了后会评估是否加上去。

六、感谢名单

https://github.com/gorhill/uBlock

https://github.com/uBlockOrigin/uAssets

https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist

https://github.com/langren1353/GM_script

（此名单不完全）
