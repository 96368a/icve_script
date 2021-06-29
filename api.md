
# 职教云api分析

### cookies

| 参数名 |   值  |
|  ---  |  --- |
| **auth** | **关键值** |



### 登录接口

> ```https://zjy2.icve.com.cn/api/common/login/login```

有验证码，比较麻烦，暂时不分析了



### 用户信息


#### 请求
> ```https://zjy2.icve.com.cn/api/student/Studio/index```

>  POST 无请求参数

#### 返回

| 参数名 | 参数值 |
| :---: | ----- |
| schoolId| 学校id |
|disPlayName| 姓名 |
| stuNo | 学号|
|schoolId|学校id|
|myCourseCount|加入的课程数量|
|UserName|用户名|
|stuId|学生id|



<style>
	pre.json {
		background: #f5f5f5;
		border-radius: 5px;
		font-family: Menlo,Monaco,Consolas,'Courier New',monospace;
    	font-size: .6em !important;
		padding: 0.6em;
}
</style>
<details>
  <summary>返回数据示例</summary>
<pre class="json">{
	"code" : 1,
	"avator" : "https://file.icve.com.cn/ssykt/279/604/45C972612A5025462C0E9779F4234D17.jpeg?x-oss-process=image/resize,m_fixed,w_110,h_110,limit_0",
	"schoolId" : "bgexaqiob5bhzua0cwitXX",
	"disPlayName" : "张三",
	"stuNo" : "99",
	"UserName" : "这是用户名",
	"statData" : {
		"unReadMsgCount" : 0,
		"faceTeachDayCount" : 0,
		"faceTeachWeekCount" : 0,
		"announcementCount" : 0,
		"myCourseCount" : 3,
		"myHomeworkCount" : 70,
		"myExamCount" : 6,
		"onlineActivityCount" : 0,
		"groupTaskCount" : 0
	},
	"stuId" : "ewuzaw6sikjh4eueok9yXX",
	"extraData" : {
		"IsExtraJXSX" : 0,
		"IsExtraZYJS" : 1,
		"IsExtraJXPJ" : 0,
		"IsExtraEXAM" : 0
	},
	"integrity" : 6,
	"moocServer" : "https://mooc.icve.com.cn",
	"isMerge" : 0,
	"isOpenLite" : "1"
}
</pre>
</details>



### 全部课程获取

#### 请求

> https://zjy2.icve.com.cn/api/student/learning/getLearnningCourseList

>  POST 无请求参数

#### 返回


| 参数名 | 参数值 |
| :---: | ----- |
| Id | 课程id(似乎没啥用) |
|**courseOpenId**| **课程资源id** |
| **openClassId** | **班级id**(猜的) |
|schoolId|学校id|
|courseName|课程名|
|process| 课程进度   |
|UserName|用户名|
|stuId|学生id|

<details>
  <summary>返回数据示例</summary>
<pre class="json">
{
    "code": 1,
    "type": "1",
    "termId": null,
    "courseList": [
        {
            "Id": "r2beartfo5eapb12qujq",
            "courseOpenId": "qra4ahurp4hhmnxeb88lza",
            "courseName": "java面向对象程序设计",
            "courseCode": "10",
            "thumbnail": "https://file.icve.com.cn/ssykt/769/845/C07D3617B6BE0A9DA5A4522DDF285A66.png?x-oss-process=image/resize,m_fixed,w_270,h_180,limit_0",
            "openClassId": "6dwyaaqt0yzlqlr6xhruxq",
            "assistTeacherName": "陈剑英",
            "openClassType": 1,
            "openClassState": 1,
            "process": 0,
            "checkStatus": 0,
            "termName": "2021春",
            "totalScore": 0,
            "courseSystemType": 0
        },
        {
            "Id": "7rznansrfhcg4kunkw",
            "courseOpenId": "oosoavmrha5farnarf7b1g",
            "courseName": "数据结构",
            "courseCode": "",
            "thumbnail": "https://file.icve.com.cn/ssykt/782/871/C38D9ED86F407DEA2C0DDA924B4FB788.jpeg?x-oss-process=image/resize,m_fixed,w_270,h_180,limit_0",
            "openClassId": "gudad2sfjvedmk9jqmkzq",
            "assistTeacherName": "成亚玲",
            "openClassType": 1,
            "openClassState": 1,
            "process": 100,
            "checkStatus": 0,
            "termName": "2021春",
            "totalScore": 0,
            "courseSystemType": 0
        },
        {
            "Id": "jguzaw6sky1ob8xgc16lqg",
            "courseOpenId": "xpxan6qubliezyut5xn7q",
            "courseName": "C语言程序设计",
            "courseCode": "",
            "thumbnail": "https://file.icve.com.cn/ssykt/953/174/EE72B90A3F93BA9D30D99A350CD80A69.jpeg?x-oss-process=image/resize,m_fixed,w_270,h_180,limit_0",
            "openClassId": "lrnvawis4qlbpdcywr7qqq",
            "assistTeacherName": "李健",
            "openClassType": 1,
            "openClassState": 1,
            "process": 100,
            "checkStatus": 1,
            "termName": "2020秋",
            "totalScore": 78.87,
            "courseSystemType": 0
        }
    ],
    "termList": [
        {
            "Id": "mnuzajgsk51li44ptyz4ba",
            "DateCreated": "/Date(1607937528000)/",
            "CreatorId": null,
            "TermCode": "202101",
            "TermName": "2021春",
            "IsCurTerm": true,
            "TermSeason": 1,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "9jzjamir8ybgz0j7oi77a",
            "DateCreated": "/Date(1590587241000)/",
            "CreatorId": null,
            "TermCode": "202002",
            "TermName": "2020秋",
            "IsCurTerm": true,
            "TermSeason": 2,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "upepap2qvyviahtkhtodyw",
            "DateCreated": "/Date(1573035530000)/",
            "CreatorId": null,
            "TermCode": "202001",
            "TermName": "2020春",
            "IsCurTerm": false,
            "TermSeason": 1,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "w0au2qcrti8mwbi19kjg",
            "DateCreated": "/Date(1557861903000)/",
            "CreatorId": null,
            "TermCode": "201902",
            "TermName": "2019秋",
            "IsCurTerm": false,
            "TermSeason": 2,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "yhcalupaztideorljl2ow",
            "DateCreated": "/Date(1545219120000)/",
            "CreatorId": null,
            "TermCode": "201901",
            "TermName": "2019春",
            "IsCurTerm": false,
            "TermSeason": 1,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "qfldaegomjpjnnstepn7pq",
            "DateCreated": "/Date(1526413173000)/",
            "CreatorId": null,
            "TermCode": "201802",
            "TermName": "2018秋",
            "IsCurTerm": false,
            "TermSeason": 2,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "filiafgo5zhlpduxt0vgdg",
            "DateCreated": "/Date(1513950281000)/",
            "CreatorId": null,
            "TermCode": "201801",
            "TermName": "2018春",
            "IsCurTerm": false,
            "TermSeason": 1,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        },
        {
            "Id": "zjezaocnhapfyto2ua9wza",
            "DateCreated": "/Date(1504214637000)/",
            "CreatorId": null,
            "TermCode": "201702",
            "TermName": "2017秋",
            "IsCurTerm": false,
            "TermSeason": 2,
            "IsSynchroUpdate": 0,
            "TableName": "Base_StudyTermInfo"
        }
    ]
}
</pre>
</details>



### 总大纲获取

#### 请求

> https://zjy2.icve.com.cn/api/study/process/getProcessList

>  POST 

|      参数名      |      备注      |
| :--------------: | :------------: |
| **courseOpenId** | **课程资源id** |
| **openClassId**  |   **班级id**   |



#### 返回


| 参数名 | 参数值 |
| :---: | ----- |
|**courseOpenId**| **课程资源id** |
|**openClassId**| **班级id** |
| openCourseCellCount | 课程总节数 |
|stuStudyCourseOpenCellCount|已学习节数|
|moduleList| 小节列表 |
|**id**|**章节id**|
|name|课程名|

<details>
  <summary>返回数据示例</summary>
<pre class="json">
{
    "code": 1,
    "courseOpenId": "qra4ahurp4hhmnxeb88lza",
    "openClassId": "6dwyaaqt0yzlqlr6xhruxq",
    "openCourseCellCount": 412,
    "stuStudyCourseOpenCellCount": 0,
    "progress": {
        "moduleList": [
            {
                "id": "z25ahurhbjekd5kwqqlaa",
                "name": "课程导学",
                "sortOrder": 1,
                "percent": 0
            },
            {
                "id": "z25ahurpibmoxbwebrtg",
                "name": "模块一    初识java及环境搭建",
                "sortOrder": 2,
                "percent": 0
            },
            {
                "id": "z25ahurx61bazyxpbexrg",
                "name": "模块二  走进java世界之语法基础",
                "sortOrder": 3,
                "percent": 0
            },
            {
                "id": "z25ahur7pbgm3ct2u1f8w",
                "name": "模块三  走进java世界之流程控制",
                "sortOrder": 4,
                "percent": 0
            },
            {
                "id": "z25ahur151jcqpjvttxpa",
                "name": "模块四  探知java之面向对象基础",
                "sortOrder": 5,
                "percent": 0
            },
            {
                "id": "z25ahurd4dolopytw7cng",
                "name": "模块五  使用java数组和方法",
                "sortOrder": 6,
                "percent": 0
            },
            {
                "id": "z25ahurekhe6kaj7z6aq",
                "name": "模块六 探知java之面向对象高级",
                "sortOrder": 7,
                "percent": 0
            },
            {
                "id": "z25ahurtyvpfcdojguva",
                "name": "模块七  探究java之异常处理",
                "sortOrder": 8,
                "percent": 0
            },
            {
                "id": "z25ahuri5pdxncltsega",
                "name": "模块八  解读java之常用API",
                "sortOrder": 9,
                "percent": 0
            },
            {
                "id": "ap65ahurb7ffxycu3oezfg",
                "name": "模块九 进阶java高级之文件操作",
                "sortOrder": 10,
                "percent": 0
            },
            {
                "id": "ap65ahurcozfctrfmbhq",
                "name": "模块十  进阶java高级之数据库编程",
                "sortOrder": 11,
                "percent": 0
            },
            {
                "id": "ap65ahurplbfxz5rripg",
                "name": "模块十一  进阶java高级之网络编程",
                "sortOrder": 12,
                "percent": 0
            },
            {
                "id": "vv74amqrkkfgxebxsv90w",
                "name": "单元1 搭建Java开发环境",
                "sortOrder": 13,
                "percent": 0
            },
            {
                "id": "vv74amqrql5iy0aqkmcqg",
                "name": "单元2 Java语言基础",
                "sortOrder": 14,
                "percent": 0
            },
            {
                "id": "vv74amqrtafd5tobu1h9gw",
                "name": "单元3 面向对象程序设计",
                "sortOrder": 15,
                "percent": 0
            },
            {
                "id": "vv74amqry4bedk9mmaruw",
                "name": "单元4 继承与多态",
                "sortOrder": 16,
                "percent": 0
            },
            {
                "id": "vv74amqruypmmk8qgundya",
                "name": "单元5 集合容器",
                "sortOrder": 17,
                "percent": 0
            },
            {
                "id": "vv74amqrdpdhohe9w18cma",
                "name": "单元6 图形用户界面设计",
                "sortOrder": 18,
                "percent": 0
            },
            {
                "id": "vv74amqre6paohw6lv40cq",
                "name": "单元7 JDBC",
                "sortOrder": 19,
                "percent": 0
            },
            {
                "id": "vv74amqryavmddbtjpftq",
                "name": "单元8 输入输出流与多线程",
                "sortOrder": 20,
                "percent": 0
            }
        ],
        "moduleId": "z25ahurhbjekd5kwqqlaa"
    }
}
</pre>
</details>
### 大纲章节获取

#### 请求

> https://zjy2.icve.com.cn/api/study/process/getTopicByModuleId

>  POST 

|      参数名      |      备注      |
| :--------------: | :------------: |
| **courseOpenId** | **课程资源id** |
|   **moduleId**   |  **大章节id**  |



#### 返回


| 参数名 | 参数值 |
| :---: | ----- |
|courseOpenId| 课程资源id |
|openClassId| 班级id |
| openCourseCellCount | 课程总节数 |
|stuStudyCourseOpenCellCount|已学习节数|
|moduleList| 小节列表 |
|**id**|**章节id**|
|name|课程名|

<details>
  <summary>返回数据示例</summary>
<pre class="json">
{
    "code": 1,{
    "code": 1,
    "topicList": [
        {
            "id": "z25ahurz6noxcwpudd8w",
            "name": "课程介绍",
            "sortOrder": 1,
            "upTopicId": "0"
        },
        {
            "id": "z25ahurjbrgzkgmyg2dg",
            "name": "课程前导",
            "sortOrder": 2,
            "upTopicId": "z25ahurz6noxcwpudd8w"
        },
        {
            "id": "z25ahurpkhfd0kcx1p2q",
            "name": "授课日历计划",
            "sortOrder": 3,
            "upTopicId": "z25ahurjbrgzkgmyg2dg"
        },
        {
            "id": "z25ahur6rlwuqnbhhhta",
            "name": "课程标准",
            "sortOrder": 4,
            "upTopicId": "z25ahurpkhfd0kcx1p2q"
        },
        {
            "id": "z25ahurviph73nioiunga",
            "name": "课程整体设计与考核要求",
            "sortOrder": 5,
            "upTopicId": "z25ahur6rlwuqnbhhhta"
        },
        {
            "id": "z25ahuryxobrfowmamq",
            "name": "岗位技能和学习方法",
            "sortOrder": 6,
            "upTopicId": "z25ahurviph73nioiunga"
        }
    ]
}
    "courseOpenId": "qra4ahurp4hhmnxeb88lza",
    "openClassId": "6dwyaaqt0yzlqlr6xhruxq",
    "openCourseCellCount": 412,
    "stuStudyCourseOpenCellCount": 0,
    "progress": {
        "moduleList": [
            {
                "id": "z25ahurhbjekd5kwqqlaa",
                "name": "课程导学",
                "sortOrder": 1,
                "percent": 0
            },
            {
                "id": "z25ahurpibmoxbwebrtg",
                "name": "模块一    初识java及环境搭建",
                "sortOrder": 2,
                "percent": 0
            },
            {
                "id": "z25ahurx61bazyxpbexrg",
                "name": "模块二  走进java世界之语法基础",
                "sortOrder": 3,
                "percent": 0
            },
            {
                "id": "z25ahur7pbgm3ct2u1f8w",
                "name": "模块三  走进java世界之流程控制",
                "sortOrder": 4,
                "percent": 0
            },
            {
                "id": "z25ahur151jcqpjvttxpa",
                "name": "模块四  探知java之面向对象基础",
                "sortOrder": 5,
                "percent": 0
            },
            {
                "id": "z25ahurd4dolopytw7cng",
                "name": "模块五  使用java数组和方法",
                "sortOrder": 6,
                "percent": 0
            },
            {
                "id": "z25ahurekhe6kaj7z6aq",
                "name": "模块六 探知java之面向对象高级",
                "sortOrder": 7,
                "percent": 0
            },
            {
                "id": "z25ahurtyvpfcdojguva",
                "name": "模块七  探究java之异常处理",
                "sortOrder": 8,
                "percent": 0
            },
            {
                "id": "z25ahuri5pdxncltsega",
                "name": "模块八  解读java之常用API",
                "sortOrder": 9,
                "percent": 0
            },
            {
                "id": "ap65ahurb7ffxycu3oezfg",
                "name": "模块九 进阶java高级之文件操作",
                "sortOrder": 10,
                "percent": 0
            },
            {
                "id": "ap65ahurcozfctrfmbhq",
                "name": "模块十  进阶java高级之数据库编程",
                "sortOrder": 11,
                "percent": 0
            },
            {
                "id": "ap65ahurplbfxz5rripg",
                "name": "模块十一  进阶java高级之网络编程",
                "sortOrder": 12,
                "percent": 0
            },
            {
                "id": "vv74amqrkkfgxebxsv90w",
                "name": "单元1 搭建Java开发环境",
                "sortOrder": 13,
                "percent": 0
            },
            {
                "id": "vv74amqrql5iy0aqkmcqg",
                "name": "单元2 Java语言基础",
                "sortOrder": 14,
                "percent": 0
            },
            {
                "id": "vv74amqrtafd5tobu1h9gw",
                "name": "单元3 面向对象程序设计",
                "sortOrder": 15,
                "percent": 0
            },
            {
                "id": "vv74amqry4bedk9mmaruw",
                "name": "单元4 继承与多态",
                "sortOrder": 16,
                "percent": 0
            },
            {
                "id": "vv74amqruypmmk8qgundya",
                "name": "单元5 集合容器",
                "sortOrder": 17,
                "percent": 0
            },
            {
                "id": "vv74amqrdpdhohe9w18cma",
                "name": "单元6 图形用户界面设计",
                "sortOrder": 18,
                "percent": 0
            },
            {
                "id": "vv74amqre6paohw6lv40cq",
                "name": "单元7 JDBC",
                "sortOrder": 19,
                "percent": 0
            },
            {
                "id": "vv74amqryavmddbtjpftq",
                "name": "单元8 输入输出流与多线程",
                "sortOrder": 20,
                "percent": 0
            }
        ],
        "moduleId": "z25ahurhbjekd5kwqqlaa"
    }
}
</pre>
</details>


### 章节小节信息获取

#### 请求

> https://zjy2.icve.com.cn/api/study/process/getCellByTopicId

>  POST 

|      参数名      |      备注      |
| :--------------: | :------------: |
| **courseOpenId** | **课程资源id** |
| **openClassId**  |   **班级id**   |
|   **topicId**    |   **小节id**   |



#### 返回


| 参数名 | 参数值 |
| :---: | ----- |
|courseOpenId| 课程资源id |
|openClassId| 班级id |
| cellList | 小节列表 |
|**Id**|**小节Id**|
|parentId|不知道啥id|
|topicId| 章节id |
|cellName|小节名|
|categoryName|小节类型|
|upCellId|不知道啥id|
|stuCellCount|学习数|
|stuCellPercent|学习进度|
|cellType|某种类型，1代表最小一级节点|
|childNodeList|子节点列表（结合cellType判断）|

注意！！ 有些小节点里还存在子节点，可根据cellType判断

<details>
  <summary>返回数据示例</summary>
<pre class="json">
{
    "code": 1,
    "courseOpenId": "qra4ahurp4hhmnxeb88lza",
    "openClassId": "6dwyaaqt0yzlqlr6xhruxq",
    "cellList": [
        {
            "Id": "z25ahursjdgphgqiku97w",
            "cellType": 1,
            "isGJS": 1,
            "isOriginal": 0,
            "fromType": 10,
            "parentId": "z25ahurz6noxcwpudd8w",
            "courseOpenId": "qra4ahurp4hhmnxeb88lza",
            "topicId": "z25ahurz6noxcwpudd8w",
            "categoryName": "文档",
            "categoryNameDb": "文档",
            "cellName": "课程介绍",
            "resourceUrl": "doc/g@57306E3DF9E5268924059C1338EA4004.docx",
            "externalLinkUrl": "",
            "cellContent": "doc/g@57306E3DF9E5268924059C1338EA4004.docx",
            "sortOrder": 1,
            "isAllowDownLoad": false,
            "childNodeList": [
            ],
            "upCellId": "0",
            "stuCellCount": 0,
            "stuCellPercent": 0
        },
        {
            "Id": "z25ahur6fcktlnbxekya",
            "cellType": 1,
            "isGJS": 0,
            "isOriginal": 1,
            "fromType": 10,
            "parentId": "z25ahurz6noxcwpudd8w",
            "courseOpenId": "qra4ahurp4hhmnxeb88lza",
            "topicId": "z25ahurz6noxcwpudd8w",
            "categoryName": "视频",
            "categoryNameDb": "视频",
            "cellName": "《JAVA面向对象程序设计》课程介绍",
            "resourceUrl": "ssykt/g@299B813EADE5F5A081F1D1D256E53494.mp4",
            "externalLinkUrl": "",
            "cellContent": "",
            "sortOrder": 2,
            "isAllowDownLoad": false,
            "childNodeList": [
            ],
            "upCellId": "z25ahursjdgphgqiku97w",
            "stuCellCount": 0,
            "stuCellPercent": 0
        }
    ]
}
</pre>
</details>


### 小节详细信息获取

#### 请求

> https://zjy2.icve.com.cn/api/common/Directory/viewDirectory

>  POST 

|      参数名      |      备注      |
| :--------------: | :------------: |
| **courseOpenId** | **课程资源id** |
| **openClassId**  |   **班级id**   |
|    **cellId**    |   **小节id**   |
|     moduleId     |  章节id(可选)  |



#### 返回


| 参数名 | 参数值 |
| :---: | :---: |
| code | 成功返回1，错误时返回-100 |
|**Id**|**小节Id**|
| guIdToken | 提交要用的token，每次请求会改变 |
|           |                                 |

此处错误返回为前一个进度未保存，请求下面的进度接口即可

<details>
  <summary>错误返回数据示例</summary>
<pre class="json">
{
    "code": -100,
    "currCourseOpenId": "qra4ahurp4hhmnxeb88lza",
    "currOpenClassId": "6dwyaaqt0yzlqlr6xhruxq",
    "currModuleId": "z25ahurhbjekd5kwqqlaa",
    "curCellId": "z25ahursjdgphgqiku97w",
    "currCellName": "课程介绍",
    "currPercent": 100,
    "lastCourseOpenId": "qra4ahurp4hhmnxeb88lza",
    "lastOpenClassId": "6dwyaaqt0yzlqlr6xhruxq",
    "lastModuleId": "z25ahurhbjekd5kwqqlaa",
    "lastCellId": "z25ahur6fcktlnbxekya",
    "lastCellName": "《JAVA面向对象程序设计》课程介绍",
    "lastPercent": 0
}
</pre>
</details>
<details>
  <summary>正确返回数据示例</summary>
<pre class="json">
{
    "code": 1,
    "dtype": 0,
    "courseOpenId": "qra4ahurp4hhmnxeb88lza",
    "courseName": "java面向对象程序设计",
    "openClassId": "6dwyaaqt0yzlqlr6xhruxq",
    "moduleId": "z25ahurhbjekd5kwqqlaa",
    "topicId": "z25ahurz6noxcwpudd8w",
    "cellId": "z25ahursjdgphgqiku97w",
    "cellName": "课程介绍",
    "cellType": 1,
    "categoryName": "文档",
    "cellContent": "doc/g@57306E3DF9E5268924059C1338EA4004.docx",
    "pageCount": 2,
    "audioVideoLong": 2,
    "isAllowDownLoad": false,
    "externalLinkUrl": "",
    "downLoadUrl": "https://file.icve.com.cn/file_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx?response-content-disposition=attachment;filename=课程介绍.docx",
    "cellLogId": "",
    "userType": 1,
    "resUrl": "{\"extension\":\"docx\",\"category\":\"office\",\"urls\":{\"status\":\"https://upload.icve.com.cn/doc/g@57306E3DF9E5268924059C1338EA4004.docx/status?time=637559296432298481&token=3F55084615B7F01A366178F5B65E47F7\",\"preview\":\"https://file.icve.com.cn/file_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx\",\"download\":\"https://file.icve.com.cn/file_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx?response-content-disposition=attachment;filename=课程介绍.docx\",\"preview_oss_ori\":\"https://file.icve.com.cn/file_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx\",\"oss_ori_internal_url\":\"https://icve.oss-cn-hangzhou-internal.aliyuncs.com/file_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx\",\"preview_oss_gen\":\"https://file.icve.com.cn/file_gen_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx\",\"oss_gen_internal_url\":\"https://icve.oss-cn-hangzhou-internal.aliyuncs.com/file_gen_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx\",\"owa_url\":\"https://ppt2.icve.com.cn/op/view.aspx?src=https://icve.oss-cn-hangzhou-internal.aliyuncs.com/file_doc/348/27/57306E3DF9E5268924059C1338EA4004.docx\"},\"args\":{\"page_count\":2},\"h5PreviewUrl\":\"\",\"isH5\":0,\"status\":2}",
    "isDownLoad": false,
    "rarList": [],
    "flag": null,
    "stuCellViewTime": 200,
    "stuCellPicCount": 1,
    "stuStudyNewlyTime": 0,
    "stuStudyNewlyPicCount": 1,
    "cellPercent": 50,
    "guIdToken": "qxxrasctklfl0muzrvegq",
    "isNeedUpdate": 0,
    "position": 0,
    "cellPositions": [],
    "cellQuestionList": ""
}
</pre>
</details>
### 进度选择

#### 请求

> https://zjy2.icve.com.cn/api/common/Directory/changeStuStudyProcessCellData

>  POST 

|      参数名      |      备注      |
| :--------------: | :------------: |
| **courseOpenId** | **课程资源id** |
| **openClassId**  |   **班级id**   |
|    **cellId**    |   **小节id**   |
|   **cellName**   |   **小节名**   |
|     moduleId     |  章节id(可选)  |



#### 返回


| 参数名 |          参数值           |
| :----: | :-----------------------: |
|  code  | 成功返回1，错误时返回-500 |

<details>
  <summary>正确返回数据示例</summary>
<pre class="json">
{"code":1}
</pre>
</details>



### 文档/视频进度更新

#### 请求

> https://zjy2.icve.com.cn/api/common/Directory/stuProcessCellLog

>  POST 

|        参数名        |             备注             |
| :------------------: | :--------------------------: |
|   **courseOpenId**   |        **课程资源id**        |
|   **openClassId**    |          **班级id**          |
|      **cellId**      |          **小节id**          |
|      **picNum**      |           **页码**           |
|  **studyNewlyTime**  | **视频秒数**（提交视频时用） |
| **studyNewlyPicNum** |   **文档页码**（文档时用）   |
|      **token**       |   **上个请求返回的token**    |

>  **备注：**

studyNewlyTime和studyNewlyPicNum参数二选一即可，看当前是文档还是视频



#### 返回


| 参数名 | 参数值 |
| :---: | :---: |
| code | 成功返回1，错误时返回-100 |
|**Id**|**小节Id**|
| guIdToken | 提交要用的token，每次请求会改变 |
|           |                                 |

<details>
  <summary>返回数据示例</summary>
<pre class="json">
{"code":1,"msg":"操作成功！"}
</pre>
</details>


