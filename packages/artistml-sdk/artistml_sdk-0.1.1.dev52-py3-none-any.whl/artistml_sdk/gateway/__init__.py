'''
Author: ksice ksice.xt@gmail.com
Date: 2022-12-12 10:35:30
LastEditors: ksice ksice.xt@gmail.com
LastEditTime: 2022-12-12 11:26:48
FilePath: /artistml/artistml-sdk/artistml_sdk/gateway/__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Final

from ._core import Error
from ._core import GrpcClient
from ._core import RPCResponseError
from ._core import try_request_grpc
from ._grpc_clients.echo import EchoClient
from ._grpc_clients.muses import MusesClient
from ._grpc_clients.tag import TagClient

echo_client: Final[EchoClient] = EchoClient()
muses_client: Final[MusesClient] = MusesClient()
tag_client: Final[TagClient] = TagClient()
__all__ = [
    "GrpcClient",
    "Error",
    "RPCResponseError",
    "try_request_grpc",
    "echo_client",
    "muses_client",
    "tag_client",
]
