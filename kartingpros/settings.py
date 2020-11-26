import json
JSON_FILE_NAME = r"kartingpros/settings.json"


def getMaxForwardSpeed():
    f = open(JSON_FILE_NAME)
    data = json.load(f)
    print(data["max_forward_speed"])
    f.close()


def getSetting(settingName):
    f = open(JSON_FILE_NAME)
    data = json.load(f)
    f.close()
    return(data[settingName])


# getMaxForwardSpeed()
