# -*- coding: utf-8 -*-

import spidev

class Temperature:
    """
    Managment class of deriving temperature data from sensor via SPI

    Using electric components:
      - Temperature Sensor: LM35
      - AD Converter: MCP3002
    """

    def __init__(self, spi_bus=0, spi_device=0, channel=0, ref_volt=5.0):
        self.spi_bus = spi_bus
        self.spi_device = spi_device
        self.channel = channel
        self.ref_volt = ref_volt

    def __make_send_data(self):
        # Start(1), SGL/DIFF(1), ODD/SIGN(self.channel), MSBF(1)
        # format: 0b0SGOM000
        #         S=Start, G=SGL/DIFF, O=ODD/SIGN, M=MSBF
        return ((1 << 3) + (1 << 2) + (self.channel << 1) + 1) << 3

    def get_temperature(self):
        try:
            spi = spidev.SpiDev()
            spi.open(self.spi_bus, self.spi_device)

            to_send_data = self.__make_send_data()

            raw_value = spi.xfer2([to_send_data, 0x00])
            adc = (raw_value[0] * 256 + raw_value[1]) & 0x3ff
            volt = adc * self.ref_volt / 1024.0
            # TODO fix temperature error(-10) in my environment
            temperature = (volt * 100.0) - 10.0
        finally:
            spi.close()

        return int(temperature)


# for debug electric circuit
if __name__ == '__main__':
    print Temperature(ref_volt=4.7).get_temperature()

