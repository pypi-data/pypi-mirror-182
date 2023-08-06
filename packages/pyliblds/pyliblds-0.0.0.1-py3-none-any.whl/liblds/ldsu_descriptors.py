from .ldsbus_commands import LDSBusCommands
from .utils import string, version, uuid, protobuf
import json


class LDSBusI2CSensorsActuators:
    """
    Class for LDSBus I2C Sensor Actuators
    """

    def __init__(self, lds_commands: LDSBusCommands):
        self.__commands = lds_commands
        self.__ldsu_salength = 0
        self.__sensors_actuators = None
        try:

            ldsu_descriptor = LDSUDescription(
                lds_commands=self.__commands)
            ldsu_desc = json.loads(ldsu_descriptor)
            self.__ldsu_salength = ldsu_desc['number_of_sensors_actuators']
            i2c_desc = []
            for read_address in range(0xc0, 0x2c0, 32):
                i2c_dev_address = (0x50 | ((read_address >> 8) & 0x3))
                register_address = read_address & 0xff
                rdata = self.__commands.read_n(
                    i2c_dev_address, register_address, 32)
                if rdata != None:
                    i2c_desc += rdata

            self.__sensors_actuators = []
            for i in range(0, (self.__ldsu_salength * 64), 64):
                i2c_dev = i2c_desc[i:i + 64]
                sensors_actuators_dic = {
                    "id": (i % 63),
                    "manufacturer": string.from_bytes(i2c_dev[0:24]),
                    "part_number": string.from_byte(i2c_dev[24:48]),
                    "i2c_address": string.format(i2c_dev[48], 'x', False),
                    "report_rate_ms": protobuf.int_from_bytes(i2c_dev[50:52])
                }
                self.__sensors_actuators.append(sensors_actuators_dic)
        except Exception as ex:
            raise ex

    def __str__(self):
        return str(self.__sensors_actuators)


class LDSUDescription:
    """
    Class for LDSU Description
    """

    def __init__(self, lds_commands: LDSBusCommands):
        self.__commands = lds_commands
        self.__ldsu_descriptor = None
        try:
            ldsu_descriptor = []
            for read_address in range(0x60, 0xb0, 16):
                i2c_dev_address = (0x50 | ((read_address >> 8) & 0x3))
                register_address = read_address & 0xff
                rdata = self.__commands.read_n(
                    i2c_dev_address, register_address, 16)
                if rdata != None:
                    ldsu_descriptor += rdata

            self.__ldsu_descriptor = {
                "manufacturer": "BRT Systems Pte Ltd.",
                "product_name": string.from_bytes(self.__ldsu_descriptor[0x20:0x40]),
                "product_version": version.from_bytes(self.__ldsu_descriptor[2:4]),
                "uuid": uuid.from_bytes(self.__ldsu_descriptor[16:32]),
                "number_of_sensors_actuators": self.__ldsu_descriptor[0x43]
            }
        except Exception as ex:
            raise ex

    def __str__(self):
        return str(self.__ldsu_descriptor)
