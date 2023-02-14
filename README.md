# wReply
从外部导入词库，项目名是乱起的

希望使用更加便捷的词库管理可以尝试铃心自定义和Dice溯洄，论坛也有大佬的自定义回复插件。此项目作为哥们一边学一边写的项目，不是很成熟


# 需要
  python环境(我用的3.9.0)
  
  [mirai-api-http](https://github.com/project-mirai/mirai-api-http)，并配置，[配置文件示例](https://github.com/avilliai/wReply/blob/master/setting.yml)
  
  目前使用的[词库](https://mirai.mamoe.net/topic/1829/%E5%BC%BA%E5%A4%A7%E7%9A%84%E4%BA%8C%E6%AC%A1%E5%85%83%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%E8%AF%8D%E5%BA%932w-%E8%AF%8D%E6%9D%A1-%E4%B8%8D%E5%AE%9A%E6%9C%9F%E6%9B%B4%E6%96%B0)来自neko002佬
# how to use
  1.克隆仓库到本地
  
  2.打开cmd，运行pip install -r requirements.txt
  
  3.修改main.py中的qq,port,key qq是你bot的qq，vertify_key和 port参考你的mirai-api-http配置文件，
  
  如果你用了上面的[配置文件示例](https://github.com/avilliai/wReply/blob/master/setting.yml),则只需修改3377428814为你bot的qq;
  
  继续向下划拉能看到botName变量，改成你bot的名字，master改成你的QQ，replypro=90意思是在群内不艾特时回复的概率是90%(艾特必定会执行匹配)
  
  3.运行main.py
  
# 指令如下

  key是你要操作的关键词
  
  txt文件是你bot直接使用的,在群里对词库进行操作会自动同步到xlsx
  
  xlsx文件是管理用的,需要在群里发送 导入词库 才会把xlsx里面的内容同步到bot使用的词库
  
  **更新词库的方式**
  
  导入词库  此命令用于将excel表格内容导入txt
  
  导出词库  此命令用于将txt导出到excel表格
  
  
  **管理模糊匹配词库指令**
  
  模糊添加
  
  模糊删除key
  
  Mel#key
  
  **管理完全匹配词库指令**
  
  开始添加
  
  删除key
  
  del#key
  
  *添加语音回复*
  
  详见另一个帖子
  
  **授权机制**
  
  授权#qq
  
  取消授权#qq
