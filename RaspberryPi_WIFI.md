1.修改/etc/network/interfaces 文件

sudo vim /etc/network/interfaces

修改后文件内容如下：

auto lo

iface lo inet loopback
iface eth0 inet dhcp

auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-ssid "quanpower"
wpa-psk "password"

2.输入sudo ifup wlan0重新启动无线网卡
3.Static IP
4.scan
#扫描热点
wpa_cli scan
#把扫描结果输出到标准输出中
wpa_cli scan_result
5.修改配置文件方法
    前面已经通过GUI的方法修改了wifi配置文件，下面查看相关的配置文件来“逆向”上述过程。
    【查看interfaces】——位于/etc/networks
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

    其实该文件配置前后是一样的，树莓派的默认配置中便包含了一个wlan0，只是该wlan0没有指定AP也没有指定AP的密码。通过wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf可获知wifi的配置文件位于/etc/wpa_supplicant目录下。
    【结论】该文件并没有被改动

    【查看wpa_supplicant.conf】——位于/etc/wpa_supplicant
    cd /etc/wpa_supplicant
    sudo cat wpa_supplicant.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="AP名称"
        psk="AP密码"
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        auth_alg=OPEN
}

    树莓派安装完成之后，该配置文件的头两行已经存在，通过GUI操作增加便是network部分。其中ssid参数为AP热点名称，psk为AP密码。另外还需要注意一点，network中每行均已TAB键开始。
    【结论】该文件增加了network部分。

