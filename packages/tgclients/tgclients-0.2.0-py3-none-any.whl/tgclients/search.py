# SPDX-FileCopyrightText: 2022 Georg-August-Universität Göttingen
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""TextGrid Search API."""
import logging
from io import BytesIO
from typing import Optional

import requests
from requests.models import Response
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from tgclients.config import TextgridConfig
from tgclients.databinding.tgsearch import Response as SearchResponse

logger = logging.getLogger(__name__)

# https://realpython.com/factory-method-python/ -> databinding on demand


class TextgridSearchRequest:
    """Provide low level access to the Textgrid Search Service, returning the response objects."""

    def __init__(self, url: str = TextgridConfig().search_public, config:
                 TextgridConfig = TextgridConfig()) -> None:
        self._url = url
        self._config = config

    def info(self, textgrid_uri: str, sid: Optional[str] = '') -> Response:
        """Retrieve metadata for a textgrid object specified by its
        textgrid-uri

        Args:
            textgrid_uri (str): Textgrid URI
            sid (Optional[str]): Session ID. Defaults to ''.

        Raises:
            TextgridSearchException: if HTTP-Status less than 400   (# noqa: DAR402)

        Returns:
            Response: metadata for uri
        """
        url = self._url + '/info/'
        response = requests.get(
            url + textgrid_uri + '?sid=' + sid, timeout=self._config.http_timeout)
        return self._handle_response(response)

    def list_project_root(self, project_id: str, sid: Optional[str] = '') -> Response:
        """Get objects belonging to a project, filtered by objects that are in
        an aggregation in the same project.

        Args:
            project_id (str): the ID of the project to list
            sid (Optional[str], optional): Session ID. Defaults to ''.

        Raises:
            TextgridSearchException: if HTTP-Status less than 400   (# noqa: DAR402)

        Returns:
            Response: HTTP response from service, containing a list of textgrid metadata entries
        """
        response = requests.get(
            self._url + '/navigation/' + project_id + '?sid=' + sid,
            timeout=self._config.http_timeout)
        return self._handle_response(response)

    def list_aggregation(self, textgrid_uri: str, sid: Optional[str] = '') -> Response:
        """Get child resources of an aggregation.

        Args:
            textgrid_uri (str): Textgrid URI
            sid (Optional[str], optional): Session ID. Defaults to ''.

        Raises:
            TextgridSearchException: if HTTP-Status less than 400   (# noqa: DAR402)

        Returns:
            Response: HTTP response from service, containing a list of textgrid metadata entries
        """
        response = requests.get(self._url + '/navigation/agg/' +
                                textgrid_uri + '?sid=' + sid,
                                timeout=self._config.http_timeout)
        return self._handle_response(response)

    @staticmethod
    def _handle_response(response: Response) -> Response:
        """Error handling for responses from tgsearch

        Args:
            response (Response): a response from tgsearch

        Raises:
            TextgridSearchException: if HTTP-Status less than 400

        Returns:
            Response: the response
        """
        if not response.ok:
            message = '[Error] HTTP Code: ' + \
                str(response.status_code) + ' - ' + response.text[0:255]
            logger.warning(message)
            raise TextgridSearchException(message)
        return response


class TextgridSearch(TextgridSearchRequest):
    """Provide access to the Textgrid Search Service using a XML data binding """

    def __init__(self, url: str = TextgridConfig().search_public) -> None:
        super().__init__(url)
        # It’s recommended to either reuse the same parser/serializer instance
        # or reuse the context instance. see https://xsdata.readthedocs.io/en/latest/xml.html
        context = XmlContext()
        self._parser = XmlParser(context=context)

    def info(self, textgrid_uri: str, sid: Optional[str] = '') -> SearchResponse:
        """Retrieve metadata for a textgrid object specified by its
        textgrid-uri

        Args:
            textgrid_uri (str): Textgrid URI
            sid (Optional[str]): Session ID. Defaults to ''.

        Raises:
            TextgridSearchException: if HTTP-Status less than 400   (# noqa: DAR402)

        Returns:
            SearchResponse: metadata for uri
        """
        response = super().info(textgrid_uri, sid)
        return self._parser.parse(BytesIO(response.content), SearchResponse)

    def list_project_root(self, project_id: str, sid: Optional[str] = '') -> SearchResponse:
        """Get objects belonging to a project, filtered by objects that are in
        an aggregation in the same project.

        Args:
            project_id (str): the ID of the project to list
            sid (Optional[str], optional): Session ID. Defaults to ''.

        Raises:
            TextgridSearchException: if HTTP-Status less than 400   (# noqa: DAR402)

        Returns:
            SearchResponse: A list of textgrid metadata entries
        """
        response = super().list_project_root(project_id, sid)
        return self._parser.parse(BytesIO(response.content), SearchResponse)

    def list_aggregation(self, textgrid_uri: str, sid: Optional[str] = '') -> SearchResponse:
        """Get child resources of an aggregation.

        Args:
            textgrid_uri (str): Textgrid URI
            sid (Optional[str], optional): Session ID. Defaults to ''.

        Raises:
            TextgridSearchException: if HTTP-Status less than 400   (# noqa: DAR402)

        Returns:
            SearchResponse: A list of textgrid metadata entries
        """
        response = super().list_aggregation(textgrid_uri, sid)
        return self._parser.parse(BytesIO(response.content), SearchResponse)


class TextgridSearchException(Exception):
    """Exception communicating with tgsearch"""
