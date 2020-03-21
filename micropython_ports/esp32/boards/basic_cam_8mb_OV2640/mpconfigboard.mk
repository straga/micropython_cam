#ESPIDF = /upy/esp-idf/
#PORT = /dev/ttyUSB0
#FLASH_MODE = dio
#FLASH_SIZE = 16MB


SDKCONFIG += boards/sdkconfig.base
SDKCONFIG += boards/sdkconfig.spiram
SDKCONFIG += boards/sdkconfig.esp32cam_OV2640

SDKCONFIG += boards/STRAGA_factory_8mb/sdkconfig.mod
PART_SRC = boards/STRAGA_factory_8mb/partitions.csv
FROZEN_MANIFEST = boards/STRAGA_factory_8mb/manifest.py