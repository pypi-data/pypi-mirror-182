#!/usr/bin/env python3.6

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from struct import pack, unpack
import time
import datetime
from bleak import BleakScanner
from bleak import BleakClient
import binascii
import math
from collections import namedtuple
import asyncio

Fanspeeds = namedtuple('Fanspeeds', 'Humidity Light Trickle')
Fanspeeds.__new__.__defaults__ = (2250, 1625, 1000)
Time = namedtuple('Time', 'DayOfWeek Hour Minute Second')
Sensitivity = namedtuple('Sensitivity', 'HumidityOn Humidity LightOn Light')
LightSensorSettings = namedtuple('LightSensorSettings', 'DelayedStart RunningTime')
HeatDistributorSettings = namedtuple('HeatDistributorSettings', 'TemperatureLimit FanSpeedBelow FanSpeedAbove')
SilentHours = namedtuple('SilentHours', 'On StartingHour StartingMinute EndingHour EndingMinute')
TrickleDays = namedtuple('TrickleDays', 'Weekdays Weekends')
BoostMode = namedtuple('BoostMode', 'OnOff Speed Seconds')

FanState = namedtuple('FanState', 'Humidity Temp Light RPM Mode')

# Stolen defines for each characteristic (taken from a decompiled Android App)
CHARACTERISTIC_APPEARANCE = "00002a01-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_AUTOMATIC_CYCLES = "f508408a-508b-41c6-aa57-61d1fd0d5c39"
CHARACTERISTIC_BASIC_VENTILATION = "faa49e09-a79c-4725-b197-bdc57c67dc32"
CHARACTERISTIC_BOOST = "118c949c-28c8-4139-b0b3-36657fd055a9"
CHARACTERISTIC_CLOCK = "6dec478e-ae0b-4186-9d82-13dda03c0682"
CHARACTERISTIC_DEVICE_NAME = "00002a00-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_FACTORY_SETTINGS_CHANGED = "63b04af9-24c0-4e5d-a69c-94eb9c5707b4"
CHARACTERISTIC_FAN_DESCRIPTION = "b85fa07a-9382-4838-871c-81d045dcc2ff"
CHARACTERISTIC_FIRMWARE_REVISION = "00002a26-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_HARDWARE_REVISION = "00002a27-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_LED = "8b850c04-dc18-44d2-9501-7662d65ba36e"
CHARACTERISTIC_LEVEL_OF_FAN_SPEED = "1488a757-35bc-4ec8-9a6b-9ecf1502778e"
CHARACTERISTIC_MANUFACTURER_NAME = "00002a29-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_MODE = "90cabcd1-bcda-4167-85d8-16dcd8ab6a6b"
CHARACTERISTIC_MODEL_NUMBER = "00002a24-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_NIGHT_MODE = "b5836b55-57bd-433e-8480-46e4993c5ac0"
CHARACTERISTIC_PIN_CODE = "4cad343a-209a-40b7-b911-4d9b3df569b2"
CHARACTERISTIC_PIN_CONFIRMATION = "d1ae6b70-ee12-4f6d-b166-d2063dcaffe1"
CHARACTERISTIC_RESET = "ff5f7c4f-2606-4c69-b360-15aaea58ad5f"
CHARACTERISTIC_SENSITIVITY = "e782e131-6ce1-4191-a8db-f4304d7610f1"
CHARACTERISTIC_SENSOR_DATA = "528b80e8-c47a-4c0a-bdf1-916a7748f412"
CHARACTERISTIC_SERIAL_NUMBER = "00002a25-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_SOFTWARE_REVISION = "00002a28-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_STATUS = "25a824ad-3021-4de9-9f2f-60cf8d17bded"
CHARACTERISTIC_TEMP_HEAT_DISTRIBUTOR = "a22eae12-dba8-49f3-9c69-1721dcff1d96"
CHARACTERISTIC_TIME_FUNCTIONS = "49c616de-02b1-4b67-b237-90f66793a6f2"

async def FindCalimas():

    addresses = [device.address for device in await BleakScanner.discover()]

    calimas = []
    
    for a in addresses:
        if a[0:8] == "58:2b:db":
            calimas.append(a)

    return tuple(e for e in calimas)

class Calima:

    def __init__(self, addr, pin):
        # Set debug to true if you want more verbose output
        self._debug = True
        self.conn = asyncio.run(BleakClient(addr).connect())
        self.setAuth(pin)

    def __del__(self):
        self.conn.disconnect()

    def disconnect(self):
       asyncio.run(self.conn.disconnect())

    def _bToStr(self, val):
        return binascii.b2a_hex(val).decode('utf-8')

    def _readUUID(self, uuid):
        val=asyncio.run(self.conn.read_gatt_char(uuid))
        #val = self.conn.getCharacteristics(uuid=uuid)[0].read()
        if (self._debug):
            print("[Calima] [R] %s = %s" % (uuid, self._bToStr(val)))

        return val

    def _readHandle(self, handle):
        val = self.conn.readCharacteristic(handle)
        if (self._debug):
            print("[Calima] [R] %s = %s" % (hex(handle), self._bToStr(val)))
        return val

    def _writeUUID(self, uuid, val):
        if (self._debug):
            print("[Calima] [W] %s = %s" % (uuid, self._bToStr(val)))

        self.conn.getCharacteristics(uuid=uuid)[0].write(val, withResponse=True)

    def scanCharacteristics(self):
        #val = self.conn.getCharacteristics()
        val = self.conn.getCharacteristics()
        for ch in val:
            if (ch.supportsRead()):
                rd = ch.read()
                print("[%s] %s (%s) = (%d) %s" % (hex(ch.getHandle()), ch.uuid.getCommonName(), ch.propertiesToString(), len(rd), self._bToStr(rd)))
            else:
                print("[%s] %s (%s)" % (hex(ch.getHandle()), ch.uuid.getCommonName(), ch.propertiesToString()))

    # --- Generic GATT Characteristics

    def getDeviceName(self):
        return self._readHandle(0x3).decode('ascii')

    def getModelNumber(self):
        return self._readHandle(0xd).decode('ascii')

    def getSerialNumber(self):
        return self._readHandle(0xb).decode('ascii')

    def getHardwareRevision(self):
        return self._readHandle(0xf).decode('ascii')

    def getFirmwareRevision(self):
        return self._readHandle(0x11).decode('ascii')

    def getSoftwareRevision(self):
        return self._readHandle(0x13).decode('ascii')

    def getManufacturer(self):
        return self._readHandle(0x15).decode('ascii')

    # --- Onwards to PAX characteristics

    def setAuth(self, pin):
        self._writeUUID(CHARACTERISTIC_PIN_CODE, pack("<I", int(pin)))

    def checkAuth(self):
        return bool(unpack('<I', self._readUUID(CHARACTERISTIC_PIN_CONFIRMATION)))

    def setAlias(self, name):
        self._writeUUID(CHARACTERISTIC_FAN_DESCRIPTION, pack('20s', bytearray(name, 'utf-8')))

    def getAlias(self):
        return self._readUUID(CHARACTERISTIC_FAN_DESCRIPTION).decode('utf-8')

    def getIsClockSet(self):
        return self._bToStr(self._readUUID(CHARACTERISTIC_STATUS))

    def getState(self):
        # Short Short Short Short    Byte Short Byte
        # Hum   Temp  Light FanSpeed Mode Tbd   Tbd
        v = unpack('<4HBHB', self._readUUID(CHARACTERISTIC_SENSOR_DATA))
        trigger = "No trigger"
        if ((v[4] >> 4) & 1) == 1:
            trigger = "Boost"
        elif (v[4] & 3) == 1:
            trigger = "Trickle ventilation"
        elif (v[4] & 3) == 2:
            trigger = "Light ventilation"
        elif (v[4] & 3) == 3: # Note that the trigger might be active, but mode must be enabled to be activated
            trigger = "Humidity ventilation"
        return FanState(round(math.log2(v[0])*10, 2) if v[0] > 0 else 0, v[1]/4, v[2], v[3], trigger)

    def getFactorySettingsChanged(self):
        return unpack('<?', self._readUUID(CHARACTERISTIC_FACTORY_SETTINGS_CHANGED))

    def getMode(self):
        v = unpack('<B', self._readUUID(CHARACTERISTIC_MODE))
        if v == 0:
            return "MultiMode"
        elif v == 1:
            return "DraftShutterMode"
        elif v == 2:
            return "WallSwitchExtendedRuntimeMode"
        elif v == 3:
            return "WallSwitchNoExtendedRuntimeMode"
        elif v == 4:
            return "HeatDistributionMode"

    def setFanSpeedSettings(self, humidity=2250, light=1625, trickle=1000):
        for val in (humidity, light, trickle):
            if (val % 25 != 0):
                raise ValueError("Speeds should be multiples of 25")
            if (val > 2500 or val < 0):
                raise ValueError("Speeds must be between 0 and 2500 rpm")

        self._writeUUID(CHARACTERISTIC_LEVEL_OF_FAN_SPEED, pack('<HHH', humidity, light, trickle))

    def getFanSpeedSettings(self):
        return Fanspeeds._make(unpack('<HHH', self._readUUID(CHARACTERISTIC_LEVEL_OF_FAN_SPEED)))

    def setSensorsSensitivity(self, humidity, light):
        if humidity > 3 or humidity < 0:
            raise ValueError("Humidity sensitivity must be between 0-3")
        if light > 3 or light < 0:
            raise ValueError("Light sensitivity must be between 0-3")

        value = pack('<4B', bool(humidity), humidity, bool(light), light)
        self._writeUUID(CHARACTERISTIC_SENSITIVITY, value)

    def getSensorsSensitivity(self):
        # Hum Active | Hum Sensitivity | Light Active | Light Sensitivity
        return Sensitivity._make(unpack('<4B', self._readUUID(CHARACTERISTIC_SENSITIVITY)))

    def setLightSensorSettings(self, delayed, running):
        if delayed not in (0, 5, 10):
            raise ValueError("Delayed must be 0, 5 or 10 minutes")
        if running not in (5, 10, 15, 30, 60):
            raise ValueError("Running time must be 5, 10, 15, 30 or 60 minutes")

        self._writeUUID(CHARACTERISTIC_TIME_FUNCTIONS, pack('<2B', delayed, running))

    def getLightSensorSettings(self):
        return LightSensorSettings._make(unpack('<2B', self._readUUID(CHARACTERISTIC_TIME_FUNCTIONS)))

    def getHeatDistributor(self):
        return HeatDistributorSettings._make(unpack('<BHH', self._readUUID(CHARACTERISTIC_TEMP_HEAT_DISTRIBUTOR)))

    def setBoostMode(self, on, speed, seconds):
        if speed % 25:
            raise ValueError("Speed must be a multiple of 25")
        if not on:
            speed = 0
            seconds = 0

        self._writeUUID(CHARACTERISTIC_BOOST, pack('<BHH', on, speed, seconds))

    def getBoostMode(self):
        return BoostMode._make(unpack('<BHH', self._readUUID(CHARACTERISTIC_BOOST)))

    def getLed(self):
        return self._bToStr(self._readUUID(CHARACTERISTIC_LED))

    def setAutomaticCycles(self, setting):
        if setting < 0 or setting > 3:
            raise ValueError("Setting must be between 0-3")

        self._writeUUID(CHARACTERISTIC_AUTOMATIC_CYCLES, pack('<B', setting))

    def getAutomaticCycles(self):
        return unpack('<B', self._readUUID(CHARACTERISTIC_AUTOMATIC_CYCLES))[0]

    def setTime(self, dayofweek, hour, minute, second):
        self._writeUUID(CHARACTERISTIC_CLOCK, pack('<4B', dayofweek, hour, minute, second))

    def getTime(self):
        return Time._make(unpack('<BBBB', self._readUUID(CHARACTERISTIC_CLOCK)))

    def setTimeToNow(self):
        now = datetime.datetime.now()
        self.setTime(now.isoweekday(), now.hour, now.minute, now.second)

    def setSilentHours(self, on, startingHours, startingMinutes, endingHours, endingMinutes):
        if startingHours < 0 or startingHours > 23:
            raise ValueError("Starting hour is an invalid number")
        if endingHours < 0 or endingHours > 23:
            raise ValueError("Ending hour is an invalid number")
        if startingMinutes < 0 or startingMinutes > 59:
            raise ValueError("Starting minute is an invalid number")
        if endingMinutes < 0 or endingMinutes > 59:
            raise ValueError("Ending minute is an invalid number")

        value = pack('<5B', int(on),
                     startingHours, startingMinutes,
                     endingHours, endingMinutes)
        self._writeUUID(CHARACTERISTIC_NIGHT_MODE, value)

    def getSilentHours(self):
        return SilentHours._make(unpack('<5B', self._readUUID(CHARACTERISTIC_NIGHT_MODE)))

    def setTrickleDays(self, weekdays, weekends):
        self._writeUUID(CHARACTERISTIC_BASIC_VENTILATION, pack('<2B', weekdays, weekends))

    def getTrickleDays(self):
        return TrickleDays._make(unpack('<2B', self._readUUID(CHARACTERISTIC_BASIC_VENTILATION)))

    def getReset(self): # Should be write
        return self._readUUID(CHARACTERISTIC_RESET)

    def resetDevice(self): # Dangerous
        self._writeUUID(CHARACTERISTIC_RESET, pack('<I', 120))

    def resetValues(self): # Danguerous
        self._writeUUID(CHARACTERISTIC_RESET, pack('<I', 85))
