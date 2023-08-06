"""
This module to send LDSU and LDSBus commands to the LDSU Device

Raises:
    AttributeError: Raises if any invalid attribute error
    ValueError: Raises if any value error
    LDSBusResponseError: Raises if LDSBus Response error
    NotImplementedError: Raises if any unimplented commands
"""
import sys
from typing import List, Tuple
if sys.version_info >= (3, 8, 0):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

import liblds.interface.lds_constants as constants
from liblds.interface.ldsbus_interface import LDSBusInterface
from liblds.utils.checksum import ldsbus_calculate_checksum
from liblds.log import lds_logging as log
from liblds.utils.converters import byte_to_version, to_board_voltage

__reset = 0x01
__identify = 0x06
__get_uuid = 0x20
__info = 0x21
__status = 0x22
__echo = 0x23
__set_i2c_reg_on = 0x2c
__set_i2c_reg_off = 0x2d
__set_i2c_speed = 0x2e
__read = 0x60
__readn = 0x61
__write = 0x62
__writen = 0x63
__response_code = 0x80
__address_mask = 0x7F


class LDSBusResponse(TypedDict):
    """
    Class for LDSBus Response
    """
    ldsu_id: int
    payload_length: int
    payload: List
    checkum: int


class LDSUInformation(TypedDict):
    """
    Class for LDSU Information

    """
    firmware_version: str
    last_command_status: int
    reset_source: str
    board_voltage: int
    number_of_received_queries_commands: int
    number_of_responses: int
    number_of_error_packets_received: int


class LDSBusResponseError(ValueError):
    """
    Class for LDSBus Response Error
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self) -> str:
        return self.message


def __response_parser(device_id: int, command: int, data: tuple, length=0) -> LDSBusResponse:
    """
    Function to parse the response from LDSU Device

    Args:
        device_id (int): LDSU Device ID
        command (int): LDSBus Command
        data (list): LDSU reponse frame list
        length (int, optional): length of the frame. Defaults to 0.

    Raises:
        AttributeError: Raises if invalid length of the frame
        ValueError: Raises if given frame is invalid

    Returns:
        LDSBusResponse: returns LDSBus Response if succeed otherwise None
    """

    if (data == None) or (len(data) == 0):
        raise AttributeError("Length of data cannot be Zero or None")

    if length != len(data):
        raise AttributeError("Data length not match")

    (ldsu_did, *ldsu_reponse_data) = data
    if (device_id | __response_code) != ldsu_did:
        raise ValueError("Invalid data to parse...")

    error_check = False

    payload_length = 0
    payload = None

    if command == __get_uuid:
        payload_length = ldsu_reponse_data[0]
        payload = ldsu_reponse_data[1:17]
        error_check = True
    elif command == __info:
        payload_length = ldsu_reponse_data[0]
        payload = ldsu_reponse_data[1:15]
        error_check = True
    elif command == __status:
        payload_length = 1
        payload = ldsu_reponse_data[0]
    elif command == __read:
        payload_length = 1
        payload = ldsu_reponse_data[0]
    elif command == __readn:
        payload_length = ldsu_reponse_data[0]
        payload = ldsu_reponse_data[1:-2]
        error_check = True
    elif command == __writen:
        payload_length = ldsu_reponse_data[0]
        payload = ldsu_reponse_data[1:3]

    checksum = 0
    if (error_check is True):
        crc = int.from_bytes(ldsu_reponse_data[-2:], 'little')
        checksum = ldsbus_calculate_checksum(payload)
        if checksum != crc:
            raise LDSBusResponseError("Checksum error")

    if (payload_length != 0):
        return {
            'ldsu_id': device_id,
            'payload_length': payload_length,
            'payload': payload,
            'checksum': checksum
        }


def __get_reset_source_str(data):
    if (data == 0):
        return "NONE"
    if (data & 0x01):
        return "EXTERNAL RESET"
    if (data & 0x02):
        return "POWER ON RESET"
    if (data & 0x08):
        return "WATCHDOG RESET"
    if (data & 0x10):
        return "SOFTWARE RESET"
    else:
        return "UNKNOWN"


def ___parse_info_command(data: bytes) -> LDSUInformation:
    if len(data) != 14:
        raise ValueError("Input data length not match")

    (firmware_version, command_status, reset_src, *others) = data

    ldsu_information = {
        "firmware_version": byte_to_version(firmware_version),
        "last_command_status": command_status,
        "reset_source": __get_reset_source_str(reset_src),
        "board_voltage": to_board_voltage(data[4:6]),
        "number_of_received_queries_commands": int.from_bytes(data[8:10], 'little'),
        "number_of_responses": int.from_bytes(data[10:12], 'little'),
        "number_of_error_packets_received": int.from_bytes(data[12:13], 'little')
    }
    return ldsu_information


def reset(ldsbus_interface: LDSBusInterface) -> None:
    """
    Function to reset the LDSU Devices in the LDSBus

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
    """
    try:
        query = [__reset]
        ldsbus_interface.read_write_data(query)
    except Exception as ex:
        raise (ex)


def random() -> None:
    raise NotImplementedError


def identifiy(ldsbus_interface: LDSBusInterface) -> None:
    """
    Function to identify the addressed LDSU in the bus

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
    """
    try:
        query = [__identify]
        ldsbus_interface.read_write_data(query)
    except Exception as ex:
        raise (ex)


def get_uuid(ldsbus_interface: LDSBusInterface) -> str:
    """
    Function to get the UUID of the addressed LDSU

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Returns:
        str: UUID
    """
    try:
        query = [__get_uuid]
        response = ldsbus_interface.read_write_data(query, read_len=20)
        uuid = __response_parser(ldsbus_interface.device_address, __get_uuid, response, 20)[
            'payload']
        return bytes(uuid[0:14]).decode('utf-8') + str(int.from_bytes(uuid[14:15], 'little')).zfill(6)
    except Exception as ex:
        raise (ex)


def info(ldsbus_interface: LDSBusInterface) -> LDSUInformation:
    """
    Function to get the LDSU Information

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Returns:
        LDSUInformation (TypedDict): return ldsu information if device present in the bus
    """
    try:
        query = [__info]
        response = ldsbus_interface.read_write_data(query, read_len=18)
        info = __response_parser(
            ldsbus_interface.device_address, __info, response, length=18)['payload']
        return ___parse_info_command(info)
    except (AttributeError, ValueError) as error:
        log.error(error)


def last_command_status(ldsbus_interface: LDSBusInterface) -> int:
    """
    Function to get the last command status

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Returns:
        int: returns command code if succeed otherwise return 0xff
    """
    try:
        query = [__status]
        response = ldsbus_interface.read_write_data(query, read_len=2)
        return __response_parser(
            ldsbus_interface.device_address, __status, response, length=2)['payload']
    except AttributeError as error:
        log.error(error)


def echo(ldsbus_interface: LDSBusInterface, data: list) -> list:
    """
    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        data (list): data to send to LDSU Device

    Raises:
        AttributeError: Raises if data length is more than 32 bytes

    Returns:
        list: received data bytes from the LDSU
    """
    try:
        if (len(data) >= 32):
            raise AttributeError("Data length not more than 32 bytes")

        query = [__echo]
    except Exception as ex:
        raise (ex)


def read(ldsbus_interface: LDSBusInterface, i2c_device_address: int, register: int) -> int:
    """
    Function to read the i2c device in the LDSU

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        i2c_device_address (int): i2c device address
        register (int): register address to read

    Returns:
        int: return read data if succeed otherwise None
    """
    try:
        query = [__read, i2c_device_address, register]
        response = ldsbus_interface.read_write_data(query, read_len=2)
        return __response_parser(ldsbus_interface.device_address, __read, response, 2)['payload']
    except Exception as ex:
        raise (ex)


def read_n(ldsbus_interface: LDSBusInterface, i2c_device_address: int, register: int, length: int) -> Tuple:
    """
    Function to read multiple bytes from the i2c device in the LDSU

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        i2c_device_address (int): i2c device address
        register (int): register address to read
        length (int): Number of bytes to read

    Returns:
        Tuple: returns tuple of int if succeed or none
    """
    try:
        query = [__readn, i2c_device_address, register, length]
        response = ldsbus_interface.read_write_data(
            query, read_len=length + 4)
        return tuple(__response_parser(ldsbus_interface.device_address,
                                       __readn, response, length + 4)['payload'])
    except Exception as ex:
        raise (ex)


def write(ldsbus_interface: LDSBusInterface, i2c_device_address, register, data: int) -> None:
    """
    Function to write into the i2c device in the LDSU Device

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        i2c_device_address (int): i2c device address to write
        register (int): register address to write
        data (int): data to write

    Raises:
        ex: _description_

    Returns:
        None
    """
    try:
        query = [__write, i2c_device_address, register, data]
        ldsbus_interface.read_write_data(query, read_len=0)
    except Exception as ex:
        raise ex


def write_n(ldsbus_interface: LDSBusInterface, i2c_device_address, register, data: list) -> int:
    """
    Function to write multiple bytes to i2c device in the LDSU

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        i2c_device_address (int): i2c device address to write
        register (int): register address to write
        data (list): list of bytes to write

    Returns:
        int: number of bytes written
    """
    try:

        if (len(data) == 0) or (len(data) > 32):
            raise AttributeError("Data length not more than 32 bytes or None")
        query = [__writen, i2c_device_address, register, len(data)] + data
        print(query)
        response = ldsbus_interface.read_write_data(query, read_len=4)
        return __response_parser(ldsbus_interface.device_address,
                                 __writen, response, 4)['payload_length']
    except Exception as ex:
        raise (ex)
    pass


def set_i2c_speed(ldsbus_interface: LDSBusInterface, speed=0) -> None:
    """
    Function to set the i2c bus speed in the LDSU

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        speed (int, optional):  Defaults to 0 - 100KHz
                                            1 - 400KHz
    """
    try:
        query = [__set_i2c_speed, 0x00]
        ldsbus_interface.read_write_data(query)
    except Exception as ex:
        raise (ex)


def enable_i2c_16bit_mode(ldsbus_interface: LDSBusInterface, reg_msb) -> None:
    """
    Function to turn ON the i2c 16 bit mode

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
        reg_msb (_type_): MSB of the register
    """
    try:
        query = [__set_i2c_reg_on, reg_msb]
        ldsbus_interface.read_write_data(query)
    except Exception as ex:
        raise (ex)


def disable_i2c_16bit_mode(ldsbus_interface: LDSBusInterface) -> None:
    """
    Function to turn OFF the 16bit mode.

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device
    """
    try:
        query = [__set_i2c_reg_off]
        ldsbus_interface.read_write_data(query)
    except Exception as ex:
        raise (ex)


def scan(ldsbus_interface: LDSBusInterface) -> Tuple:
    """
    Function to scan the number of LDSU(s) connected to the bus.

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Returns:
        Tuple: returns the number of LDSU(s) in the bus
    """
    devices = []
    try:
        for address in range(constants.LDSBUS_START_SCAN_ADDRESS, constants.LDSBUS_END_SCAN_ADDRESS):
            if ldsbus_interface.address_ldsu(address) == True:
                devices.append(address)
        return tuple(devices)
    except Exception as ex:
        raise (ex)
