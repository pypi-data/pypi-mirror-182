import logging
import coloredlogs

coloredlogs.install(
    fmt='%(asctime)s:%(msecs)03d %(levelname)s %(message)s')


def info(msg, *args, **kwargs):
    logging.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    logging.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    logging.error(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    logging.critical(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    logging.debug(msg, *args, **kwargs)


def print_sensor_actuator_list(list_of_sensors):

    if len(list_of_sensors) == 0:
        warning("No sensors found.")
        return
    sa_str = "Sensors and actuators"
    info(sa_str)
    info("="*len(sa_str))
    for sa in list_of_sensors:
        info("ID: %d", sa['id'])
        info("\t Manufacturer : %s", sa['manufacturer'])
        info("\t Part Number : %s", sa['part_number'])
        info("\t I2C Address : %s", sa['i2c_address'])
        info("\t Maximum report rate (millsecs) : %s", sa['report_rate_ms'])


def print_ldsu_descriptor(descriptor):
    desc_str = "LDSU Descriptor"
    info(desc_str)
    info("="*len(desc_str))
    info("\t Manufacturer : %s", descriptor['manufacturer'])
    info("\t Product Name : %s", descriptor['product_name'])
    info("\t Product Version : %s", descriptor['product_version'])
    info("\t UUID : %s", descriptor['uuid'])
