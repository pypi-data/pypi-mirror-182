
import requests
from pandas import json_normalize
import time
import numpy as np
from metrics import load_metrics
from rich.console import Console

console = Console()


class flowsheet:
    def __init__(self, name=''):
        self.name = name

    def load_metrics():
        return load_metrics()


class sensor:
    def __init__(self, name=''):
        self.name = name
        self.samples = None
        self.index = 0
        self.device_id = None
        self.sensor_name = None
        self.sensor_value = None
        self.sensor_unit = '°F'
        self.sleep_seconds = 0.5

    def _sendSensorData(self, name, value, device_id):
        # sensor place holder
        sensor_name = name
        sensor_value = value
        sensor_id = 'device6ef0e2a6f88f481ea81e388d8be91a1c'

        # request parameters
        base_url = 'https://connect.forge-api.com'
        body = {
            "sensor_data": {
                'sensor_name': sensor_name,
                'sensor_value': sensor_value,
                'sensor_id': sensor_id,
            },
        }
        headers = {'User-Agent': 'XY', 'Content-type': 'application/json'}
        response = requests.post(f"{base_url}/devices", json=body, headers=headers, params={
            "device_id": device_id,
        })
        data = response.json()

        json_normalize(data)
        return data

    def authenticate(self, device_id):
        # authenticate
        self.device_id = device_id
        return self

    def createSamples(start_temperature, end_temperature, amount):
        arr = np.linspace(start_temperature, end_temperature, amount)
        def roundVal(val): return round(val, 1)
        applyall = np.vectorize(roundVal)(arr)
        return applyall

    def send(self, dict={}):
        self.sensor_name = list(dict.keys())[0]
        self.sensor_value = round(dict[self.sensor_name], 1)
        # delay after sending
        time.sleep(self.sleep_seconds)

        console.print(
            f"[cyan]\[sensor] [white]sent [blue]{self.sensor_name} [white]value of [gold1]{self.sensor_value}{self.sensor_unit} [white]to server")

        if self.device_id is not None:
            self._sendSensorData(
                self.sensor_name, self.sensor_value, self.device_id)
        else:
            print("Device id not authenticated or present")
