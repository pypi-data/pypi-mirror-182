import sys

if sys.version_info >= (3, 8, 0):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from typing import Tuple

from liblds.interface.ldsbus_interface import LDSBusInterface
from liblds.commands.ldsbus_commands import read_n
from liblds.log import lds_logging as log
from liblds.utils.converters import byte_to_version, bytes_to_date
from liblds.utils.checksum import xor_checksum


class LDSBusCalibrationError(Exception):
    ...


class CalibrationHeader(TypedDict):
    """
    Class for Calibration info header
    """
    version: str
    date: str


class pHSensorCalibrationInfo(TypedDict):
    pH: int
    gain: int
    offset: int
    temperature: int


class ORPSensorCalibrationInfo(TypedDict):
    voltage: int
    temperature: int
    buffer_solution: int


class ECSensorCalibrationInfo(TypedDict):
    x1: int
    y1: int
    x2: int
    y2: int
    slope: int
    origin: int
    probe: int
    temperature: int


class SalinitySensorCalibrationInfo(TypedDict):
    x1: int
    y1: int
    x2: int
    y2: int
    slope: int
    origin: int
    probe: int
    temperature: int


class DOSensorCalibrationInfo(TypedDict):
    voltage: int
    temperature: int


def __read_nvm_calibration(ldsbus_interface: LDSBusInterface) -> Tuple:
    """"""
    try:
        data = []
        for read_address in range(0x300, 0x380, 0x20):
            i2c_dev_address = (0x50 | ((read_address >> 8) & 0x3))
            register_address = read_address & 0xff
            rdata = read_n(ldsbus_interface, i2c_dev_address,
                           register_address, 32)
            if rdata != None:
                data += rdata
        return data
    except Exception as ex:
        log.error(ex)


def __parse_calibration_info_header(data: list) -> CalibrationHeader:

    try:
        if len(data) != 5:
            raise ValueError("Invalid data to parse")
        (version, *date) = data
        return {"version": byte_to_version(version), 'date': bytes_to_date(date)}
    except ValueError as error:
        log.error("Sensor not calibrated.")


def ldsu_get_ORP_calibration(ldsbus_interface: LDSBusInterface) -> ORPSensorCalibrationInfo:
    """
    Function to get the ORP Sensor Calibration data

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Raises:
        LDSBusCalibrationError: Rasises calibration error if not calibrated or unable to get the calibration information

    Returns:
        ORPSensorCalibrationInfo (TypedDict): Returns calibration information on success otherwise None
    """
    try:
        response = __read_nvm_calibration(ldsbus_interface)
        if (response is None) or (len(response) != 128):
            raise LDSBusCalibrationError(
                "Unable to read calibration information")
        calibration_header = __parse_calibration_info_header(response[:5])
        if (calibration_header == None):
            raise LDSBusCalibrationError("Sensor not calibrated")

        (sensor_index, data_length, *data) = response[5:]
        (*calibration_data, checksum) = data[:data_length + 1]
        size_of_calibration = data_length + 7
        calculated_checksum = xor_checksum(response[:size_of_calibration])
        if (calculated_checksum != checksum):
            raise LDSBusCalibrationError("Invalid calibration data")
        cal_data = {
            'voltage': int.from_bytes(calibration_data[0:2], 'little'),
            'temperature': round(int.from_bytes(calibration_data[2:6], 'little') / 1024, 3),
            'buffer_solution': 225
        }
        if (data_length == 8):
            cal_data['buffer_solution'] = int.from_bytes(
                calibration_data[6:8], 'little'),
        return cal_data

    except Exception as ex:
        log.error(ex)


def ldsu_get_pH_calibration(ldsbus_interface: LDSBusInterface) -> pHSensorCalibrationInfo:
    """
    Function to get the pH Sensor Calibration data

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Raises:
        LDSBusCalibrationError: Rasises calibration error if not calibrated or unable to get the calibration information

    Returns:
        pHSensorCalibrationInfo (TypedDict): Returns calibration information on success otherwise None
    """

    try:
        response = __read_nvm_calibration(ldsbus_interface)
        if (response is None) or (len(response) != 128):
            raise LDSBusCalibrationError(
                "Unable to read calibration information")
        calibration_header = __parse_calibration_info_header(response[:5])
        if (calibration_header == None):
            raise LDSBusCalibrationError("Sensor not calibrated")

        (sensor_index, data_length, *data) = response[5:]
        (*calibration_data, checksum) = data[:data_length + 1]
        size_of_calibration = data_length + 7
        calculated_checksum = xor_checksum(response[:size_of_calibration])
        if (calculated_checksum != checksum):
            raise LDSBusCalibrationError("Invalid calibration data")
        cal_data = {
            'pH': int.from_bytes(calibration_data[0:2], 'little'),
            'gain': round(int.from_bytes(calibration_data[2:4], 'little') / 1024, 3),
            'offset': round(int.from_bytes(calibration_data[4:6], 'little') / 1024, 3),
            'temperature': round(int.from_bytes(calibration_data[6:8], 'little') / 1024, 3),
        }
        if (data_length == 10):
            cal_data['offset'] = round(int.from_bytes(
                calibration_data[4:8], 'little') / 1024, 3)
            cal_data['temperature'] = round(int.from_bytes(
                calibration_data[8:10], 'little') / 1024, 3)
        return cal_data

    except Exception as ex:
        log.error(ex)


def ldsu_get_EC_calibration(ldsbus_interface: LDSBusInterface) -> ECSensorCalibrationInfo:
    """
    Function to get the EC Sensor Calibration data

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Raises:
        LDSBusCalibrationError: Rasises calibration error if not calibrated or unable to get the calibration information

    Returns:
        ECSensorCalibrationInfo (TypedDict): Returns calibration information on success otherwise None
    """

    try:
        response = __read_nvm_calibration(ldsbus_interface)
        if (response is None) or (len(response) != 128):
            raise LDSBusCalibrationError(
                "Unable to read calibration information")
        calibration_header = __parse_calibration_info_header(response[:5])
        if (calibration_header == None):
            raise LDSBusCalibrationError("Sensor not calibrated")

        (sensor_index, data_length, *data) = response[5:]
        (*calibration_data, checksum) = data[:data_length + 1]
        size_of_calibration = data_length + 7
        calculated_checksum = xor_checksum(response[:size_of_calibration])
        if (calculated_checksum != checksum):
            raise LDSBusCalibrationError("Invalid calibration data")

        calibration_key_parameters = [
            "x1", "y1", "x2", "y2", "slope", "origin", "probe", "temperature"]
        cal_data = [round((int.from_bytes(calibration_data[i:i+4], 'little') / 1024.0), 3)
                    for i in range(0, data_length, 4)]
        return {calibration_key_parameters[i]: cal_data[i]
                for i in range(len(calibration_key_parameters))}
    except Exception as ex:
        log.error(ex)


def ldsu_get_salinity_calibration(ldsbus_interface: LDSBusInterface) -> SalinitySensorCalibrationInfo:
    """
    Function to get the Salinity Sensor Calibration data

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Raises:
        LDSBusCalibrationError: Rasises calibration error if not calibrated or unable to get the calibration information

    Returns:
        SalinitySensorCalibrationInfo (TypedDict): Returns calibration information on success otherwise None
    """
    try:
        response = __read_nvm_calibration(ldsbus_interface)
        if (response is None) or (len(response) != 128):
            raise LDSBusCalibrationError(
                "Unable to read calibration information")
        calibration_header = __parse_calibration_info_header(response[:5])
        if (calibration_header == None):
            raise LDSBusCalibrationError("Sensor not calibrated")

        (sensor_index, data_length, *data) = response[5:]
        (*calibration_data, checksum) = data[:data_length + 1]
        size_of_calibration = data_length + 7
        calculated_checksum = xor_checksum(response[:size_of_calibration])
        if (calculated_checksum != checksum):
            raise LDSBusCalibrationError("Invalid calibration data")

        calibration_key_parameters = [
            "x1", "y1", "x2", "y2", "slope", "origin", "probe", "temperature"]
        cal_data = [round((int.from_bytes(calibration_data[i:i+4], 'little') / 1024.0), 3)
                    for i in range(0, data_length, 4)]
        return {calibration_key_parameters[i]: cal_data[i]
                for i in range(len(calibration_key_parameters))}
    except Exception as ex:
        log.error(ex)


def ldsu_get_DO_calibration(ldsbus_interface: LDSBusInterface) -> DOSensorCalibrationInfo:
    """
    Function to get the DO Sensor Calibration data

    Args:
        ldsbus_interface (LDSBusInterface): COM Port object to communicate to the device

    Raises:
        LDSBusCalibrationError: Rasises calibration error if not calibrated or unable to get the calibration information

    Returns:
        DOSensorCalibrationInfo (TypedDict): Returns calibration information on success otherwise None
    """

    try:
        response = __read_nvm_calibration(ldsbus_interface)
        if (response is None) or (len(response) != 128):
            raise LDSBusCalibrationError(
                "Unable to read calibration information")
        calibration_header = __parse_calibration_info_header(response[:5])
        if (calibration_header == None):
            raise LDSBusCalibrationError("Sensor not calibrated")

        (sensor_index, data_length, *data) = response[5:]
        (*calibration_data, checksum) = data[:data_length + 1]
        size_of_calibration = data_length + 7
        calculated_checksum = xor_checksum(response[:size_of_calibration])
        if (calculated_checksum != checksum):
            raise LDSBusCalibrationError("Invalid calibration data")
        return {
            'voltage': int.from_bytes(calibration_data[0:2], 'little'),
            'temperature': round(int.from_bytes(calibration_data[2:6], 'little') / 1024, 3)
        }
    except Exception as ex:
        log.error(ex)
