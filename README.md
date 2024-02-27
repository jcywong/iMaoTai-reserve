
# i茅台预约工具----青龙版
fork  https://github.com/397179459/iMaoTai-reserve
修改适配青龙平台


## 原理：
```shell
1、登录获取验证码
2、输入验证码获取TOKEN
3、获取当日SESSION ID
4、根据配置文件预约CONFIG文件中，所在城市的i茅台商品
```


## 使用方法：
### 本地运行
#### 1、下载项目
```shell
git clone https://github.com/397179459/iMaoTai-reserve.git
```


#### 2、安装依赖
```shell
pip3 install --no-cache-dir -r requirements.txt
```

### 3、修改config.py，按照你的需求修改相关配置，这里很重要，建议每个配置项都详细阅读。
1. 去配置环境变量 `GAODE_KEY`

### 4、按提示输入 预约位置、手机号、验证码 等，生成的token等。很长时间不再需要登录。支持多账号。
1. 运行`login.py`
```shell
python3 login.py
# 都选择完之后可以去./myConfig/credentials中查看
```
2. 获取”复制以下内容，以备后续使用“后的内容，去青龙平台添加环境变量`mao_user`，值为刚才复制的内容。
3. 继续添加账号


### 青龙平台
1. 添加订阅
```shell
ql repo https://github.com/jcywong/iMaoTai-reserve.git
```
2. 依赖管理中选择python3 安装依赖pycryptodome
3. 青龙平台添加环境变量`mao_user`，值为本地生成的内容**（内容需要去掉回车）**

4. 保留main任务，删除其他任务，并修改main任务的定时规则为 `0 50 9 * * *`
