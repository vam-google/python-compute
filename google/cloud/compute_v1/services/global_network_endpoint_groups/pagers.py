# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.compute_v1.types import compute


class ListPager:
    """A pager for iterating through ``list`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.NetworkEndpointGroupList` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``List`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.NetworkEndpointGroupList`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.NetworkEndpointGroupList],
        request: compute.ListGlobalNetworkEndpointGroupsRequest,
        response: compute.NetworkEndpointGroupList,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListGlobalNetworkEndpointGroupsRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.NetworkEndpointGroupList):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListGlobalNetworkEndpointGroupsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[compute.NetworkEndpointGroupList]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[compute.NetworkEndpointGroup]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNetworkEndpointsPager:
    """A pager for iterating through ``list_network_endpoints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.NetworkEndpointGroupsListNetworkEndpoints` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNetworkEndpoints`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.NetworkEndpointGroupsListNetworkEndpoints`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.NetworkEndpointGroupsListNetworkEndpoints],
        request: compute.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest,
        response: compute.NetworkEndpointGroupsListNetworkEndpoints,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.NetworkEndpointGroupsListNetworkEndpoints):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[compute.NetworkEndpointGroupsListNetworkEndpoints]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[compute.NetworkEndpointWithHealthStatus]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
