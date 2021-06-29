import API
import traceback
import os
import json
import time
import random

API.cookies = r""
try:
    info = API.getUserInfo()
    if info["UserName"]:
        print("登录成功\n")
        print("+++准备获取课程+++\n")
    print(1)
except:
    traceback.print_exc()
    print("\n出现错误,请检查网络!!")
    exit(0)

# 获取课程
try:
    courseList = []
    if(os.path.exists("courseList.json")):
        with open("courseList.json", "r", encoding="utf-8") as f:
            courseList = json.load(f)
    else:
        courseList = API.getAllCourseList()
        courseList = courseList["courseList"]
        with open("courseList.json", "w+", encoding="utf-8") as f:
            json.dump(courseList, f, indent=4, ensure_ascii=False)
    print("获取到%d门课程\n" % len(courseList))
    print("分别是")
    for i, j in enumerate(courseList):
        print("%d.%s" % (i+1, j["courseName"]))
except:
    traceback.print_exc()

# 获取课程
try:
    ProcessList = {}
    if(os.path.exists("%s.json" % courseList[0]["courseName"])):
        with open("%s.json" % courseList[0]["courseName"], "r", encoding="utf-8") as f:
            ProcessList = json.load(f)
        print("233")
    else:
        ProcessList = API.Analysis_Course(
            courseList[0]["courseOpenId"], courseList[0]["openClassId"])
        API.saveJson("%s.json" % courseList[0]["courseName"], ProcessList)
        # with open("%s.json" % courseList[0]["courseName"], "w", encoding="utf-8") as f:
        #     json.dump(ProcessList, f, indent=4, ensure_ascii=False)
    print("课程读取完毕")
except:
    traceback.print_exc()

# 准备开始
try:
    courseOpenId = ProcessList["courseOpenId"]
    openClassId = ProcessList["openClassId"]
    for i, j in enumerate(ProcessList["totalCourses"]):
        #小节的信息，包含token
        cellInfo = API.getViewDirectory(courseOpenId, openClassId, j["Id"])
        #存在进度选择问题
        if (cellInfo["code"] == -100):
            print("选择进度..")
            result = API.changeProcessCell(
                courseOpenId, openClassId, j["Id"], j["cellName"])
            if result["code"] == 1:
                print("选择%s成功" % j["cellName"])
                cellInfo = API.getViewDirectory(courseOpenId, openClassId, j["Id"])
            else:
                print("选择失败")        
        if(cellInfo["code"] == 1):
            if cellInfo["cellPercent"] != 100:
                if cellInfo["pageCount"] == 0:
                    # 视频类型
                    print("%d. %s - %s "%(i,cellInfo["cellName"], cellInfo["categoryName"]))
                    countProgress = cellInfo["audioVideoLong"]
                    newProgress = cellInfo["stuStudyNewlyTime"]
                    print("当前进度%.2f" % cellInfo["cellPercent"])
                    while newProgress < countProgress:
                        newProgress += 10
                        if newProgress > countProgress:
                            newProgress = countProgress
                        time.sleep(8)
                        result = API.UpdateStuProcess(
                            courseOpenId, openClassId, j["Id"], 0, newProgress, cellInfo["guIdToken"], 2)
                        if result["code"] == 1:
                            print("进度%.2f" % (newProgress/countProgress*100))
                        else:
                            print("操作失败")
                else:
                    # 文档类型
                    print("%d. %s - %s "%(i,cellInfo["cellName"], cellInfo["categoryName"]))
                    countProgress = cellInfo["pageCount"]
                    for newProgress in range(int(cellInfo["cellPercent"]/100*cellInfo["pageCount"]),countProgress):
                        time.sleep(random.randint(3, 6))
                        result = API.UpdateStuProcess(
                            courseOpenId, openClassId, j["Id"], newProgress+1,newProgress+1, cellInfo["guIdToken"], 1)
                        if result["code"] == 1:
                            print("进度%.2f" % ((newProgress+1)/countProgress*100))
                        else:
                            print("操作失败")
            else:
                print("%d. %s - %s  已完成" %
                        (i,cellInfo["cellName"], cellInfo["categoryName"]))
        else:
            print("进度出错")

except:
    traceback.print_exc()
