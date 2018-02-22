
# MinDa_News
A small flask app

# Getting started
## First Base config
1. run the following  command to clone this project to local

 `git clone git@github.com:zhoujunjiang/MinDa_news.git`

2. create a virtual environment such as `virtualenv` and start it
3. in the venv run the following command to install this project needed library

    `pip install requirments`

4. open folder `news_spider`
    - modify the create_db.py cahnge the `db username` and `db passowrd` with your own config
    - modify the news_spider.py as above shown

5. modify the config.py as above shown or set it from the environ

## Second running

when finish above configuration now we can run this project

1. run `news_spider.py` to spider the data from [scmzu important news](http://news.scuec.edu.cn/?cat)
    wait a few times until the spider running finish
2. runing `manage.py`
    - windows  `python manage.py runserver`
    - *unix `./manage.py`
3. open the browser type `127.0.0.1:5000` to run when you see the `Congratulation,you are running success!` on the screen means the project running successful

>Tips: All the operation must in the virtual envirment

## NEWS API

1. news list will return a list
    >url http:127.0.0.1/news/api/list/pages

method `get`


`request param`

| param        | type   |  defualt  |example |must | describe |
| :--------:  | :-----:  | :----:  |:---:|:---:|:---:|
| pages| int|null|http:127.0.0.1/news/api/list/1|y|news list|

`response param`  is a json type
    
| key        | type   |  examplevalue   | describe |
| :--------:  | :-----:  | :----:  |:---:|
| code        |     int| 200      | request success|
|msg        | String|request success|request success|
|content|json list||content list|

` return instance`

```json
{
    "code": 200,
    "msg": "request success",
    "content": [
        {
            "content_id": 6239,
            "news_preview": "4月15日是全民国家安全教育日，根据国家民委办公厅、湖北省教育厅等相关文件和通知精神，学校精心部署、全面开展全民国家安全教育日“十个一”系列活动，即组织一次校党 ",
            "news_push_time": "2017.04.21",
            "news_title": "学校开展全民国家安全教育日系列活动",
            "original_url": "http://news.scuec.edu.cn/?p=6239"
        }
    ]
}
```



2. news content will return a news content
 >url http:127.0.0.1/news/api/content/content_id

method `get`

`request param`

| param        | type   |  defualt  |example |must | describe |
| :--------:  | :-----:  | :----:  |:---:|:---:|:---:|
| content_id| int|null|http:127.0.0.1/news/api/content/6239|y|news content|


`response param`  is a json type

| key        | type   |  examplevalue   | describe |
| :--------:  | :-----:  | :----:  |:---:|
| code        |     int| 200      | request success|
|msg        | String|request success|request success|
|content|String| |content |


`return instance`

```json
{
    "code": 200,
    "content": "<div class=\\\"left-content\\\">\\n<div class=\\\"single-header\\\">\\n<h2>我校学生团队荣获国际企业管理挑战赛中国赛区一等奖</h2>\\n<h3></h3>\\n<p><span class=\\\"s-time\\\">2017-03-27    11:12:14</span>\\n<span class=\\\"s-author\\\">    作者：潘文捷 董银红</span>\\n<span class=\\\"s-view\\\">    阅读量：1,202</span></p>\\n</div>\\n<div class=\\\"single-content\\\">\\n<p>近日，国际企业管理挑战赛组委会发来喜讯，由我校学生组成的“浪里个浪”团队在第37届艾迪国际杯国际企业管理挑战赛(Global Management Challenge，简称GMC)中国赛区比赛中表现优异，获得一等奖。</p>\\n<p>GMC是起源于欧洲的全球最大规模的企业管理比赛，被誉为企业管理模拟的奥林匹克大赛。GMC比赛以管理决策为核心，涉及企业发展战略、生产、研发、营销、人力资源、投资及财务等方面，通过最大限度地模拟公司在市场经济条件下的真实运作状况，为同学们培养和加强统观全局、系统思考、正确决策、灵活应变的能力提供了平台。2016年度GMC中国赛区共有来自全国150多所高校的近2000支队伍参赛，经过初赛、复赛、半决赛的层层选拔，历时四个月，最终有16支代表队在全国决赛（分为准决赛、总决赛）中进行了巅峰对决。</p>\\n<p>我校对该赛事高度重视，创新创业学院、管理学院通过线上和线下渠道进行宣传，组织全校学生统一报名，并为参赛队伍提供专业培训，营造了良好的参赛氛围。我校师生表现出极大热情，全校共有60支团队参加了该项赛事，其中29支队伍拿到复赛参赛权，最终有5支队伍进入半决赛，1支队伍闯进全国总决赛。我校“浪里个浪”学生团队在管理学院张秋来、董银红两位老师的指导下荣获全国一等奖，这也是我校在该项赛事中第二次获得全国一等奖。</p>\\n<p style=\\\"text-align: right;\\\">（编辑：杨征  来源：创新创业学院）</p>\\n<div class=\\\"thumbnail\\\"></div>\\n</div>\\n</div>",
    "msg": "request success"
}
```

## END
