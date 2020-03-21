Info

https://github.com/tsaarni/micropython-with-esp32-cam/wiki
https://github.com/espressif/esp32-camera

micropython - 8d34344dceb367844b651deccadff2b55f20c55c
_

esp_cam module with resolder - 8/16mb flash

Alredy have micropython and esp-idf

step 1. v4. esp-idf/components

	copy esp-idf_components_esp32-camera to esp-idf/components/esp32-camera	


step 2. micropython/ports/esp32
	git branche/checkout from master to cam
	copy micropython_ports to micropython/ports
	

step 3. Export env
	
	 export PATH="$PATH:$HOME/upy/xtensa-esp32-elf/bin"
	 export IDF_PATH="$HOME/upy/esp-idf"
	 
step 4. Build/Deploy
	
	make -j4 BOARD=cam_8mb
	make -j4 BOARD=basic_cam_8mb_OV2640 PORT=/dev/ttyS3 BAUD=921600 erase
	make -j4 BOARD=basic_cam_8mb_OV2640 PORT=/dev/ttyS3 BAUD=921600 deploy
	
step 5. Camera Inii and capture to buff 

	import camera
	camera.init()
	
	buf = camera.capture()
	
step 6. Do file save.py  with code and put on the board.
	
	def save_image(buf, file="test.jpeg"):

    try:
        with open(file, "wb") as f:
            f.write(buf)
    except OSError as e:
        print("exception .. {}".format(e))

    print(file)
    

step 7. Sav buf to flash and get file for view.
	
	imprort save
	save.save_image(buf)
	
	will be test.jpg on flash