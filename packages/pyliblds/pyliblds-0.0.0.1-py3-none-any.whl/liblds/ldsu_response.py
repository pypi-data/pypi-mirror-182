from .utils import protobuf, version


class LDSUResponse(list):

    def __init__(self, data):
        super().__init__()
        self.__data = data

    def get_payload_length(self):
        if self.__data == None or len(self.__data) == 0:
            return 0

        if len(self.__data) > 2:
            return self.__data[1]

        return 1

    def get_payload(self):
        length = self.get_payload_length()
        if length == 0:
            return

        if length == 1 and len(self.__data) == 2:
            return self.__data[1]

        if len(self.__data) == (length + 4):
            return self.__data[2:-2]
        return

    def get_reponse_id(self):
        if self.__data == None or len(self.__data) == 0:
            return self.__data[0]
        return 0

    def get_checksum(self):
        if len(self.__data) > 2:
            return
        return protobuf.int_from_bytes(self.__data[-2:])


class LDSUResetSource:

    def __init__(self, src):
        self.__src = src

    def __str__(self):
        if (self.__src == 0):
            return 'NONE'
        if (self.__src & 0x01):
            return "EXTERNAL RESET"
        if (self.__src & 0x02):
            return "POWER ON RESET"
        if (self.__src & 0x08):
            return "WATCHDOG RESET"
        if (self.__src & 0x10):
            return "SOFTWARE RESET"
        else:
            return "UNKNOWN"


class LDSUInformation:
    """
    Class for LDSU Information
    """

    def __init__(self, info):
        self.__info = info

    def __str__(self):
        if len(self.__info) != 14:
            return None

        (firmware_version, command_status, reset_src, *others) = self.__info

        ldsu_information = {
            "firmware_version": version.from_bytes(firmware_version),
            "last_command_status": command_status,
            "reset_source": LDSUResetSource(reset_src),
            "board_voltage": protobuf.board_voltage_from_bytes(self.__info[4:6]),
            "number_of_received_queries_commands": protobuf.int_from_bytes(self.__info[8:10]),
            "number_of_responses": protobuf.int_from_bytes(self.__info[10:12]),
            "number_of_error_packets_received": protobuf.int_from_bytes(self.__info[12:13])
        }
        return str(ldsu_information)
