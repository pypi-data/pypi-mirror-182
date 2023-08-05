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

from pyasic.miners._backends import BTMiner  # noqa - Ignore access to _module
from pyasic.miners._types import (  # noqa - Ignore access to _module
    M30SPlus,
    M30SPlusVE40,
    M30SPlusVF20,
    M30SPlusVG60,
    M30SPlusVG40,
)


class BTMinerM30SPlus(BTMiner, M30SPlus):
    def __init__(self, ip: str, api_ver: str = "1.0.0") -> None:
        super().__init__(ip, api_ver=api_ver)
        self.ip = ip


class BTMinerM30SPlusVF20(BTMiner, M30SPlusVF20):
    def __init__(self, ip: str, api_ver: str = "1.0.0") -> None:
        super().__init__(ip, api_ver=api_ver)
        self.ip = ip


class BTMinerM30SPlusVE40(BTMiner, M30SPlusVE40):
    def __init__(self, ip: str, api_ver: str = "1.0.0") -> None:
        super().__init__(ip, api_ver=api_ver)
        self.ip = ip


class BTMinerM30SPlusVG40(BTMiner, M30SPlusVG40):
    def __init__(self, ip: str, api_ver: str = "1.0.0") -> None:
        super().__init__(ip, api_ver=api_ver)
        self.ip = ip


class BTMinerM30SPlusVG60(BTMiner, M30SPlusVG60):
    def __init__(self, ip: str, api_ver: str = "1.0.0") -> None:
        super().__init__(ip, api_ver=api_ver)
        self.ip = ip
