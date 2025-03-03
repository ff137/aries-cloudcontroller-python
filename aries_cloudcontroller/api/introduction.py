from uplink import (
    Consumer,
    Path,
    Query,
    Body,
    Header,
    get,
    post,
    patch,
    put,
    delete,
    returns,
    json,
)

from typing import Any, Dict, List, Optional, Union  # noqa: F401

from aries_cloudcontroller.uplink_util import bool_query


class IntroductionApi(Consumer):
    async def start_introduction(
        self, *, conn_id: str, target_connection_id: str, message: Optional[str] = None
    ) -> Dict[str, Any]:
        """Start an introduction between two connections"""
        return await self.__start_introduction(
            conn_id=conn_id,
            target_connection_id=target_connection_id,
            message=message,
        )

    @returns.json
    @post("/connections/{conn_id}/start-introduction")
    def __start_introduction(
        self, *, conn_id: str, target_connection_id: Query, message: Query = None
    ) -> Dict[str, Any]:
        """Internal uplink method for start_introduction"""
