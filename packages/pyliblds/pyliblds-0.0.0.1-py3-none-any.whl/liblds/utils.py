class string(str):

    @classmethod
    def zfill(cls, data, length: int, position='prefix') -> str:

        if type(data) == int:
            data = str(data)

        zfill_len = length - len(data)
        if (position == 'suffix'):
            return data + zfill_len * '0'
        return zfill_len * '0' + data

    @classmethod
    def format(cls, data, type='b', remove_prefix=True) -> str:
        converted_data = None
        if type == 'b':
            converted_data = bin(data)
        elif type == 'x':
            converted_data = bin(data)

        if remove_prefix:
            if type == 'b':
                return converted_data.removeprefix('0x')
            return converted_data.removeprefix('0b')
        return converted_data

    @classmethod
    def to_hex_string(cls, data, type='x', case='lower') -> str:
        hex_str = str(hex(data))
        if type == None:
            hex_str = hex_str.removeprefix('0x')
        if case == 'upper':
            hex_str = hex_str.upper()
        return hex_str

    @classmethod
    def from_bytes(name_bytes: list) -> str:
        encoded_str = bytes(
            [c for c in name_bytes if c != 0xff and c != 0x00])
        return encoded_str.decode('utf-8')


class version:
    @classmethod
    def from_bytes(cls, data: list[int], version_format='M.m',
                   byte_order='little') -> str:

        if len(data) == 0 or data == None:
            return

        length = len(data)
        if length == 1 and version_format == 'M.m':
            major = string.to_hex_string(
                (data[0] >> 4) & 0xf, type=None, case='upper')
            minor = string.to_hex_string(
                (data[0] & 0xf), type=None, case='upper')
            return major + '.' + minor

        if length == 2 and version_format == 'M.m':
            major = string.to_hex_string(data[1], type=None, case='upper')
            minor = string.to_hex_string(data[0], type=None, case='upper')
            return major + '.' + minor


class bcd:
    @classmethod
    def to_decimal(cls, data: int) -> int:
        """
        Function to convert bcd data to decimal

        Args:
            data (int): number to convert

        Raises:
            ValueError: Raises if invalid data occurs

        Returns:
            int: return decimal data
        """
        data_str = string.format(data)
        data_str = string.zfill(data_str, (4 - len(data_str) % 4))
        nibbles = [int(data_str[i:i + 4], 2)
                   for i in range(0, len(data_str), 4)]
        if nibbles == None:
            raise ValueError('Invalid data to convert.')

        nibbles.reverse()
        val = 0
        for index, nibble in enumerate(nibbles):
            if nibble > 9:
                raise ValueError('Invalid data to convert.')
            else:
                val += (nibble * (pow(10, index)))
        return val


class protobuf:
    @classmethod
    def int_from_bytes(cls, data, endianess='little'):
        return int.from_bytes(bytearray(data), endianess)

    @classmethod
    def board_voltage_from_bytes(cls, bytes: list, ref=3300, resolution=1024):
        raw_data = int.from_bytes(bytearray(bytes), 'little')
        voltage = ((raw_data * ref) / resolution) / 0.4650
        return round(voltage)

    @classmethod
    def sensor_voltage_from_bytes(cls, bytes: list):
        raw_data = int.from_bytes(bytearray(bytes), 'big')
        return round(((raw_data * 3300) / 1024), 0)


class date:
    @classmethod
    def from_bytes(cls, bytes: list) -> str:
        """
        Function to convert bytes to date string DD:MM:YYYY
        Args:
            bytes (list): data to convert to date 

        Returns:
            str: date string on successfull conversion otherwise none
        """
        if (len(bytes) != 4):
            return None
        (date, month, *year) = bytes
        date = bcd.to_decimal(date)
        month = bcd.to_decimal(month)
        year = bcd.to_decimal(int.from_bytes_protobuf(year))
        if (date > 31) or (month > 12):
            return None
        return ":".join([str(date), str(month), str(year)])


class checksum:

    @classmethod
    def ldsbus(cls, buffer: list, poly=0x1021, initial_value=0xffff):
        """
        Function to compute the LDSU CRC16

        Args:
            buffer (list): list of bytes to compute
            poly (hexadecimal, optional): polynomial. Defaults to 0x1021.
            initial_value (hexadecimal, optional): initial value . Defaults to 0xffff.

        Raises:
            AttributeError: if given data length is zero or none.

        Returns:
            int: computed crc16
        """
        if (len(buffer) == 0):
            raise AttributeError("Input buffer length cannot be zero.")

        crc_acc = initial_value
        for data in buffer:
            crc_acc_in = (crc_acc ^ (data << 8)) & 0xffff
            for i in range(0, 8):
                if (crc_acc_in & 0x8000) == 0x8000:
                    crc_acc_in <<= 1
                    crc_acc_in = (crc_acc_in ^ poly)
                else:
                    crc_acc_in <<= 1
            crc_acc = crc_acc_in

    @classmethod
    def xor(cls, data: list, initial_value=0) -> int:
        """
        Function to compute XOR checksum

        Args:
            data (list): list of bytes to compute
            initial_value (int, optional): initial value . Defaults to 0.

        Raises:
            AttributeError: if given data length is zero or none.

        Returns:
            int: computed xor checksum
        """
        if (data == None) or (len(data) == 0):
            raise AttributeError("Invalid data to compute")
        xor_val = initial_value
        for d in data:
            xor_val ^= d
        return xor_val


class uuid:
    @classmethod
    def from_bytes(uuid_bytes: list, prefix_length=14, byte_order='little') -> str:
        uuid_prefix = bytes(uuid_bytes[0:prefix_length]).decode('utf-8')
        running_number = protobuf.int_from_bytes(
            uuid_bytes[prefix_length:], byte_order)
        running_number = string.zfill(running_number, 5)
        return uuid_prefix + running_number
