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
### 4.3.2 SFTP
sftp 是一个交互式文件传输程式。它类似于 ftp, 但它进行加密传输，比FTP有更高的安全性。下边就简单介绍一下如何远程连接主机，进行文件的上传和下载，以及一些相关操作。
举例，如远程主机的 IP 是 202.206.64.33或者是域名www.hebust.edu.cn,用户名是  fyt ,在命令行模式下:sftp fyt@202.206.64.33或者  fyt@www.hebust.edu.cn。回车提示输入密码。进入提示符
sftp>

如果登陆远程机器不是为了上传下载文件，而是要修改远程主机上的某些文件。可以
ssh  fyt@202.206.64.33 （其实sftp就是ssh 的一个程式。）
sftp> get /var/www/fuyatao/index.php  /home/fuyatao/
这条语句将从远程主机的  /var/www/fuyatao/目录下将 index.php 下载到本地  /home/fuyatao/目录下。
sftp> put /home/fuyatao/downloads/Linuxgl.pdf /var/www/fuyatao/
这条语句将把本地 /home/fuyatao/downloads/目录下的 linuxgl.pdf文件上传至远程主机/var/www/fuyatao/ 目录下。
你如果不知道远程主机的目录是什么样， pwd命令可以帮您查询远程主机的当前路径。查询本机当前工作目录 lpwd.
改变路径可以用cd ，改变本机路径可以用 lcd;
ls rm rmdir mkdir 这些命令都可以使用。同理调用本机都是加 l , 即 lls lrm.
要离开sftp，用exit 或quit、 bye 均可。详细情况可以查阅 man  sftp.
### 4.3.2 install weboipi

$ tar xvzf WebIOPi-x.y.z.tar.gz  
$ cd WebIOPi-x.y.z  
$ sudo ./setup.sh

### 4.3.3 

