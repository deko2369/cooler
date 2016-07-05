# -*- coding: utf-8 -*-

import unittest

from mock import patch, MagicMock

from cooler.lib.temperature import Temperature

class TestTemperature(unittest.TestCase):
    def setUp(self):
        self.temperature = Temperature()
 
    def test_initialize(self):
        self.assertEqual(self.temperature.spi_bus, 0)
        self.assertEqual(self.temperature.spi_device, 0)
        self.assertEqual(self.temperature.channel, 0)
        self.assertEqual(self.temperature.ref_volt, 5.0)

    def test_make_send_data(self):
        self.assertEqual(self.temperature._Temperature__make_send_data(),
                         0b01101000)

    @patch('spidev.SpiDev')
    def test_get_temperature(self, SpiDev):
        spi_stub = MagicMock()
        spi_stub.open = MagicMock()
        # if temperature = 24 C and ref_volt = 5V,
        # returned raw_value is 70
        spi_stub.xfer2 = MagicMock(return_value=[0, 70])

        SpiDev.return_value = spi_stub

        self.assertEqual(self.temperature.get_temperature(),
                         24)


if __name__ == '__main__':
    unittest.main()

