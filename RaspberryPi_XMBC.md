# Install Raspbmc to RaspberryPI by Ubuntu:
## 0.Equipment needed

    1x Raspberry Pi (this must be a Model B device).
    Method of powering the device:
        4xAA batteries to Micro USB
        At least a 1Amp charger @ 5V — please read about the importance of a good quality power supply here
    Class 6 SD card of 2GB or greater capacity. Note: for optimal performance, a Class 10 SD card is recommended. If you are storing Thumbnails on your device an 8GB capacity or greater is recommended.
    Wired network connection (for initial setup), thereafter, unnecessary.
    HDMI cable or RCA video cable with 3.5mm audio cable.


## 1.Insert a SD card and install the Boot File to the SD card
    wget http://svn.stmlabs.com/svn/raspbmc/release/installers/python/install.py
    chmod +x install.py

    sudo python install.py
Lists some like belows:

    quanpower@Ubuntu-dev:~/dev/RaspberryPI$ sudo python install.py 
    /usr/bin/clear
    /sbin/fdisk
    /bin/grep
    /bin/umount
    /bin/mount
    /usr/bin/cut
    /bin/gunzip
    /bin/dd
    /sbin/blockdev

    Raspbmc installer for Linux and OS X
    http://raspbmc.com
    ----------------------------------------
    Please ensure you've inserted your SD card, and press Enter to continue.

    Enter the 'Disk' you would like imaged, from the following list:
    Disk /dev/sda: 163.3 GB, 163314663424 bytes
    Disk /dev/sdb: 7969 MB, 7969177600 bytes

    Enter your choice here (e.g. 'mmcblk0' or 'sdd'): sdb
    It is your own responsibility to ensure there is no data loss! Please backup your system before imaging
    You should also ensure you agree with the Raspbmc License Agreeement
    Are you sure you want to install Raspbmc to '/dev/sdb' and accept the license agreement? [y/N] 
    y
    It appears that the Raspbmc installation image has already been downloaded. Would you like to re-download it? [y/N] 
    n

    Unmounting all partitions...
    Please wait while Raspbmc is installed to your SD card...
    This may take some time and no progress will be reported until it has finished.
    0+2230 records in
    0+2230 records out
    76800000 bytes (77 MB) copied, 15.8568 s, 4.8 MB/s
    Installation complete.
    Would you like to setup your post-installation settings [ADVANCED]? [y/N] 
    n

    Raspbmc is now ready to finish setup on your Pi, please insert the SD card with an active internet connection

## 2.Install Raspbmc 
### 2.1 Put this SD card to Raspberry PI
### 2.2 plug the power and the net wire,power on! 
### 2.3 install Raspbmc
    it will download installers from the Raspbmc update server,includes root filesystem,kernel modules,kernel and bootloader
### 2.4 after reboot will run first config

## 3.Install XBMC
## 4.XBMC settings
### 4.1 Fonts--Arial,Language--Chinese,TimeZone--China
### 4.2 WebServer Port:80
### 4.3 Install XBMC Nightly
### 4.4 Add video sources:SMB,NFS

## 4.Add-ones

## 5.XBMC Remote
yatse
reference:http://www.chiphell.com/thread-662458-1-1.html
