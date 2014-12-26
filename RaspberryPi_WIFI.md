 修改 /etc/network/interfaces 文件

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
