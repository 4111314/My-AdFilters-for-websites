# My-AdFilters-for-websites
对于一些网站的屏蔽列表，支持Ublock Origin，X浏览器，uBlacklist和AC-baidu脚本

# 一、项目原因和目标

在网上浏览时，遇到某些网页实在是恶心，想要屏蔽它们。

屏蔽分两部分，一部分是屏蔽网站本身，让这些网站本身就打不开；另一方面是在搜索引擎（特别是谷歌）的搜索结果中屏蔽这些网站的链接。

# 二、使用的工具介绍

可使用的工具包括Ublock Origin，uBlacklist，X浏览器和AC-baidu脚本

注：本来我想通过v2rayN等代理软件的路由规则来实现对网站的屏蔽，但我使用的是白名单规则，这样的话，因为名单不可能完全精准，某些打不开的网站，也不知道是想屏蔽的还是路由规则的问题导致打不开。而Ublock Origin可以直接以一种非常简洁明了的方式拦截住，并且我可以看到拦截它的规则。只要规则属于我写的这些列表，那么它明显就是我想屏蔽的网站。这样可以很好地进行区分。

## 1.Ublock Origin

这是一款浏览器扩展，支持桌面端主流浏览器（旧版Microsoft Edge，新版Microsoft Edge，Safari，Chrome，Firefox，Opera等）和安卓端部分浏览器（Firefox完全适配；Kiwi经测试应该完全兼容；Yandex没试过）。它本身是用于广告拦截的，但是可以通过拦截域名来实现对网站的拦截，我这里就使用了这个功能。

安装请移步：

https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak

https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm

https://addons.mozilla.org/zh-CN/firefox/addon/ublock-origin/

https://addons.opera.com/zh-cn/extensions/details/ublock/

## 2.uBlacklist

这是桌面端谷歌浏览器的一个扩展，可以拦截谷歌搜索的结果，使之在搜索结果中不出现。**该扩展同时也会对DuckDuckGo和Startpage起作用。**

## 3.X浏览器
**只支持安卓端**，拥有非常强大的广告拦截功能，但不完全兼容Adblock Plus的语法。

**X浏览器的拦截网站只能适用于X浏览器本身!** 

## 4.AC-baidu脚本

**需要安装油猴**，有许多功能，具体介绍请移步：https://greasyfork.org/zh-CN/scripts/14178-ac-baidu-%E9%87%8D%E5%AE%9A%E5%90%91%E4%BC%98%E5%8C%96%E7%99%BE%E5%BA%A6%E6%90%9C%E7%8B%97%E8%B0%B7%E6%AD%8C%E5%BF%85%E5%BA%94%E6%90%9C%E7%B4%A2-favicon-%E5%8F%8C%E5%88%97

**安装油猴的方法**，见https://greasyfork.org/zh-CN

## 5.不同平台具体使用

**桌面端浏览器**可使用Ublock Origin，uBlacklist和AC-baidu脚本；**安卓端**可使用X浏览器、Ublock Origin和uBlacklist（**如果支持的话**），**目前没找到在安卓端使用AC-baidu脚本的办法**。

Ublock Origin和X浏览器用于拦截网站，AC-baidu脚本和uBlacklist用于拦截搜索引擎（特别是谷歌）的搜索结果。

# 三、屏蔽列表介绍

## 1.Ublock Origin

**1.txt**里面是长年炮制假新闻，反华反共反人类的网站、恐怖组织、邪教组织或者是作为意识形态传播工具的政治战心理战部队、媒体、NGO等

**2.txt**里面是一些臭名昭著的流氓软件或流氓导航网页、看到了就心烦的那种

**3.txt**里面是一些内容农场，那种到处复制粘贴一大堆不相干的东西，骗人进去打广告的那种。

**4.txt**里面是一些会在移动端(特别是安卓手机端)有流氓行为(比如无法回退，震动，自动下载安装包等)的网站

## 2.X浏览器

Xbrowser_n.txt是**专为X浏览器**准备的。X浏览器不是Ublock Origin，经过实际测试，似乎不能只输入根域名就拦截所有的子域名。所以搞一个完整版的。

## 3.uBlacklist

uBlacklist_n.txt就为uBlacklist这个扩展准备的。但我已经决定采用AC-baidu脚本来解决这个问题，而且github上已经有人为这个准备了适合uBlacklist扩展屏的蔽内容农场的列表。

可以移步去那个项目：https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist

按照项目中的描述，他已经收集了四年多，我看了一下，超过1000个，绝对比我现在收集的更全。我准备如果我又发现内容农场，我就去那个项目那边告诉他。

也可以自己写脚本自动的将他那个列表转成适合Ublock Origin或X浏览器的列表。

**所以这个文件现在已经停止更新。**

## 4.AC-baidu

同Ublock Origin

目前没找到订阅功能，只能将想屏蔽的网址手动粘贴到相应文本框中。暂时没找到解决办法，只能过段时间手动更新。

## 5.附加说明

因为桌面端和移动端进行拦截的工具和原理都不一样，包括需要应对的威胁也不一样，所以两边的不完全通用。

以下均以example.com,123.example.com和123.example.com/456 这三个域名为例。

**纯粹只是举个例子，如果确实存在如上的网站，纯属偶然。**

如果将example.com添加到Ublock Origin屏蔽列表中，那么example.com,123.example.com和123.example.com/456都会被拦截。

如果将example.com添加到uBlacklist屏蔽列表中（**但是要注意语法！**），那么example.com,123.example.com和123.example.com/456在谷歌搜索引擎的结果中都会被屏蔽。

如果将example.com添加到X浏览器屏蔽列表中，那么example.com会被拦截，但123.example.com和123.example.com/456不会被拦截。

如果将example.com添加到AC-baidu脚本屏蔽列表中，那么example.com,123.example.com和123.example.com/456在谷歌搜索引擎的结果中都会被拦截。

# 四、具体操作

## 1.Ublock Origin

先安装。安装完后，这个扩展是一个盾牌的形状，接近深红色，中间有连着的u和o两个白色字母。鼠标左键单击该扩展，选择右下角的齿轮打开控制面板。在出来的界面中，在最上面的菜单栏中选择第二个“**规则列表**”。然后拉到最底下。然后在最底下的“**自定义**”中，点击“**导入**”，在出来的文本框中黏贴相关规则的网址，并点击最上方的“**√应用更改**”，即可完成订阅。

## 2.uBlacklist

请移步https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist#%E5%B1%8F%E8%94%BD-google-%E4%B8%AD%E6%96%87%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C

## 3.X浏览器

通过Google Play商店，或国内其他各大应用商店，或Google Play商店镜像站，或X浏览器官网下载安装包等方式，下载X浏览器并安装（**注意Google Play版和国内其他各大应用商店版的X浏览器的包名不同，但区别仅是Google Play版有更多的语言支持。**）。

安装完后打开X浏览器，点击X浏览器底部导航栏3条横线->点击左下角齿轮进入"**设置**"->点击**广告拦截**->点击**规则文件**->点击右上方**导入**->点击**从网址导入**->在出来的文本框中将规则文件的文件的**完整url**输入->点击**导入**，即可完成订阅，订阅成功。

## 4.AC-baidu脚本

请移步https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist#%E5%B1%8F%E8%94%BD-baidu-%E4%B8%AD%E6%96%87%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C

# 五、其他

说明与几个具体的列表文件都还在完善中。

如果有人想订阅规则的话，可以直接用。

如果想转载，请注明出处。

如果有其他网站符合描述的情况的话，可以在issues里通知我，我看到了后会评估是否加上去。

是否更新取决于有没有新发现以及我有没有时间等多方面原因。

# 六、感谢名单

https://www.52pojie.cn/thread-1070300-1-1.html (提供了对恶意广告网站的完整的分析)

https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist (收集了大量内容农场)

https://github.com/gorhill/uBlock(Ublock Origin官方项目)

https://github.com/langren1353/GM_script(AC-baidu脚本官方项目)

https://github.com/uBlockOrigin/uAssets(Ublock Origin的一些资源，包含了一些恶意网站)

https://www.xbext.com/ (X浏览器官网)

（此名单不完全，按域名排序）


（待续）
