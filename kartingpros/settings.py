import json
import os
JSON_FILE_NAME = "./settings.json"


def getSetting(settingName):
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_image_path = os.path.join(current_path, JSON_FILE_NAME)
    f = open(absolute_image_path)
    data = json.load(f)
    f.close()
    return(data[settingName])


# getMaxForwardSpeed()
