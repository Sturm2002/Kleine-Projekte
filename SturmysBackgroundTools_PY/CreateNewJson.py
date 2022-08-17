import json,os
jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
JsonDict = {
    "General":{
        "Settings":{
            "KeyGrabberNormalOn": False,
            "NetCheckNormalOn": True,
            "NFCReaderNormalOn": False,
            "DiscordBotNormalOn": True,
            "NotificationEnable": True,
            "NotificationDuration": 5,
            "SherlockTimeout" : 5,
            "SherlockOutputFile" : "/sherlockOutput/sherlock_*.txt"
        }
    },
    "NFCReader":{
        "Settings":{
            "ComPort": "COM3"
        }
    },
    "KeyGrabber":{
        "Settings":{
            "OutputFileName" : "/KeyLogs/KeyGrabber*.txt",
            "NoWriteDuration": 5
        }
    },
    "DiscordBot":{
        "Settings":{
            "SecretToken": "SECRETTOKEN"
        }
    },
    "NetCheck": {
        "Settings":{
            "RunInterval": 5,
            "ToastFormat": "<NAME> STATUS\n",
            "ConFormat": "CustomName | status | ip | name | mac | LastCon\n",
            "FritzBoxIP":"192.168.10.1",
            "FritzBoxPW":"PW"
            
        },
        "KnownDevices": [
            
        ],
        "CurrentDevices": {

        }

    }
}

JsonFile = open(jsonpath,"w+")
JsonFile.write(json.dumps(JsonDict,indent=4))
JsonFile.close()