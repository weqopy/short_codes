# 原生镜像、Docker

[Operating system images - Raspberry Pi](https://www.raspberrypi.com/software/operating-systems/)

### Apt

```bash
# 清华 apt 源

sudo vi /etc/apt/sources.list

deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ bullseye main non-free contrib rpi
# deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ bullseye main non-free contrib rpi

# docker 权限
sudo usermod -aG docker $USER
```

### OpenWrt

[在树莓派上使用Dockers运行Openwrt并作为主路由器的旁路由](https://www.ahsup.top/post/linux/openwrt/)

[docker容器网络更改_我是罗易呀！的博客-CSDN博客_docker修改网络](https://blog.csdn.net/Qcg0223/article/details/108053460)

```bash
docker network create -d macvlan --subnet=192.168.31.0/24 --gateway=192.168.31.1 -o parent=eth0 macnet

sudo docker pull registry.cn-shanghai.aliyuncs.com/suling/openwrt:rpi2

sudo docker run --restart always --name openwrt -d --network macnet --privileged registry.cn-shanghai.aliyuncs.com/suling/openwrt:rpi2 /sbin/init

```

### Portainer

```bash
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock --restart=always --name portainer portainer/portainer-ce
```

### NetData

```bash
docker run -d --name=netdata \
  -p 19999:19999 \
  -v netdataconfig:/etc/netdata \
  -v netdatalib:/var/lib/netdata \
  -v netdatacache:/var/cache/netdata \
  -v /etc/passwd:/host/etc/passwd:ro \
  -v /etc/group:/host/etc/group:ro \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \
  -v /etc/os-release:/host/etc/os-release:ro \
  --restart unless-stopped \
  --cap-add SYS_PTRACE \
  --security-opt apparmor=unconfined \
  -e NETDATA_CLAIM_TOKEN=VMBH5iZYbOTMesK06OSsbExGytlNjmnM3JB9VBRIozOAfhnCbTh4tY3ByN8aurjczJUenQe3nHkPYXK171yfbviTDdGrwHmu0wawBIK-_GZMMUGmewZRivdP_jXiiJbu4_1_T44 \
  -e NETDATA_CLAIM_URL=https://app.netdata.cloud \
  netdata/netdata
```

### HomeAssistant

```bash
mkdir -P /home/pi/homeassistant

docker run -d \
  --name homeassistant \
  -p 8123:8123 \
  --privileged \
  --restart=unless-stopped \
  -e TZ=Asia/Shanghai \
  -v /home/pi/homeassistant:/config \
  --network=host \
  ghcr.io/home-assistant/raspberrypi4-homeassistant:stable

```

### AdGuard Home

```bash
docker run \
--name adguardhome \
-v /etc/adguardhome/:/opt/adguardhome/work \
-v /etc/adguardhome/:/opt/adguardhome/conf \
-p 53:53/tcp -p 53:53/udp -p 67:67/udp -p 368:68/tcp -p 368:68/udp -p 3080:80/tcp -p 3443:443/tcp -p 853:853/tcp -p 3000:3000/tcp \
--restart=always \
-d adguard/adguardhome

```
