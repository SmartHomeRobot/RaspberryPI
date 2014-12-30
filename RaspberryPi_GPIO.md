# 1.Install python-dev
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python-dev -y

# 2.Install pip
`sudo apt-get install python-pip`

# 3.Install rpi.gpio
`sudo pip install rpi.gpio`

# 4.Install WiringPi
    git clone git://git.drogon.net/wiringPi

    cd wiringPi
    git pull origin

    cd wiringPi
    ./build
# 4. Samples
>Connect a led + pin to the board 11 pin,the other to the 6 pin as gound.

![](http://img.blog.csdn.net/20140726111027622?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveHVrYWk4NzExMDU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![](http://img.blog.csdn.net/20140726111041240?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveHVrYWk4NzExMDU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 4.1 rpi.gpio

### 4.1.1 led.py
    # -*- coding: utf-8 -*-  
    import RPi.GPIO as GPIO  
    import time  
    # BOARD编号方式，基于插座引脚编号  
    GPIO.setmode(GPIO.BOARD)  
    # 输出模式  
    GPIO.setup(11, GPIO.OUT)  
      
    while True:  
        GPIO.output(11, GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(11, GPIO.LOW)  
        time.sleep(1) 

### 4.1.2 use root to run led.py
`sudo python led.py`

## 4.2 WiringPi

### 4.2.1 blink.c
    #include <stdio.h>
    #include <wiringPi.h>

    // LED Pin - wiringPi pin 0 is BCM_GPIO 17.

    #define LED     0

    int main (void)
    {
      printf ("Raspberry Pi blink\n") ;

      wiringPiSetup () ;
      pinMode (LED, OUTPUT) ;

      for (;;)
      {
        digitalWrite (LED, HIGH) ;  // On
        delay (500) ;               // mS
        digitalWrite (LED, LOW) ;   // Off
        delay (500) ;
      }
      return 0 ;
    }

### 4.2.2 compile
`gcc -Wall -o blink blink.c -lwiringPi`    
-lwiringPi表示动态加载wiringPi共享库

### 4.2.3 use root to run
`sudo ./blink`

## 4.3 webiopi

### 4.3.1 download weboipi
### 4.3.2 install weboipi

$ tar xvzf WebIOPi-x.y.z.tar.gz  
$ cd WebIOPi-x.y.z  
$ sudo ./setup.sh

### 4.3.3 

