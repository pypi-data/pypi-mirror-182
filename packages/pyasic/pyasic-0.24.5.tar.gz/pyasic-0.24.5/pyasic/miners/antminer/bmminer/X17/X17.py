#  Copyright 2022 Upstream Data Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Union

import httpx

from pyasic.miners._backends import BMMiner  # noqa - Ignore access to _module
from pyasic.settings import PyasicSettings


class BMMinerX17(BMMiner):
    def __init__(self, ip: str, api_ver: str = "1.0.0") -> None:
        super().__init__(ip, api_ver=api_ver)
        self.ip = ip
        self.uname = "root"
        self.pwd = PyasicSettings().global_x17_password

    async def get_hostname(self) -> Union[str, None]:
        hostname = None
        url = f"http://{self.ip}/cgi-bin/get_system_info.cgi"
        auth = httpx.DigestAuth(self.uname, self.pwd)
        async with httpx.AsyncClient() as client:
            data = await client.get(url, auth=auth)
        if data.status_code == 200:
            data = data.json()
            if len(data.keys()) > 0:
                if "hostname" in data.keys():
                    hostname = data["hostname"]
        return hostname

    async def get_mac(self) -> Union[str, None]:
        mac = None
        url = f"http://{self.ip}/cgi-bin/get_system_info.cgi"
        auth = httpx.DigestAuth(self.uname, self.pwd)
        async with httpx.AsyncClient() as client:
            data = await client.get(url, auth=auth)
        if data.status_code == 200:
            data = data.json()
            if len(data.keys()) > 0:
                if "macaddr" in data.keys():
                    mac = data["macaddr"]
        return mac

    async def fault_light_on(self) -> bool:
        url = f"http://{self.ip}/cgi-bin/blink.cgi"
        auth = httpx.DigestAuth(self.uname, self.pwd)
        async with httpx.AsyncClient() as client:
            try:
                await client.post(url, data={"action": "startBlink"}, auth=auth)
            except httpx.ReadTimeout:
                # Expected behaviour
                pass
            data = await client.post(url, data={"action": "onPageLoaded"}, auth=auth)
        if data.status_code == 200:
            data = data.json()
            if data["isBlinking"]:
                self.light = True
                return True
        return False

    async def fault_light_off(self) -> bool:
        url = f"http://{self.ip}/cgi-bin/blink.cgi"
        auth = httpx.DigestAuth(self.uname, self.pwd)
        async with httpx.AsyncClient() as client:
            await client.post(url, data={"action": "stopBlink"}, auth=auth)
            data = await client.post(url, data={"action": "onPageLoaded"}, auth=auth)
        if data.status_code == 200:
            data = data.json()
            if not data["isBlinking"]:
                self.light = False
                return True
        return False

    async def check_light(self) -> Union[bool, None]:
        if self.light:
            return self.light
        url = f"http://{self.ip}/cgi-bin/blink.cgi"
        auth = httpx.DigestAuth(self.uname, self.pwd)
        async with httpx.AsyncClient() as client:
            data = await client.post(url, data={"action": "onPageLoaded"}, auth=auth)
        if data.status_code == 200:
            data = data.json()
            if data["isBlinking"]:
                self.light = True
                return True
            else:
                self.light = False
                return False
        return None

    async def reboot(self) -> bool:
        url = f"http://{self.ip}/cgi-bin/reboot.cgi"
        auth = httpx.DigestAuth(self.uname, self.pwd)
        async with httpx.AsyncClient() as client:
            data = await client.get(url, auth=auth)
        if data.status_code == 200:
            return True
        return False
