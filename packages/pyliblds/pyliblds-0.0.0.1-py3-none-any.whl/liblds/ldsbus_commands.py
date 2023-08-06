from .ldsbus_interface import LDSBusInterface
from .ldsbus_errors import LDSBusResponseError
from .ldsu_response import LDSUResponse, LDSUInformation
from .ldsbus_constants import LDSBusConstants as constants
from .utils import checksum, uuid


class LDSBusCommands:

    @property
    def cmd_reset(self):
        return 0x01

    @property
    def cmd_identify(self):
        return 0x06

    @property
    def cmd_get_uuid(self):
        return 0x06

    @property
    def cmd_info(self):
        return 0x21

    @property
    def cmd_status(self):
        return 0x22

    @property
    def cmd_echo(self):
        return 0x23

    @property
    def cmd_i2c_reg_on(self):
        return 0x2c

    @property
    def cmd_i2c_reg_off(self):
        return 0x2d

    @property
    def cmd_i2c_speed(self):
        return 0x2e

    @property
    def cmd_read(self):
        return 0x60

    @property
    def cmd_readn(self):
        return 0x61

    @property
    def cmd_write(self):
        return 0x62

    @property
    def cmd_writen(self):
        return 0x63

    @property
    def response_code(self):
        return 0x80

    @property
    def ldsu_address_mask(self):
        return 0x7f

    def __init__(self, ldsbus_interface: LDSBusInterface):
        super().__init__()
        self.__interface = ldsbus_interface
        self.__ldsu_address = 0

    def is_valid_response_code(self, response_id):
        exp_response_id = self.__ldsu_address | self.response_code
        return response_id == exp_response_id

    def __get_payload_length(data: list) -> int:
        if data == None or len(data) == 0:
            return data[0]
        return 0

    def __response_parser(self, command: int, data: tuple, length=0):
        if (data == None) or (len(data) == 0):
            raise AttributeError("Length of data cannot be Zero or None")

        if length != len(data):
            raise AttributeError("Data length not match")

        ldsu_response = LDSUResponse(data)
        ldsu_id = ldsu_response.get_reponse_id()

        if self.is_valid_response_code(ldsu_id):
            raise ValueError("Invalid data to parse...")

        payload_length = ldsu_response.get_payload_length()
        payload = ldsu_response.get_payload()
        ldsu_crc16 = ldsu_response.get_checksum()
        if ldsu_crc16 != None:
            crc16 = checksum.ldsbus(payload)
            if crc16 != ldsu_crc16:
                raise LDSBusResponseError("Checksum error")

        return {
            'ldsu_id': self.__ldsu_address,
            'payload_length': payload_length,
            'payload': payload,
            'checksum': checksum
        }

    def reset(self) -> None:
        """
        Function to reset the ldsu in the bus
        """
        try:
            query = [self.cmd_reset]
            self.__interface.read_write_data(query)
        except Exception as ex:
            raise (ex)

    def identifiy(self) -> None:
        """
        Function to identify the addressed LDSU in the bus
        """
        try:
            query = [self.cmd_identify]
            self.__interface.read_write_data(query)
        except Exception as ex:
            raise (ex)

    def get_uuid(self) -> str:
        """
        Function to get the UUID of the addressed LDSU

        Returns:
            str: UUID of the ldsu
        """
        try:
            query = [self.cmd_get_uuid]
            response = self.__interface.read_write_data(query, read_len=20)
            payload = self.__response_parser(self.cmd_get_uuid, response, 20)[
                'payload']
            return uuid.from_bytes(payload)
        except Exception as ex:
            raise (ex)

    def info(self) -> LDSUInformation:
        """
        Function to get the LDSU Information

        Returns:
            LDSUInformation: return ldsu information if device present in the bus
        """
        try:
            query = [self.cmd_info]
            response = self.__interface.read_write_data(query, read_len=18)
            info = self.__response_parser(
                self.cmd_info, response, length=18)['payload']
            return LDSUInformation(info)
        except (AttributeError, ValueError) as error:
            print(error)

    def last_command_status(self) -> int:
        """
        Function to get the last command status

        Returns:
            int: returns command code if succeed otherwise return 0xff
        """
        try:
            query = [self.cmd_status]
            response = self.__interface.read_write_data(query, read_len=2)
            return self.__response_parser(self.cmd_status, response, length=2)['payload']
        except AttributeError as error:
            print(error)

    def echo(self, data: list) -> list:
        """
        Args:

            data (list): data to send to LDSU Device

        Raises:
            AttributeError: Raises if data length is more than 32 bytes

        Returns:
            list: received data bytes from the LDSU
        """
        try:
            if (len(data) >= 32):
                raise AttributeError("Data length not more than 32 bytes")

            query = [self.cmd_echo]
        except Exception as ex:
            print(ex)

    def read(self, i2c_device_address: int, register: int) -> int:
        """
        Function to read the i2c device in the LDSU

        Args:
            i2c_device_address (int): i2c device address
            register (int): register address to read

        Returns:
            int: return read data if succeed otherwise None
        """
        try:
            query = [self.cmd_read, i2c_device_address, register]
            response = self.__interface.read_write_data(query, read_len=2)
            return self.__response_parser(self.cmd_read, response, 2)['payload']
        except Exception as ex:
            print(ex)

    def read_n(self, i2c_device_address: int, register: int, length: int) -> tuple:
        """
        Function to read multiple bytes from the i2c device in the LDSU

        Args:
            i2c_device_address (int): i2c device address
            register (int): register address to read
            length (int): Number of bytes to read

        Returns:
            Tuple: returns tuple of int if succeed or none
        """
        try:
            query = [self.cmd_readn, i2c_device_address, register, length]
            response = self.__interface.read_write_data(
                query, read_len=length + 4)
            return tuple(self.__response_parser(self.cmd_readn, response, length + 4)['payload'])
        except Exception as ex:
            print(ex)

    def write(self, i2c_device_address, register, data: int) -> None:
        """
        Function to write into the i2c device in the LDSU Device

        Args:
            i2c_device_address (int): i2c device address to write
            register (int): register address to write
            data (int): data to write

        Returns:
            None
        """
        try:
            query = [self.cmd_write, i2c_device_address, register, data]
            self.__interface.read_write_data(query)
        except Exception as ex:
            print(ex)

    def write_n(self, i2c_device_address, register, data: list) -> int:
        """
        Function to write multiple bytes to i2c device in the LDSU

        Args:
            i2c_device_address (int): i2c device address to write
            register (int): register address to write
            data (list): list of bytes to write

        Returns:
            int: number of bytes written
        """
        try:

            if (len(data) == 0) or (len(data) > 32):
                raise AttributeError(
                    "Data length not more than 32 bytes or None")
            query = [self.cmd_writen, i2c_device_address,
                     register, len(data)] + data
            response = self.__interface.read_write_data(query, read_len=4)
            return self.__response_parser(self.cmd_writen, response, 4)['payload_length']
        except Exception as ex:
            raise (ex)
        pass

    def set_i2c_speed(self, speed=0) -> None:
        """
        Function to set the i2c bus speed in the LDSU

        Args:
            speed (int, optional):  Defaults to 0 - 100KHz
                                                1 - 400KHz
        """
        try:
            query = [self.cmd_i2c_speed, 0x00]
            self.__interface.read_write_data(query)
        except Exception as ex:
            raise (ex)

    def enable_i2c_16bit_mode(self, reg_msb) -> None:
        """
        Function to turn ON the i2c 16 bit mode

        Args:
            reg_msb (_type_): MSB of the register
        """
        try:
            query = [self.cmd_i2c_reg_on, reg_msb]
            self.__interface.read_write_data(query)
        except Exception as ex:
            print(ex)

    def disable_i2c_16bit_mode(self) -> None:
        """
        Function to turn OFF the 16bit mode.
        """
        try:
            query = [self.cmd_i2c_reg_off]
            self.__interface.read_write_data(query)
        except Exception as ex:
            print(ex)

    def scan(self) -> tuple:
        """
        Function to scan the number of LDSU(s) connected to the bus.

        Returns:
            Tuple: returns the number of LDSU(s) in the bus
        """
        devices = []
        try:
            for address in range(constants.LDSBUS_START_SCAN_ADDRESS, constants.LDSBUS_END_SCAN_ADDRESS):
                if self.__ldsu_address.address_ldsu(address) == True:
                    devices.append(address)
            return tuple(devices)
        except Exception as ex:
            print(ex)

    def address_ldsu(self, address:int) -> bool:
        """
        Function to address the ldsu

        Args:
            address (int): device address 

        Returns:
            bool: True on device found otherwise False
        """
        try:
            return self.__interface.send_address(address)
        except Exception as ex:
            print(ex)
