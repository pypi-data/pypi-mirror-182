import os
import requests, json
from starsaiot_monit.logger import logger
from os import path

class Conf:
    def __init__(self):
        logger.info("Conf init ..")

        self._conf_dir = os.path.join(os.getcwd(), path.dirname(path.abspath(__file__)) + "/config")
        self._monitJson = self.setMonitJson()
        # self.dynamicRegister()

    def setMonitJson(self):
        filePath = (self._conf_dir + '/monit.json').replace('/', path.sep)
        if not os.path.exists(filePath):
            file = open(filePath, mode='w')
            file.write('{"deviceId": ""}')
            file.close()
            return {}
        with open(filePath, 'r', encoding='utf-8') as f:
            return json.loads(f.read())

    def getMonitJson(self):
        filePath = (self._conf_dir + '/monit.json').replace('/', path.sep)
        if self._monitJson == {}:
            with open(filePath, 'r', encoding='utf-8') as f:
                return json.loads(f.read())
        return self._monitJson

    def dynamicRegister(self):
        url = 'http://device.starsaiot.com:9600/hercules/open/api/v1/device/monitor/dynamicRegister'
        data = json.dumps({
            'deviceSn': '20221210',
            'deviceName': '20221210test',
            'runFirewareVersion': '0.1.0',
            'devModel': '1',
            'runAppVersionCode': '1',
            'runAppVersionName': '0.1.0',
        })
        # 设置请求头
        headers = {"content-type": "application/json"}
        response = requests.post(url, data, headers = headers)
        text = json.loads(response.text)
        logger.info(text)
        if(response.status_code == 200 and text['success']):
            self._monitJson['deviceId'] = text['content']['deviceId']
            self._monitJson['deviceToken'] = text['content']['deviceToken']
            with open((self._conf_dir + '/monit.json').replace('/', os.path.sep), 'w', encoding='utf-8') as f:
                f.write(json.dumps(self._monitJson))

monitJson = Conf()