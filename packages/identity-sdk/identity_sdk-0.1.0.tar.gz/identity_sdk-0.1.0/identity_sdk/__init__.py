from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

from starlite import (AbstractAuthenticationMiddleware, ASGIConnection,
                      AuthenticationResult, DefineMiddleware,
                      NotAuthorizedException, Request)


class Group(Enum):
    """
    The possible groups a user could have
    """

    Participant = "participant"
    Sponsor = "sponsor"
    MLH = "mlh"
    Organizer = "organizer"
    Director = "director"


@dataclass(frozen=True)
class CurrentUser:
    """
    The user information for the request
    """

    id: int
    first_name: str
    last_name: str
    email: str
    group: Group
    context: str

    @property
    def is_admin(self):
        return self.context == "admin"

    @property
    def is_registering(self):
        return self.context == "manage"


class AuthenticationMiddleware(AbstractAuthenticationMiddleware):
    async def authenticate_request(
        self, connection: ASGIConnection
    ) -> AuthenticationResult:
        def value_or_fail(header: str) -> str:
            value = connection.headers.get(header)
            if value is None:
                raise NotAuthorizedException()

            return value

        try:
            user = CurrentUser(
                id=int(value_or_fail("X-Identity-ID")),
                first_name=value_or_fail("X-Identity-First-Name"),
                last_name=value_or_fail("X-Identity-Last-Name"),
                email=value_or_fail("X-Identity-Email"),
                group=Group(value_or_fail("X-Identity-Group")),
                context=value_or_fail("X-Identity-Context"),
            )
        except ValueError:
            raise NotAuthorizedException()

        return AuthenticationResult(user=user, auth=None)


AuthenticatedRequest: TypeAlias = Request[CurrentUser, None]

middleware = DefineMiddleware(AuthenticationMiddleware)
