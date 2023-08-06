from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mipac.abc.manager import AbstractManager
from mipac.http import HTTPClient, Route
from mipac.models.user import FollowRequest, UserDetailed
from mipac.types.user import IFollowRequest

if TYPE_CHECKING:
    from mipac.client import ClientActions

__all__ = ('FollowManager', 'FollowRequestManager')


class FollowManager(AbstractManager):
    def __init__(
        self,
        user_id: Optional[str] = None,
        *,
        session: HTTPClient,
        client: ClientActions
    ):
        self.__user_id: Optional[str] = user_id
        self.__session: HTTPClient = session
        self.__client: ClientActions = client

    async def add(
        self, user_id: Optional[str] = None
    ) -> tuple[bool, Optional[str]]:
        """
        ユーザーをフォローします

        Returns
        -------
        bool
            成功ならTrue, 失敗ならFalse
        str
            実行に失敗した際のエラーコード
        """

        user_id = user_id or self.__user_id

        data = {'userId': user_id}
        res = await self.__session.request(
            Route('POST', '/api/following/create'),
            json=data,
            auth=True,
            lower=True,
        )
        if res.get('error'):
            code = res['error']['code']
            status = False
        else:
            code = None
            status = True
        return status, code

    async def remove(self, user_id: Optional[str] = None) -> bool:
        """
        ユーザーのフォローを解除します

        Returns
        -------
        bool
            成功ならTrue, 失敗ならFalse
        """

        user_id = user_id or self.__user_id

        data = {'userId': user_id}
        res = await self.__session.request(
            Route('POST', '/api/following/delete'), json=data, auth=True
        )
        return bool(res.status_code == 204 or 200)


class FollowRequestManager(AbstractManager):
    def __init__(
        self,
        user_id: Optional[str] = None,
        *,
        session: HTTPClient,
        client: ClientActions
    ):
        self.__user_id: Optional[str] = user_id
        self.__session: HTTPClient = session
        self.__client: ClientActions = client

    async def get_all(self) -> list[FollowRequest]:
        """
        未承認のフォローリクエストを取得します
        """

        res: list[IFollowRequest] = await self.__session.request(
            Route('POST', '/api/following/requests/list'),
            auth=True,
            lower=True,
        )
        return [FollowRequest(request=i, client=self.__client) for i in res]

    async def get_user(self, user_id: Optional[str] = None) -> UserDetailed:
        """
        フォローリクエスト元のユーザーを取得します
        Parameters
        ----------
        user_id : Optional[str], default=None
            ユーザーID

        Returns
        -------
        UserDetailed
            フォローリクエスト元のユーザー
        """

        user_id = user_id or self.__user_id

        return await self.__client.user.action.get(user_id)

    async def accept(self, user_id: Optional[str] = None) -> bool:
        """
        与えられたIDのユーザーのフォローリクエストを承認します
        """

        user_id = user_id or self.__user_id

        data = {'userId': user_id}
        return bool(
            await self.__session.request(
                Route('POST', '/api/following/requests/accept'),
                json=data,
                auth=True,
            )
        )

    async def reject(self, user_id: Optional[str]) -> bool:
        """
        与えられたIDのユーザーのフォローリクエストを拒否します
        """

        user_id = user_id or self.__user_id

        data = {'userId': user_id}
        return bool(
            await self.__session.request(
                Route('POST', '/api/following/requests/reject'),
                json=data,
                auth=True,
            )
        )
