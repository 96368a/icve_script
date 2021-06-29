import requests
import json

cookies = r"01022D9D4AE9023AD908FE2DADF6BA563AD90801166500770075007A00610077003600730069006B006A00680034006500750065006F006B00390079007700710000012F00FFEC0E3ABE0668DC583DE683037815FD360390873A"

userInfoUrl = r"https://zjy2.icve.com.cn/api/student/Studio/index"
allCourseListUrl = r"https://zjy2.icve.com.cn/api/student/learning/getLearnningCourseList"
processListUrl = r"https://zjy2.icve.com.cn/api/study/process/getProcessList"
topicByModuleIdUrl = r"https://zjy2.icve.com.cn/api/study/process/getTopicByModuleId"
cellByTopicIdUrl = r"https://zjy2.icve.com.cn/api/study/process/getCellByTopicId"
viewDirectoryUrl = r"https://zjy2.icve.com.cn/api/common/Directory/viewDirectory"
stuProcessCellLogUrl = r"https://zjy2.icve.com.cn/api/common/Directory/stuProcessCellLog"
changeProcessUrl = r"https://zjy2.icve.com.cn/api/common/Directory/changeStuStudyProcessCellData"


def _Post(url, data={}):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'cookie': "auth=%s;" % cookies
    }
    return requests.post(url, headers=header, data=data).json()


def getUserInfo():
    return _Post(userInfoUrl)


def getAllCourseList():
    return _Post(allCourseListUrl)


def getProcessList(courseOpenId, openClassId):
    data = {
        "courseOpenId": courseOpenId,
        "openClassId": openClassId
    }
    return _Post(processListUrl, data)


def getTopicByModuleId(courseOpenId, moduleId):
    data = {
        "courseOpenId": courseOpenId,
        "moduleId": moduleId
    }
    return _Post(topicByModuleIdUrl, data)


def getCellByTopicId(courseOpenId, openClassId, topicId):
    data = {
        "courseOpenId": courseOpenId,
        "openClassId": openClassId,
        "topicId": topicId
    }
    return _Post(cellByTopicIdUrl, data)


def getViewDirectory(courseOpenId, openClassId, cellId, moduleId=None):
    data = {
        "courseOpenId": courseOpenId,
        "openClassId": openClassId,
        "cellId": cellId
    }
    if(moduleId != None):
        data["moduleId"] = moduleId
    return _Post(viewDirectoryUrl, data)


def UpdateStuProcess(courseOpenId, openClassId, cellId, picNum, newStudy, token, type=1):
    # type表示类型,1为文档,2为视频
    data = {
        "courseOpenId": courseOpenId,
        "openClassId": openClassId,
        "cellId": cellId,
        "picNum": picNum,
        "token": token
    }
    if type == 1:
        data["studyNewlyPicNum"] = newStudy
    elif type == 2:
        data["studyNewlyTime"] = newStudy
    return _Post(stuProcessCellLogUrl, data)


def changeProcessCell(courseOpenId, openClassId, cellId, cellName, moduleId=None):
    data = {
        "courseOpenId": courseOpenId,
        "openClassId": openClassId,
        "cellId": cellId,
        "cellName": cellName
    }
    if(moduleId != None):
        data["moduleId"] = moduleId
    return _Post(changeProcessUrl, data)


def Analysis_Course(courseOpenId, openClassId):
    # 大纲获取
    processList = getProcessList(courseOpenId, openClassId)
    processList["totalCourses"] = []
    moduleList = processList["progress"]["moduleList"]
    # moduleList["courseOpenId"]=courseOpenId
    # moduleList["openClassId"]=openClassId
    # 遍历每个获取章节
    print("开始分析课程..")
    for i, v in enumerate(processList["progress"]["moduleList"]):
        print("%d. %s"%(i+1,v["name"]))
        topicList = getTopicByModuleId(courseOpenId, v["id"])
        topicList = topicList["topicList"]
        # 遍历章节获取小节
        for n, m in enumerate(topicList):
            print("  %d.%d %s"%(i+1,n+1,m["name"]))
            cellList = getCellByTopicId(courseOpenId, openClassId, m["id"])
            # topicList[n]["cellList"] = cellList["cellList"]
            for nodenNum,childNode in enumerate(cellList["cellList"]):
                print("    %d.%d.%d %s - %s"%(i+1,n+1,nodenNum+1,childNode["cellName"],childNode["categoryName"]))
                if childNode["cellType"]==1:
                    processList["totalCourses"] += [childNode]
                else:
                    #存在子节点
                    processList["totalCourses"] += childNode["childNodeList"]
        # processList["progress"]["moduleList"][i]["topicList"] = topicList
    del processList["progress"]
    return processList


def saveJson(filename, jsonData):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(jsonData, f, indent=4, ensure_ascii=False)
