from typing import Iterable, List, Optional, Union

from benchling_api_client.v2.stable.api.users import get_user, list_users
from benchling_api_client.v2.types import Response

from benchling_sdk.errors import raise_for_status
from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.logging_helpers import log_not_implemented
from benchling_sdk.helpers.pagination_helpers import NextToken, PageIterator
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.helpers.serialization_helpers import none_as_unset, optional_array_query_param
from benchling_sdk.models import ListUsersSort, User, UsersPaginatedList
from benchling_sdk.services.v2.base_service import BaseService


class UserService(BaseService):
    """
    Users.

    Benchling users.

    See https://benchling.com/api/reference#/Users
    """

    @api_method
    def get_by_id(self, user_id: str) -> User:
        """
        Get a user by ID.

        See https://benchling.com/api/reference#/Users/getUser
        """
        response = get_user.sync_detailed(client=self.client, user_id=user_id)
        return model_from_detailed(response)

    @api_method
    def _users_page(
        self,
        *,
        ids: Optional[Iterable[str]] = None,
        name: Optional[str] = None,
        name_includes: Optional[str] = None,
        names_any_of: Optional[Iterable[str]] = None,
        names_any_of_case_sensitive: Optional[Iterable[str]] = None,
        modified_at: Optional[str] = None,
        member_of: Optional[Iterable[str]] = None,
        admin_of: Optional[Iterable[str]] = None,
        handles: Optional[Iterable[str]] = None,
        sort: Optional[ListUsersSort] = None,
        page_size: Optional[int] = 50,
        next_token: Optional[str] = None,
    ) -> Response[UsersPaginatedList]:
        response = list_users.sync_detailed(
            client=self.client,
            ids=none_as_unset(optional_array_query_param(ids)),
            name=none_as_unset(name),
            name_includes=none_as_unset(name_includes),
            namesany_of=none_as_unset(optional_array_query_param(names_any_of)),
            namesany_ofcase_sensitive=none_as_unset(optional_array_query_param(names_any_of_case_sensitive)),
            modified_at=none_as_unset(modified_at),
            member_of=none_as_unset(optional_array_query_param(member_of)),
            admin_of=none_as_unset(optional_array_query_param(admin_of)),
            handles=none_as_unset(optional_array_query_param(handles)),
            page_size=none_as_unset(page_size),
            next_token=none_as_unset(next_token),
            sort=none_as_unset(sort),
        )
        raise_for_status(response)
        return response  # type: ignore

    def list(
        self,
        *,
        ids: Optional[Iterable[str]] = None,
        name: Optional[str] = None,
        name_includes: Optional[str] = None,
        names_any_of: Optional[Iterable[str]] = None,
        names_any_of_case_sensitive: Optional[Iterable[str]] = None,
        modified_at: Optional[str] = None,
        member_of: Optional[Iterable[str]] = None,
        admin_of: Optional[Iterable[str]] = None,
        handles: Optional[Iterable[str]] = None,
        sort: Optional[Union[ListUsersSort]] = None,
        page_size: Optional[int] = 50,
        mentioned_in: Optional[List[str]] = None,
    ) -> PageIterator[User]:
        """
        List users.

        See https://benchling.com/api/reference#/Users/listUsers
        """
        if sort:
            sort = ListUsersSort(sort)

        if mentioned_in:
            log_not_implemented("mentioned_in")

        def api_call(next_token: NextToken) -> Response[UsersPaginatedList]:
            return self._users_page(
                ids=ids,
                name=name,
                name_includes=name_includes,
                names_any_of=names_any_of,
                names_any_of_case_sensitive=names_any_of_case_sensitive,
                modified_at=modified_at,
                member_of=member_of,
                admin_of=admin_of,
                handles=handles,
                sort=sort,
                next_token=next_token,
                page_size=page_size,
            )

        def results_extractor(body: UsersPaginatedList) -> Optional[List[User]]:
            return body.users

        return PageIterator(api_call, results_extractor)
