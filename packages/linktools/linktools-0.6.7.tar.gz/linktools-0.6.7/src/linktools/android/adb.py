#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author  : Hu Ji
@file    : adb.py
@time    : 2018/11/25
@site    :
@software: PyCharm

              ,----------------,              ,---------,
         ,-----------------------,          ,"        ,"|
       ,"                      ,"|        ,"        ,"  |
      +-----------------------+  |      ,"        ,"    |
      |  .-----------------.  |  |     +---------+      |
      |  |                 |  |  |     | -==----'|      |
      |  | $ sudo rm -rf / |  |  |     |         |      |
      |  |                 |  |  |/----|`---=    |      |
      |  |                 |  |  |   ,/|==== ooo |      ;
      |  |                 |  |  |  // |(((( [33]|    ,"
      |  `-----------------'  |," .;'| |((((     |  ,"
      +-----------------------+  ;;  | |         |,"
         /_)______________(_/  //'   | +---------+
    ___________________________/___  `,
   /  oooooooooooooooo  .o.  oooo /,   \,"-----------
  / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
 /_==__==========__==_ooo__ooo=_/'   /___________,"
"""

import json
import re
from typing import Optional, Any, AnyStr

from .struct import Package, UnixSocket, InetSocket
from .. import utils, resource, tools, config, get_logger
from ..decorator import cached_property
from ..version import __name__ as module_name

_logger = get_logger("android.adb")


class AdbError(Exception):

    def __init__(self, message: str):
        super().__init__(message.rstrip("\r\n"))


class Adb(object):
    _alive_status = ["bootloader", "device", "recovery", "sideload"]

    @classmethod
    def devices(cls, alive: bool = None) -> [str]:
        """
        获取所有设备列表
        :param alive: 只显示在线的设备
        :return: 设备号数组
        """
        devices = []
        result = cls.exec("devices")
        lines = result.splitlines()
        for i in range(1, len(lines)):
            splits = lines[i].split(maxsplit=1)
            if len(splits) >= 2:
                device, status = splits
                if alive is None:
                    devices.append(device)
                elif alive == (status in cls._alive_status):
                    devices.append(device)

        return devices

    @classmethod
    def popen(cls, *args: [Any], **kwargs) -> utils.Popen:
        return tools["adb"].popen(*args, **kwargs)

    @classmethod
    def exec(cls, *args: [Any], input: AnyStr = None, timeout: float = None, ignore_errors: bool = False,
             capture_output: bool = True, output_to_logger: bool = False, **kwargs) -> str:
        """
        执行命令
        :param args: 命令
        :param input: 输入
        :param timeout: 超时时间
        :param ignore_errors: 忽略错误，报错不会抛异常
        :param capture_output: 捕获输出，默认为True
        :param output_to_logger: 把输出打印到logger中
        :return: 如果是不是守护进程，返回输出结果；如果是守护进程，则返回Popen对象
        """
        if output_to_logger:
            if not capture_output:
                capture_output = True
                _logger.warning("output_to_logger argument needs to be used with capture_output argument")

        process = cls.popen(
            *args,
            capture_output=capture_output,
            **kwargs
        )
        out, err = process.communicate(
            input=input,
            timeout=timeout,
            ignore_errors=ignore_errors
        )

        if output_to_logger:
            if out:
                message = out.decode(errors="ignore") if isinstance(out, bytes) else out
                _logger.info(message.rstrip())
            if err:
                message = err.decode(errors="ignore") if isinstance(err, bytes) else err
                _logger.error(message.rstrip())

        if not ignore_errors and process.returncode != 0 and not utils.is_empty(err):
            err = err.decode(errors='ignore')
            if not utils.is_empty(err):
                raise AdbError(err)

        return out.decode(errors='ignore') if out is not None else ""


class Device(object):

    def __init__(self, device_id: str = None):
        """
        :param device_id: 设备号
        """
        if device_id is None:
            devices = Adb.devices(alive=True)
            if len(devices) == 0:
                raise AdbError("no devices/emulators found")
            elif len(devices) > 1:
                raise AdbError("more than one device/emulator")
            self._device_id = next(iter(devices))
        else:
            self._device_id = device_id

    @property
    def config(self) -> dict:
        return config["ANDROID_TOOL_BRIDGE_APK"]

    @cached_property
    def id(self) -> str:
        """
        获取设备号
        :return: 设备号
        """
        return self._device_id

    @cached_property
    def abi(self) -> str:
        """
        获取设备abi类型
        :return: abi类型
        """
        result = self.get_prop("ro.product.cpu.abi")
        if result.find("arm64") >= 0:
            return "arm64"
        elif result.find("armeabi") >= 0:
            return "arm"
        elif result.find("x86_64") >= 0:
            return "x86_64"
        elif result.find("x86") >= 0:
            return "x86"
        raise AdbError("unknown abi: %s" % result)

    @property
    def uid(self) -> int:
        """
        获取shell的uid
        :return: uid
        """
        default = -1
        out = self.shell("echo", "-n", "${USER_ID}")
        uid = utils.int(out, default=default)
        if uid != default:
            return uid
        raise AdbError("unknown adb uid: %s" % out)

    def popen(self, *args: [Any], **kwargs) -> utils.Popen:
        """
        执行命令
        :param args: 命令行参数
        :return: 打开的进程
        """
        args = ["-s", self.id, *args]
        return Adb.popen(*args, **kwargs)

    def exec(self, *args: [Any], **kwargs) -> str:
        """
        执行命令
        :param args: 命令行参数
        :return: adb输出结果
        """
        args = ["-s", self.id, *args]
        return Adb.exec(*args, **kwargs)

    def shell(self, *args: [Any], privilege: bool = False, **kwargs) -> str:
        """
        执行shell
        :param args: shell命令
        :param privilege: 是否以root权限运行
        :return: adb输出结果
        """
        args = ["shell", *args] \
            if not privilege or self.uid == 0 \
            else ["shell", "su", "-c", *args]
        return self.exec(*args, **kwargs)

    def sudo(self, *args: [Any], **kwargs) -> str:
        """
        以root权限执行shell
        :param args: shell命令
        :return: adb输出结果
        """
        kwargs["privilege"] = True
        return self.shell(*args, **kwargs)

    def install(self, *file_path: str, **kwargs) -> str:
        """
        安装apk
        :param file_path: apk文件路径
        :return: adb输出结果
        """
        return self.exec("install", *file_path, **kwargs)

    def uninstall(self, package_name: str, **kwargs) -> str:
        """
        卸载apk
        :param package_name: 包名
        :return: adb输出结果
        """
        return self.exec("uninstall", self.extract_package(package_name), **kwargs)

    def push(self, src: str, dst: str, **kwargs) -> str:
        """
        推送文件到设备
        :param src: 源文件
        :param dst: 目标文件
        :return: adb输出结果
        """
        return self.exec("push", src, dst, **kwargs)

    def pull(self, src: str, dst: str, **kwargs) -> str:
        """
        拉取设备的文件
        :param src: 源文件
        :param dst: 目标文件
        :return: adb输出结果
        """
        return self.exec("pull", src, dst, **kwargs)

    def forward(self, *args, **kwargs) -> str:
        """
        端口转发
        :return: adb输出结果
        """
        return self.exec("forward", *args, **kwargs)

    def reverse(self, *args, **kwargs) -> str:
        """
        端口转发
        :return: adb输出结果
        """
        return self.exec("reverse", *args, **kwargs)

    def call_agent(self, *args: [str], **kwargs) -> str:
        """
        调用辅助apk功能
        :param args: 参数
        :return: 输出结果
        """
        apk_name = self.config["name"]
        apk_md5 = self.config["md5"]
        main_class = self.config["main"]
        start_flag = f"__start_flag_{apk_md5}__"
        end_flag = f"__end_flag_{apk_md5}__"

        apk_path = resource.get_asset_path(apk_name)
        target_dir = self.get_storage_path("apk", apk_md5)
        target_path = self.get_storage_path("apk", apk_md5, apk_name)

        capture_output = kwargs.setdefault("capture_output", True)

        # check apk path
        if not self.is_file_exist(target_path):
            self.shell("rm", "-rf", target_dir)
            self.push(apk_path, target_path)
            if not self.is_file_exist(target_path):
                raise AdbError("%s does not exist" % target_path)
        # set flag if necessary
        if capture_output:
            args = ["--start-flag", start_flag, "--end-flag", end_flag, *args]
        # call apk
        result = self.shell(
            "CLASSPATH=%s" % target_path,
            "app_process", "/", main_class, *args,
            **kwargs
        )
        # parse flag if necessary
        if capture_output:
            begin = result.find(start_flag)
            end = result.rfind(end_flag)
            if begin >= 0 and end >= 0:
                begin = begin + len(start_flag)
                result = result[begin: end]
            elif begin >= 0:
                begin = begin + len(start_flag)
                raise AdbError(result[begin:])
        return result

    def get_prop(self, prop: str, **kwargs) -> str:
        """
        获取属性值
        :param prop: 属性名
        :return: 属性值
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        return self.shell("getprop", prop, **kwargs).rstrip()

    def set_prop(self, prop: str, value: str, **kwargs) -> str:
        """
        设置属性值
        :param prop: 属性名
        :param value: 属性值
        :return: adb输出结果
        """
        args = ["setprop", prop, value]
        return self.shell(*args, **kwargs).rstrip()

    def kill(self, package_name: str, **kwargs) -> str:
        """
        关闭进程
        :param package_name: 关闭的包名
        :return: adb输出结果
        """
        args = ["am", "kill", self.extract_package(package_name)]
        return self.shell(*args, **kwargs).rstrip()

    def force_stop(self, package_name: str, **kwargs) -> str:
        """
        关闭进程
        :param package_name: 关闭的包名
        :return: adb输出结果
        """
        args = ["am", "force-stop", self.extract_package(package_name)]
        return self.shell(*args, **kwargs).rstrip()

    def is_file_exist(self, path: str, **kwargs) -> bool:
        """
        文件是否存在
        :param path: 文件路径
        :return: 是否存在
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        args = ["[", "-a", path, "]", "&&", "echo", "-n ", "1"]
        out = self.shell(*args, **kwargs)
        return utils.bool(utils.int(out, default=0), default=False)

    def get_current_package(self, **kwargs) -> str:
        """
        获取顶层包名
        :return: 顶层包名
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        timeout_meter = utils.TimeoutMeter(kwargs.pop("timeout", None))
        if self.uid < 10000:
            args = ["dumpsys", "activity", "top", "|", "grep", "^TASK", "-A", "1", ]
            out = self.shell(*args, timeout=timeout_meter.get(), **kwargs)
            items = out.splitlines()[-1].split()
            if items is not None and len(items) >= 2:
                return items[1].split("/")[0].rstrip()
        # use agent instead of dumpsys
        out = self.call_agent("common", "--top-package", timeout=timeout_meter.get(), **kwargs)
        if not utils.is_empty(out):
            return out
        raise AdbError("can not fetch top package")

    def get_current_activity(self, **kwargs) -> str:
        """
        获取顶层activity名
        :return: 顶层activity名
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        args = ["dumpsys", "activity", "top", "|", "grep", "^TASK", "-A", "1"]
        result = self.shell(*args, **kwargs)
        items = result.splitlines()[-1].split()
        if items is not None and len(items) >= 2:
            return items[1].rstrip()
        raise AdbError("can not fetch top activity")

    def get_apk_path(self, package: str, **kwargs) -> str:
        """
        获取apk路径
        :return: apk路径
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        timeout_meter = utils.TimeoutMeter(kwargs.pop("timeout", None))
        if self.uid < 10000:
            out = self.shell("pm", "path", package, timeout=timeout_meter.get(), **kwargs)
            match = re.search(r"^.*package:[ ]*(.*)[\s\S]*$", out)
            if match is not None:
                return match.group(1).strip()
        obj = self.get_packages(package, simple=True, timeout=timeout_meter.get(), **kwargs)
        return utils.get_item(obj, 0, "sourceDir", default="")

    def get_package(self, package_name: str, **kwargs) -> Optional[Package]:
        """
        根据包名获取包信息
        :param package_name: 包名
        :return: 包信息
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        args = ["package", "--packages", package_name]
        objs = json.loads(self.call_agent(*args, **kwargs))
        return Package(objs[0]) if len(objs) > 0 else None

    def get_packages(self, *package_names: str, system: bool = None, simple: bool = None, **kwargs) -> [Package]:
        """
        获取包信息
        :param package_names: 需要匹配的所有包名，为空则匹配所有
        :param system: true只匹配系统应用，false只匹配非系统应用，为空则全匹配
        :param simple: 只获取基本信息
        :return: 包信息
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        result = []
        agent_args = ["package"]
        if not utils.is_empty(package_names):
            agent_args.append("--packages")
            agent_args.extend(package_names)
        if system is True:
            agent_args.append("--system")
        elif system is False:
            agent_args.append("--non-system")
        if simple is True:
            agent_args.append("--simple")
        objs = json.loads(self.call_agent(*agent_args, **kwargs))
        for obj in objs:
            result.append(Package(obj))
        return result

    def get_packages_for_uid(self, *uids: int, simple: bool = None, **kwargs) -> [Package]:
        """
        获取指定uid包信息
        :param uids: 需要匹配的所有uid
        :param simple: 只获取基本信息
        :return: 包信息
        """
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        result = []
        agent_args = ["package"]
        if not utils.is_empty(uids):
            agent_args.append("--uids")
            agent_args.extend([str(uid) for uid in uids])
        if simple is True:
            agent_args.append("--simple")
        objs = json.loads(self.call_agent(*agent_args, **kwargs))
        for obj in objs:
            result.append(Package(obj))
        return result

    def get_tcp_sockets(self, **kwargs) -> [InetSocket]:
        """
        同netstat命令，获取设备tcp连接情况，需要读取/proc/net/tcp文件，高版本设备至少需要shell权限
        :return: tcp连接列表
        """
        return self._get_sockets(InetSocket, "--tcp-sock", **kwargs)

    def get_udp_sockets(self, **kwargs) -> [InetSocket]:
        """
        同netstat命令，获取设备udp连接情况，需要读取/proc/net/udp文件，高版本设备至少需要shell权限
        :return: udp连接列表
        """
        return self._get_sockets(InetSocket, "--udp-sock", **kwargs)

    def get_raw_sockets(self, **kwargs) -> [InetSocket]:
        """
        同netstat命令，获取设备raw连接情况，需要读取/proc/net/raw文件，高版本设备至少需要shell权限
        :return: raw连接列表
        """
        return self._get_sockets(InetSocket, "--raw-sock", **kwargs)

    def get_unix_sockets(self, **kwargs) -> [UnixSocket]:
        """
        同netstat命令，获取设备unix连接情况，需要读取/proc/net/unix文件，高版本设备至少需要shell权限
        :return: unix连接列表
        """
        return self._get_sockets(UnixSocket, "--unix-sock", **kwargs)

    def _get_sockets(self, type, command, **kwargs):
        self._set_default(kwargs, capture_output=True, output_to_logger=False)

        result = []
        agent_args = ["network", command]
        objs = json.loads(self.call_agent(*agent_args, **kwargs))
        for obj in objs:
            result.append(type(obj))
        return result

    @classmethod
    def get_safe_path(cls, path: str) -> str:
        """
        过滤"../"关键字
        :param path: 原始路径
        :return: 过滤完"../"的路径
        """
        temp = path
        while True:
            result = temp.replace("../", "..")
            if temp == result:
                return result
            temp = result

    @classmethod
    def get_safe_command(cls, seq: [str]) -> str:
        """
        用双引号把命令包起来
        :param seq: 原命令
        :return: 双引号包起来的命令
        """
        return utils.list2cmdline(seq)

    @classmethod
    def get_storage_path(cls, *paths: [str]) -> str:
        """
        存储文件路径
        :param paths: 文件名
        :return: 路径
        """
        return "/sdcard/%s/%s" % (
            module_name,
            "/".join([cls.get_safe_path(o) for o in paths])
        )

    @classmethod
    def get_data_path(cls, *paths: [str]) -> str:
        """
        /data/local/tmp路径
        :param paths: 文件名
        :return: 路径
        """
        ""
        return "/data/local/tmp/%s" % (
            "/".join([cls.get_safe_path(o) for o in paths])
        )

    @classmethod
    def extract_package(cls, package_name) -> str:
        """
        获取可识别的包名（主要是过滤像":"这类字符）
        :param package_name: 包名
        :return: 包名
        """
        match = re.search(r"([a-zA-Z_]\w*)+([.][a-zA-Z_]\w*)+", package_name)
        if match is not None:
            return match.group(0)
        return package_name

    @classmethod
    def _set_default(cls, kwargs: dict, **_kwargs: Any):
        for key, value in _kwargs.items():
            if key in kwargs and kwargs[key] != value:
                _logger.warning(f"Invalid argument {key}={kwargs[key]}, ignored!", stack_info=True)
            kwargs[key] = value

    def redirect(self, address: str = None, port: int = 8080):
        """
        将手机流量重定向到本地指定端口
        :param address: 本地监听地址，不填默认本机
        :param port: 本地监听端口
        :return: 重定向对象
        """
        return _Redirect(self, address, port)

    def __repr__(self):
        return f"AdbDevice<{self.id}>"


class _Redirect:

    def __init__(self, device: "Device", address: str, port: int):
        self.device = device
        self.target_address = address
        self.target_port = port
        self.remote_port = None

    def start(self):
        if not self.target_address:
            # 如果没有指定目标地址，则通过reverse端口访问
            self.remote_port = self.device.exec("reverse", f"tcp:0", f"tcp:{self.target_port}").strip()
            destination = f"127.0.0.1:{self.remote_port}"
            _logger.debug(f"Not found redirect address, use {destination} instead")
        else:
            # 指定了目标地址那就直接用目标地址
            destination = f"{self.target_address}:{self.target_port}"
            _logger.debug(f"Found redirect address {destination}")
        # 排除localhost
        self.device.sudo(
            "iptables", "-t", "nat", "-A", "OUTPUT", "-p", "tcp", "-o", "lo", "-j", "RETURN"
        )
        # 转发流量
        self.device.sudo(
            "iptables", "-t", "nat", "-A", "OUTPUT", "-p", "tcp", "-j", "DNAT", "--to-destination", destination
        )

    def stop(self):
        # 清空iptables -t nat配置
        self.device.sudo("iptables", "-t", "nat", "-F", ignore_errors=True)
        # 如果占用reverse端口，则释放端口
        if self.remote_port:
            self.device.exec("reverse", "--remove", f"tcp:{self.remote_port}", ignore_errors=True)

    def __enter__(self):
        self.stop()
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
