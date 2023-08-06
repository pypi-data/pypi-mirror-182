import sys
if sys.version_info >= (3, 8, 0):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
from typing import List, Tuple

from liblds.interface.ldsbus_interface import LDSBusInterface
from liblds.commands.ldsbus_commands import read_n


class LDSBusI2CSensorsActuators(TypedDict):
    """
    Class for LDSBus I2C Sensor Actuators
    """
    manufacturer: str
    part_number: str
    i2c_address: int
    report_rate_ms: int


class LDSUDescription(TypedDict):
    """
    Class for LDSU Description
    """
    manufacturer: str
    product_name: int
    product_version: str
    uuid: str


def __read_nvm_i2c_descriptors(lds_interface: LDSBusInterface) -> list[bytes]:
    try:
        data = []
        for read_address in range(0xc0, 0x2c0, 32):
            i2c_dev_address = (0x50 | ((read_address >> 8) & 0x3))
            register_address = read_address & 0xff
            rdata = read_n(lds_interface, i2c_dev_address,
                           register_address, 32)
            if rdata != None:
                data += rdata
        return data
    except Exception as ex:
        raise ex


def __read_nvm_ldsu_descriptors(lds_interface: LDSBusInterface) -> Tuple:
    """
    Function to read the LDSU Descriptors

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Raises:
        ex: _description_

    Returns:
        Tuple: on successful read returns list of bytes otherwise none
    """
    try:
        data = []
        for read_address in range(0x60, 0xb0, 16):
            i2c_dev_address = (0x50 | ((read_address >> 8) & 0x3))
            register_address = read_address & 0xff
            rdata = read_n(lds_interface, i2c_dev_address,
                           register_address, 16)
            if rdata != None:
                data += rdata
        return tuple(data)
    except Exception as ex:
        raise ex


def ldsu_get_sensors_actuators_list(lds_interface: LDSBusInterface) -> List[LDSBusI2CSensorsActuators]:
    """
    Function to get the LDSU Sensors and Actuators 

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Returns:
        List[LDSBusI2CSensorsActuators]: returns list of i2c descriptors if succeed otherwise None
    """
    try:
        sensors_actuators = []
        descriptor = __read_nvm_ldsu_descriptors(lds_interface)
        device_counts = descriptor[0x43]
        i2c_descriptor_raw_data = __read_nvm_i2c_descriptors(lds_interface)
        for i in range(0, (device_counts * 64), 64):
            i2c_dev = i2c_descriptor_raw_data[i:i + 64]
            manufacturer = bytes(
                [c for c in i2c_dev[0:24] if c != 0xff and c != 0x00]).decode('utf-8')
            sensors_actuators_dic = {
                "id": (i % 63),
                "manufacturer": manufacturer,
                "part_number": bytes([c for c in i2c_dev[24:48] if c != 0xff and c != 0x00]).decode('utf-8'),
                "i2c_address": i2c_dev[48],
                "report_rate_ms": int.from_bytes(i2c_dev[50:52], 'little')
            }
            sensors_actuators.append(sensors_actuators_dic)
        return sensors_actuators
    except Exception as ex:
        raise (ex)


def ldsu_get_descriptor(lds_interface: LDSBusInterface) -> LDSUDescription:
    """
    Function to get the LDSU descriptor

    Args:
        ldsbus_interface (LDSBusInterface): ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Returns:
        LDSUDescription: returns LDSU description if succeed otherwise None
    """
    try:
        ldsu_des_raw_data = __read_nvm_ldsu_descriptors(lds_interface)
        descriptor = {
            "manufacturer": "BRT Systems Pte Ltd.",
            "product_name": bytes([c for c in ldsu_des_raw_data[0x20:0x40] if c != 0xff and c != 0x00]).decode('utf-8'),
            "product_version": str(ldsu_des_raw_data[2]) + "." + str(ldsu_des_raw_data[3]),
            "uuid": bytes(ldsu_des_raw_data[16:30]).decode('utf-8') + str(int.from_bytes(ldsu_des_raw_data[30:32], 'little')).zfill(5),
        }
        return descriptor
    except Exception as ex:
        raise (ex)
