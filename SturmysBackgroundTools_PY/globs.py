import os,json,copy



def NotiOff():
    jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
    jsonfile = open(jsonpath)
    jsonvals = json.load(jsonfile)
    outjson = copy.deepcopy(jsonvals)
    outjson["General"]["Settings"]["NotificationEnable"] = False
    with open(jsonpath, "w") as outfile:
            outfile.write(json.dumps(outjson,indent=4))
            outfile.close()

def NotiOn():
    jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
    jsonfile = open(jsonpath)
    jsonvals = json.load(jsonfile)
    outjson = copy.deepcopy(jsonvals)
    outjson["General"]["Settings"]["NotificationEnable"] = True
    with open(jsonpath, "w") as outfile:
            outfile.write(json.dumps(outjson,indent=4))
            outfile.close()