测试Python版本：3.12.1
运行此脚本所需外部库：
pip install requests pycryptodome pyyaml httpx
本人不使用青龙面板，所以写的脚本都是按照可独立运行的Python方式来写，理论上支持从青龙面板运行，无法运行请自行想办法

使用说明：
首先通过各种渠道下载one APP，下载后登录账号，然后抓包，抓包教程就不细说了，Fiddler抓不到就用Fiddler Everywhere，抓请求头中的uuid、user-key、token分别填入config.yaml中对应项
再配置好wxpusher的token和uid
配置好后首先运行一次refreshToken.pyc，脚本输出成功的消息后，config.yaml中的token会被刷新，也会增加一些参数，这个不用管
refreshToken.pyc建议每隔6-8小时运行一次，以防止token过期
freeBuy.pyc建议30分钟-1小时运行一次
buyPusher.pyc建议每天23:50运行一次，用于推送当天的白嫖记录（只能推送当天的记录，所以一定要在0点前完成推送）