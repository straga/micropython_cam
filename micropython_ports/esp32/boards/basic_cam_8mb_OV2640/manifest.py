folder_board = "STRAGA_factory_8mb"

freeze('$(PORT_DIR)/modules',  ('_boot.py', 'flashbdev.py','inisetup.py'))
freeze('$(MPY_DIR)/tools', ('upip_utarfile.py'))
freeze('$(MPY_DIR)/ports/esp8266/modules', 'ntptime.py')
freeze('$(MPY_DIR)/drivers/onewire')
include("$(MPY_DIR)/extmod/webrepl/manifest.py")

# freeze('$(PORT_DIR)/boards/modules/ftp_recovery')
# freeze('$(PORT_DIR)/boards/modules/uiot_control')


#freeze('$(MPY_DIR)/tools', ('upip.py', 'upip_utarfile.py'))

