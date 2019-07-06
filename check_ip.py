"""
通过调用淘宝 IP 服务查询目标 IP 地址信息
"""
import requests
import json


def check_ip(ip):
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip={}".format(ip)
    content = requests.get(apiurl).text
    data = json.loads(content)["data"]
    code = json.loads(content)["code"]

    if code == 0:
        print(
            "ip:{0} from {1} {2} {3} \n".format(
                data["ip"], data["country"], data["region"], data["city"]
            )
        )
    else:
        print(data.encode("utf-8"))


def get_ips():
    # this func should get a file named 'ip.txt' contains ip you want check
    with open("ip.txt", "r") as target:
        ips = target.readlines()
    return ips


def check_ips():
    ips = get_ips()
    for ip in ips:
        check_ip(ip)
