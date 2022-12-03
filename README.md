# wReply
从外部导入词库
# 需要
  python环境(我用的3.9.0)
  
  [mirai-api-http](https://github.com/project-mirai/mirai-api-http)
# how to use
  1.克隆仓库到本地
  
  2.打开cmd，运行pip install -r requirements.txt
  
  3.修改main.py中的qq,port,key   向下划拉能看到botName变量，改成你bot的名字
  
  3.运行main.py
# 指令如下

  key是你要操作的关键词
  
  **更新词库的方式**
  
  把新的词库文件重命名(格式指定为xlsx)为词库.xlsx,放在Config文件下，运行superDict.py
  
  如果是向已有词库中添加请直接运行superDict.py，希望新建词库详见注释
  
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
