import os
import time
import smbus
import RPi.GPIO



# Get I2C bus
bus = smbus.SMBus(1)

# MMA8452Q address, 0x1D(28)
# Select Control register, 0x2A(42)
#		0x00(00)	StandBy mode
bus.write_byte_data(0x1D, 0x2A, 0x00)
# MMA8452Q address, 0x1C(28)
# Select Control register, 0x2A(42)
#		0x01(01)	Active mode
bus.write_byte_data(0x1D, 0x2A, 0x01)
# MMA8452Q address, 0x1C(28)
# Select Configuration register, 0x0E(14)
#		0x00(00)	Set range to +/- 2g
bus.write_byte_data(0x1D, 0x0E, 0x00)
os.system("amixer set PCM -- 100% &")
os.system("chromium-browser -kiosk -incognito http://127.0.0.1/autest.html &")
time.sleep(0.5)

while(1):
	# MMA8452Q address, 0x1C(28)
	# Read data back from 0x00(0), 7 bytes
	# Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
	data = bus.read_i2c_block_data(0x1D, 0x00, 7)
    
	# Convert the data
	xAccl = (data[1] * 256 + data[2]) / 16
	if xAccl > 2047 :
		xAccl -= 4096

	yAccl = (data[3] * 256 + data[4]) / 16
	if yAccl > 2047 :
		yAccl -= 4096

	zAccl = (data[5] * 256 + data[6]) / 16
	if zAccl > 2047 :
		zAccl -= 4096
		
    #os.system("sudo rm -r ~/.cache/chromium/Default/Cache/* ")
# front x
	if ( (xAccl<-300)and(-300 < yAccl < 300) and (-300 < zAccl < 300) ):
		#response = urllib.request.urlopen('http://python.org/')
		#html = response.read()
		f= open("/var/www/html/Channel1.txt","r")
		response=f.read()
		f.close
		f= open("/var/www/html/javascript.php","w+")
		f.write(response)
		f.close
		
		f= open("/var/www/html/javascript.php","r")
		f.close
# back x
	if ((xAccl > 300) and (-300 < yAccl < 300) and (-300 < zAccl < 300)):
		#os.system("chromium-browser ")
		f= open("/var/www/html/Channel2.txt","r")
		response=f.read()
		f.close
		f= open("/var/www/html/javascript.php","w+")
		f.write(response)
		f.close
		
		f= open("/var/www/html/javascript.php","r")
		f.close
#front y
	if ((yAccl < -300) and (-300 < xAccl < 300) and (-300 < zAccl < 300)):
		#os.system("chromium-browser ")
		f= open("/var/www/html/Channel3.txt","r")
		response=f.read()
		f.close
		f= open("/var/www/html/javascript.php","w+")
		f.write(response)
		f.close
		
		f= open("/var/www/html/javascript.php","r")
		f.close
#back y
	if ((yAccl > 300) and (-300 < xAccl < 300) and (-300 < zAccl < 300)):
		#os.system("chromium-browser ")
		f= open("/var/www/html/Channel4.txt","r")
		response=f.read()
		f.close
		f= open("/var/www/html/javascript.php","w+")
		f.write(response)
		f.close
		
		f= open("/var/www/html/javascript.php","r")
		f.close
#front z
	if ((zAccl < -300) and (-300 < xAccl < 300) and (-300 < yAccl < 300)):
		#os.system("chromium-browser ")
		f= open("/var/www/html/Channel5.txt","r")
		response=f.read()
		f.close
		
		
		
		f= open("/var/www/html/javascript.php","w+")
		
		f.write(response)
		f.close
		
		f= open("/var/www/html/javascript.php","r")
		f.close
#back z
	if ((zAccl > 300) and (-300 < xAccl < 300) and (-300 < yAccl < 300)):
		f= open("/var/www/html/Channel6.txt","r")
		response=f.read()
		f.close
		
		
		f= open("/var/www/html/javascript.php","w+")
		f.write(response)
		f.close
		
		
		f= open("/var/www/html/javascript.php","r")
		
		f.close
	print("xxxxx: /n/r")
	print(xAccl)
	print("yAccl: /n/r")
	print(yAccl)
	print("zAccl :")
	print(zAccl)
	time.sleep(0.7)


"""
# Output data to screen
#print "Acceleration in X-Axis : %d" %xAccl
##print "Acceleration in Y-Axis : %d" %yAccl
#print "Acceleration in Z-Axis : %d" %zAccl
"""
