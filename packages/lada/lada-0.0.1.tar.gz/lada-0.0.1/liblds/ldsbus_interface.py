"""
This module gives LDSBus interface APIs to communicate with LDSBus Devices.

Raises:
    LDSBusInterfaceError: raises if COM port error occurs
    ValueError: raises if any value error occurs
"""
from typing import List, Tuple, Union, Any
import sys
import ftd2xx as d2xx
import time
import liblds.interface.ldsbus_interface_messages as msg
import liblds.interface.lds_constants as constants


if sys.version_info >= (3, 8, 0):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class LDSBusUSBAdapterInfo(TypedDict):
    """
    Dictionary for LDSBus USB Adapter Information
    """
    index: int
    id: int
    serial: bytes
    description: bytes


class LDSBusInterfaceException(Exception):
    """
        LDSBus Interface Exceptions
    """

    def __init__(self, message):
        super().__init__()
        self.message = str(message)

    def __str__(self):
        return self.message


class LDSBusInterface:

    def __init__(self):
        self.__selected_adapter = None
        self.__adapter_list = self.__usb_adapter_list()
        self.__port_handle = None

    def __int__(self, data):
        return int.from_bytes(data, 'little')

    def __usb_adapter_list(self):
        adapter_list = []
        connected_devices = d2xx.listDevices()
        if (connected_devices == None):
            return None
        for index in range(len(connected_devices)):
            try:
                port = d2xx.open(index)
                device_info = port.getDeviceInfo()
                c_device_info = {
                    "index": index,
                    "description": device_info['description'],
                    "serial": device_info['serial'],
                    "id": hex(device_info['id']),
                }
                if constants.LDS_ADAPTER_CODE in c_device_info['description'].decode('utf8'):
                    adapter_list.append(c_device_info)
                port.close()
            except Exception as ex:
                pass

        return adapter_list

    def __power_on(self, ldsu_port=0) -> bool:
        if self.__port_handle is not None:
            io_status = self.__port_handle.getBitMode()
            if ldsu_port == 0:
                io_status &= 0xf7
            elif ldsu_port == 1:
                io_status &= 0xfb
            else:
                return False
            self.__port_handle.setBitMode(io_status, 0x20)
            time.sleep(1)
        return True

    def __power_off(self, ldsu_port=0) -> bool:
        if self.__port_handle is not None:
            io_status = self.__port_handle.getBitMode()
            if ldsu_port == 0:
                io_status |= 0x08
            elif ldsu_port == 1:
                io_status |= 0x04
            else:
                return False
            self.__port_handle.setBitMode(io_status, 0x20)
            time.sleep(1)
        return True

    def __port_write_bytes(self, data):
        try:
            if (self.__port_handle == None):
                raise LDSBusInterfaceException(
                    msg.LDSBUS_USB_ADAPTER_NOT_OPENED)

            self.__port_handle.write(bytes(data))
        except Exception as ex:
            raise ex

    def __port_write_byte(self, data):
        try:
            if (self.__port_handle == None):
                raise LDSBusInterfaceException(
                    msg.LDSBUS_USB_ADAPTER_NOT_OPENED)

            self.__port_handle.write(data.to_bytes(1, 'little'))
        except Exception as ex:
            raise ex

    def __port_read_bytes(self, length: int) -> Tuple:
        try:
            if (self.__port_handle == None):
                raise LDSBusInterfaceException(
                    msg.LDSBUS_USB_ADAPTER_NOT_OPENED)
            response = self.__port_handle.read(length, True)
            return response
        except Exception as ex:
            raise ex

    def __port_set_ldsu_mode_charateristics(self, ldsu_break: bool):
        try:
            if (self.__port_handle == None):
                raise LDSBusInterfaceException(
                    msg.LDSBUS_USB_ADAPTER_NOT_OPENED)
            parity = 0
            stop_bits = 2
            if (ldsu_break):
                parity = 4
                stop_bits = 0

            self.__port_handle.setDataCharacteristics(
                wordlen=8, stopbits=stop_bits, parity=parity)
        except Exception as ex:
            raise ex

    def __port_purge(self):
        try:
            if (self.__port_handle == None):
                raise LDSBusInterfaceException(
                    msg.LDSBUS_USB_ADAPTER_NOT_OPENED)

            self.__port_handle.purge(3)
        except:
            raise LDSBusInterfaceException(msg.LDSBUS_USB_IO_ERROR)

    def __port_get_received_length(self):
        try:
            if (self.__port_handle == None):
                raise LDSBusInterfaceException(
                    msg.LDSBUS_USB_ADAPTER_NOT_OPENED)

            (read_len, *other_status) = self.__port_handle.getStatus()
            return read_len
        except Exception as ex:
            raise ex

    def __send_break(self) -> None:
        if self.__port_handle is None:
            raise LDSBusInterfaceException(
                "LDSBus Communication port not opened.")
        try:
            self.__port_set_ldsu_mode_charateristics(True)
            self.__port_purge()
            self.__port_write_byte(0)
            self.__port_set_ldsu_mode_charateristics(False)
            time.sleep(0.001)
        except:
            raise LDSBusInterfaceException(msg.LDSBUS_USB_ADAPTER_NOT_FOUND)

    @ property
    def usb_adapter_list(self):
        """
        Property to get the number of LDSBus USB adapter connected to the machine.

        Returns:
           List of LDSBusUSBAdapterInfo (TypedDict): List of USB adapter information
        """
        return self.__adapter_list

    @ property
    def port_is_opened(self):
        """
        Propery to get the port status.

        Returns:
            bool : True if port is opened otherwise None.
        """
        if (self.__port_handle):
            return True
        return False

    @ property
    def selected_usb_adapter_info(self):
        """
        Propery to get the selected LDSBus USB Adapter information
        Returns:
            LDSBus USB Adapter Information(TypedDict): Return None if not selected.
        """
        return self.__adapter_list

    def print_adapter_info(self) -> None:
        """
        Helper function to print the LDSBus USB Adapter information

        Raises:
            LDSBusInterfaceException: Raises if the given adapter list is empty
        """

        if (len(self.__adapter_list) == 0):
            raise LDSBusInterfaceException(msg.LDSBUS_USB_ADAPTER_NOT_FOUND)

        for adapter in self.__adapter_list:
            print(f"Device {adapter['index']} :")
            print(f"\tDescription: {adapter['description'].decode('utf8')}")
            print(f"\tSerial: {adapter['serial'].decode('utf8')}")

    def open_usb_adapter(self, device_index: int) -> object:
        """
        Function to open the communication interface

        Raises:
            LDSBusInterfaceException: Raises if LDSBus USB adapter not found in the machine

        Returns:
            object : Return d2xx handle otherwise None if any not successfull
        """

        if constants.LDSBUS_ADAPTER_NOT_SELECTED >= device_index or device_index >= len(self.__adapter_list):
            raise LDSBusInterfaceException(
                msg.LDSBUS_USB_ADAPTER_INVALID_INDEX)

        self.__selected_adapter = self.__adapter_list[device_index]
        try:
            self.__port_handle = d2xx.openEx(self.__selected_adapter['serial'])
            if self.__port_handle != None:
                self.__port_handle.setBaudRate(230400)
                self.__port_handle.setDataCharacteristics(
                    wordlen=8, stopbits=2, parity=0)
                self.__port_handle.setTimeouts(
                    constants.LDSBUS_READ_TIMEOUT, constants.LDSBUS_WRITE_TIMEOUT)
                return self.__port_handle
        except:
            raise LDSBusInterfaceException(msg.LDSBUS_USB_ADAPTER_NOT_FOUND)

        return None

    def close_usb_adapter(self):
        """
        Function to close the opened LDSBus USB Adapter
        """
        try:
            self.__power_off(0)
            self.__power_off(1)
            if (self.__port_handle):
                self.__port_handle.close()
            self.__port_handle = None
            self.__selected_adapter = None
        except:
            raise LDSBusInterfaceException("LDSBus USB Adapter not found...")

    def ldsu_port_power(self, on_off=0) -> None:
        """
        Function to control the LDSU port power.
        Args:
            on_off (int, optional):  Defaults to    0 - Off.
                                                    1 - On
        """
        try:
            if on_off == 1:
                self.__power_on(0)
            else:
                self.__power_off(0)
        except:
            pass

    def ldsbus_port_power(self, on_off=0) -> None:
        """
        Function to control the LDSBus port power.

        Args:
            on_off (int, optional):  Defaults to    0 - Off.
                                                    1 - On
        """
        try:
            if on_off == 1:
                self.__power_on(1)
            else:
                self.__power_off(1)
        except:
            pass

    @ property
    def port_power_status(self):
        """
        Property to get the power status.

        Returns:
            int:    0x00 - LDSBus and LDSU port power is turned OFF
                    0x01 - LDSBus Port power turned ON and LDSU port power is turned OFF
                    0x02 - LDSBus Port power turned OFF and LDSU port power is turned ON
                    0x03 - LDSBus Port power turned ON and LDSU port power is turned ON
        """
        if self.port_handle is not None:
            io_status = ~(self.port_handle.getBitMode() >> 2) & 0x03
            return io_status

    def address_ldsu(self, ldsu_id: int) -> bool:
        """
        Function to address the device to communicate the LDSU

        Args:
            ldsu_id (int): LDSU Device ID (1 - 126)

        Raises:
            ValueError: Raises value error if LDSU ID is invalid
            LDSBusInterfaceException: Raise Interface exception if port not found.

        Returns:
            bool: Returns True if device found in the bus otherwise False
        """

        if 0 >= ldsu_id > 126:
            raise ValueError("Invalid address.")

        response = False

        self.device_address = ldsu_id
        try:
            self.__send_break()
            self.__port_purge()
            self.__port_write_byte(ldsu_id)
            time.sleep(0.002)
            if self.__port_get_received_length() == 1 and (self.__int__(self.__port_read_bytes(1)) == 0xAA):
                response = True

            return response
        except LDSBusInterfaceException as ex:
            raise LDSBusInterfaceException("LDSBus USB Adapter not found...")

    def terminate_device(self) -> None:
        """
        Function to terminate the last addressed device from the communication.

        Raises:
            LDSBusInterfaceException if any error occured at COM port
        """
        try:
            self.__send_break()
        except LDSBusInterfaceException as ex:
            raise ex

    def read_write_data(self, query: list, read_len=0) -> Tuple:
        """
        Function to read write data to the LDSU Device

        Args:
            query (list): list of bytes to send
            read_len (int, optional): Length to receive the bytes from the LDSU Device

        Returns:
            bytes: _description_
        """
        try:
            exit_time_counts = 0
            self.__port_purge()
            self.__port_write_bytes(query)

            if read_len == 0:
                return

            while True:
                received_length = self.__port_get_received_length()
                if received_length == read_len:
                    return tuple(self.__port_read_bytes(read_len))

                if exit_time_counts >= constants.LDSBUS_READ_TIMEOUT:
                    return None
                time.sleep(0.001)
                exit_time_counts += 1
        except LDSBusInterfaceException as ex:
            raise (ex)
