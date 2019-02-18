## branch deploy

### set bbr

```
# config BBR
modprobe tcp_bbr
echo "tcp_bbr" >> /etc/modules-load.d/modules.conf
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf

# load BBR
sysctl -p

# verify bbr
sysctl net.ipv4.tcp_available_congestion_control
sysctl net.ipv4.tcp_congestion_control
lsmod | grep bbr
```

### Install shadowsocks
```
git clone -b master https://github.com/shadowsocks/shadowsocks.git
cd shadowsocks
python setup.py install
```

### deploy.py
Prepare config files and prepare init scripts.
```
python deploy.py SERVER_IP, PORT, PASSWORD
```
