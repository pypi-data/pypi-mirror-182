"""
This module helps to convert the lds data to various formats

"""


def bcd_to_decimal(data: int) -> int:
    """
    Function to convert bcd data to decimal

    Args:
        data (int): number to convert

    Raises:
        ValueError: Raises if invalid data occurs

    Returns:
        int: return decimal data
    """
    data_str = format(data, 'b')
    number_of_zeros_to_append = (4 - len(data_str) % 4)
    data_str = (number_of_zeros_to_append * '0') + data_str
    nibbles = [int(data_str[i:i + 4], 2) for i in range(0, len(data_str), 4)]
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


def byte_to_version(byte_data: int) -> str:
    """
    Function to convert byte to version string M:m
    Args:
        byte_data (int): data to convert to version

    Returns:
        str: version string
    """
    major = str((byte_data >> 4) & 0x0f)
    minor = str(byte_data & 0x0f)
    return ".".join([major, minor])


def bytes_to_date(bytes: list) -> str:
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
    date = bcd_to_decimal(date)
    month = bcd_to_decimal(month)
    year = bcd_to_decimal(int.from_bytes(year, 'little'))
    if (date > 31) or (month > 12):
        return None
    return ":".join([str(date), str(month), str(year)])


def to_board_voltage(bytes: list, ref=3300, resolution=1024) -> int:
    """
    Function to convert the list of bytes to board voltage

    Args:
        bytes (list): int list to convert
        ref (int, optional): reference voltage
        resolution (int, optional): resolution

    Returns:
        int: ldsu board voltage
    """
    raw_data = int.from_bytes(bytes, 'little')
    voltage = ((raw_data * ref) / resolution) / 0.46
    return round(voltage)


def to_sensor_voltage(bytes: list) -> int:
    """
    Function to convert raw data to sensor voltage

    Args:
        bytes (list): list of two bytes

    Returns:
        int : Converted sensor voltage
    """
    raw_data = int.from_bytes(bytes, 'big')
    return round(((raw_data * 3300) / 1024), 0)


def convert_raw_data_to_ec(bytes: list, calibration_data: dict) -> float:
    """
    Function to convert raw data to EC value

    Args:
        bytes (list): list of two bytes to convert
        calibration_data (dict): EC Calibration data

    Returns:
        float: EC Value
    """

    if (calibration_data == None):
        return 0
    tcoeff = 1.0
    raw_data = to_sensor_voltage(bytes)
    m = calibration_data['slope']
    x1 = calibration_data['x1']
    y1 = calibration_data['y1']
    ec = ((m * (raw_data - x1) + y1) / tcoeff)
    if (ec < 0):
        ec = 0
    return round(ec, 3)


def convert_raw_data_to_salinity(bytes: list, calibration_data: dict) -> float:
    """
    Function to convert raw data to Salinity value

    Args:
        bytes (list): list of two bytes to convert
        calibration_data (dict): Salinity Calibration data

    Returns:
        float: Salinity Value
    """

    if (calibration_data == None):
        return 0
    ec = convert_raw_data_to_ec(bytes, calibration_data)
    salinity = 0
    if (ec > 6.2):
        salinity = 0.0014 * (pow(ec, 2)) + 0.5923*(ec) - 0.364
    else:
        salinity = -0.0012 * (pow(ec, 3)) + 0.0181 * \
            (pow(ec, 2)) + (0.4758 * ec) + 0.0016
    return round(salinity, 3)


def convert_raw_data_to_ORP(bytes: list, calibration_data: dict) -> float:
    """
    Function to convert raw data to ORP value

    Args:
        bytes (list): list of two bytes to convert 
        calibration_data (dict): ORP Calibration data

    Returns:
        float: ORP Value
    """

    if (calibration_data == None):
        return 0
    voltage = calibration_data['voltage']
    buffer_solution = calibration_data['buffer_solution']
    raw_data = to_sensor_voltage(bytes)
    return buffer_solution + 2 * (voltage - raw_data)


def convert_raw_data_to_pH(bytes: list, calibration_data: dict) -> float:
    """
    Function to convert raw data to pH value

    Args:
        bytes (list): list of two bytes to convert 
        calibration_data (dict): pH Calibration data

    Returns:
        float: pH Value
    """

    if (calibration_data == None):
        return 0
    gain = calibration_data['gain']
    offset = calibration_data['offset']
    raw_data = to_sensor_voltage(bytes)
    evalue = (2000 - raw_data) / gain
    return round(7 - ((evalue - offset) / (0.1984 * (25 + 273.15))), 3)


def convert_raw_data_to_DO(bytes: list, calibration_data: dict, temperature=25) -> float:
    """
    Function to convert raw data to DO value

    Args:
        bytes (list): list of two bytes to convert 
        calibration_data (dict): DO Calibration data

    Returns:
        float: DO Value
    """

    if (calibration_data == None):
        return 0
    DO_table = [
        14460, 14220, 13820, 13440, 13090, 12740, 12420, 12110, 11810, 11530,
        11260, 11010, 10770, 10530, 10300, 10080, 9860, 9660, 9460, 9270,
        9080, 8900, 8730, 8570, 8410, 8250, 8110, 7960, 7820, 7690,
        7560, 7430, 7300, 7180, 7070, 6950, 6840, 6730, 6630, 6530, 6410]

    voltage = calibration_data['voltage']
    c_temperature = calibration_data['temperature']
    saturation = (voltage + ((int)(35 * temperature)) - (c_temperature * 35))
    raw_data = to_sensor_voltage(bytes)
    DO = round((raw_data * DO_table[temperature] / saturation) / 1000, 3)
    return saturation, DO
