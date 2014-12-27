# 1.修改/etc/network/interfaces 文件

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

# 2.输入sudo ifup wlan0重新启动无线网卡
# 3.Static IP

    auto lo
    iface lo inet loopback

    iface eth0 inet dhcp

    allow-hotplug wlan0
    iface wlan0 inet manual
    address 192.168.1.110
    netmask 255.255.255.0
    gateway 192.168.1.1
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp
# 4.scan
    # 扫描热点
    wpa_cli scan
    # 把扫描结果输出到标准输出中
    wpa_cli scan_result


