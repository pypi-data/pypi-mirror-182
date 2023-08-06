"""This module has checksum functions"""


def __update_crc(crc_acc_in: int, data: int, poly=0x1021) -> int:
    crc_acc_in = (crc_acc_in ^ (data << 8)) & 0xffff
    for i in range(0, 8):
        if (crc_acc_in & 0x8000) == 0x8000:
            crc_acc_in <<= 1
            crc_acc_in = (crc_acc_in ^ poly)
        else:
            crc_acc_in <<= 1
    return crc_acc_in


def ldsbus_calculate_checksum(buffer: list, poly=0x1021, initial_value=0xffff):
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
        crc_acc = __update_crc(crc_acc, data, poly=poly) & 0xffff

    return crc_acc


def xor_checksum(data: list, initial_value=0) -> int:
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
