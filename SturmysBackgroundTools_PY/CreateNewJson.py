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
            "SecretToken": "NzgzMzY2MzAwMzY1MDk1MDAy.GnLuEv.KNnZ39lOFH726WPSSJOn1_2a2qd4SN8qFXCbkU"
        }
    },
    "NetCheck": {
        "Settings":{
            "RunInterval": 5,
            "ToastFormat": "<NAME> STATUS\n",
            "ConFormat": "CustomName | status | ip | name | mac | LastCon\n",
            "FritzBoxIP":"192.168.10.1",
            "FritzBoxPW":"Master0909"
            
        },
        "KnownDevices": [
            ["Mama Android 122", "192.168.10.122"],
            ["Papa A51 136", "192.168.10.136"],
            ["Papa J6 29","192.168.10.29"],
            ["Alex Android 157", "192.168.10.157"],
            ["Wlada Iphone 99", "192.168.10.99"],
            ["Alessio Iphone 87", "192.168.10.87"],
            ["Vlad Iphone 174", "192.168.10.174"],
            ["Maurice Android 53", "192.168.10.53"],
            ["Theo Android 183", "192.168.10.183"],
            ["Yasemin Iphone 43", "192.168.10.43"],
            ["Anna Android 54", "192.168.10.54"],
            ["Mateja Iphone 169", "192.168.10.169"],
            ["Rene Handy 186", "192.168.10.186"],
            ["Amin Android 121","192.168.10.121"],
            ["Isaak Android 123?","192.168.10.123"]
        ],
        "CurrentDevices": {

        }

    }
}

JsonFile = open(jsonpath,"w+")
JsonFile.write(json.dumps(JsonDict,indent=4))
JsonFile.close()