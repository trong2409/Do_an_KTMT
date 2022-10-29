#!/bin/bash
rm -f ~/.conf
rm -f ~/server_opc/.conf

if [ $1 != "" ]
then
	rm -f ~/server_opc/server.py
	rm -f ~/server_opc/serialThread.py
	rm -f ~/server_opc/DRIVER_PAUL_HW.ino.hex

	echo '{"ip": null, "port": "53535", "station": "'$1'", "id": null, "version": "0.0.1"}' > ~/server_opc/.conf
	case $1 in
		01 | 02 | 03)
		cp -r ~/server_opc/server_010203/* ~/server_opc/
		;;

		04 | 05 | 06)
		cp -r ~/server_opc/server_$1/* ~/server_opc/
		;;
	esac
	chmod a+x ~/server_opc/server.py
	chmod a+x ~/server_opc/serialThread.py
	cd ~/server_opc
	chmod a+x download_driver.sh
	bash download_driver.sh
else
	echo "Please input station Number"
	echo "Example: bash setup.sh 01"
fi
exit
