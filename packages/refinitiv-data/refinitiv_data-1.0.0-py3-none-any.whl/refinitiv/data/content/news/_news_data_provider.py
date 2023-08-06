import abc
from typing import TYPE_CHECKING, Optional, List

from ._data_classes import (
    HeadlineRDP,
    Story,
    StoryUDF,
    HeadlineUDF,
)
from ._sort_order import SortOrder
from ._tools import get_headlines
from .._join_responses import join_responses
from ..._core.session import DesktopSession
from ..._tools import to_datetime, make_enum_arg_parser
from ...delivery._data._data_provider import (
    DataProvider,
    RequestFactory,
    ResponseFactory,
    Response,
    Data,
    ContentValidator,
    ValidatorContainer,
    EndpointData,
)
from ...delivery._data._endpoint_data import RequestMethod

if TYPE_CHECKING:
    from ...delivery._data._data_provider import ParsedData
    from ..._types import OptInt

MAX_LIMIT = 100


# --------------------------------------------------------------------------------------
#   Content data
# --------------------------------------------------------------------------------------


# NewsStory
class NewsStoryData(EndpointData):
    @abc.abstractmethod
    def _build_story(self, raw: dict) -> Story:
        # override this
        pass

    def __init__(self, raw, **kwargs) -> None:
        super().__init__(raw, **kwargs)
        self._story: Optional[Story] = None

    @property
    def story(self) -> Story:
        if self._story is None:
            self._story = self._build_story(self.raw)
        return self._story


class NewsStoryRDPData(NewsStoryData):
    @abc.abstractmethod
    def _build_story(self, raw: dict) -> Story:
        return Story.from_dict(raw)


class NewsStoryUDFData(NewsStoryData):
    @abc.abstractmethod
    def _build_story(self, raw: dict) -> StoryUDF:
        return StoryUDF.from_dict(raw)


# NewsHeadlines


class NewsHeadlinesData(Data):
    @abc.abstractmethod
    def _build_headlines(self, raw: dict, limit: int) -> List[HeadlineRDP]:
        # override this
        pass

    def __init__(self, raw, **kwargs) -> None:
        super().__init__(raw, **kwargs)
        self._headlines: Optional[List[HeadlineRDP]] = None
        self._limit: "OptInt" = None

    @property
    def headlines(self) -> List[HeadlineRDP]:
        if self._headlines is None:
            self._headlines = self._build_headlines(self.raw, self._limit)

        return self._headlines


class NewsHeadlinesRDPData(NewsHeadlinesData):
    @abc.abstractmethod
    def _build_headlines(self, raw: dict, limit: int) -> List[HeadlineRDP]:
        return get_headlines(raw, HeadlineRDP.from_dict, limit)


class NewsHeadlinesUDFData(NewsHeadlinesData):
    @abc.abstractmethod
    def _build_headlines(self, raw: dict, limit: int) -> List[HeadlineUDF]:
        return get_headlines(raw, HeadlineUDF.from_dict, limit)


# --------------------------------------------------------------------------------------
#   Response object
# --------------------------------------------------------------------------------------


class NewsStoryResponse(Response):
    def __init__(self, is_success: bool, data: "ParsedData") -> None:
        super().__init__(is_success, data)
        _raw = None
        if self.is_success:
            _raw = self.data
        self._data = NewsStoryData(_raw)

    def __str__(self):
        if self._data and self._data.raw:
            return (
                self._data.raw.get("newsItem", {})
                .get("contentSet", {})
                .get("inlineData", [{}])[0]
                .get("$")
                or self.data.story.content.text
            )
        else:
            return f"{self.errors}"


# --------------------------------------------------------------------------------------
#   Content data validator
# --------------------------------------------------------------------------------------


class NewsUDFContentValidator(ContentValidator):
    def __init__(self) -> None:
        super().__init__()
        self.validators.append(self.content_data_has_no_error)


# --------------------------------------------------------------------------------------
#   Response factory
# --------------------------------------------------------------------------------------


class NewsStoryResponseFactory(ResponseFactory):
    @staticmethod
    def change_code_and_message_in_data(data: "ParsedData") -> "ParsedData":
        new_error_msg = "Error while calling the NEP backend: Story not found"
        error_code = data.first_error_code
        error_msg = data.first_error_message

        if error_code == 400 or error_code == 404 and new_error_msg != error_msg:
            data.error_codes = 404
            data.error_messages = new_error_msg

        return data

    def create_fail(self, data: "ParsedData", **kwargs):
        self.change_code_and_message_in_data(data)
        return super().create_fail(data, **kwargs)


# --------------------------------------------------------------------------------------
#   Request factory
# --------------------------------------------------------------------------------------

# NewsStory


class NewsStoryUDFRequestFactory(RequestFactory):
    def get_body_parameters(self, session, *args, **kwargs):
        entity = {
            "E": "News_Story",
        }
        w = dict()

        story_id = kwargs.get("story_id")
        w["storyId"] = story_id

        app_key = session.app_key
        w["productName"] = app_key

        entity["W"] = w
        body_parameters = {"Entity": entity}
        return body_parameters

    def get_url(self, session, *args, **kwargs):
        url = session._get_rdp_url_root()
        if isinstance(session, DesktopSession):
            url = session._get_udf_url()
        return url

    def update_url(self, url_root, url, path_parameters, query_parameters):
        return url

    def get_request_method(self, **kwargs) -> RequestMethod:
        return RequestMethod.POST


class NewsStoryRDPRequestFactory(RequestFactory):
    def get_path_parameters(self, session=None, *, story_id=None, **kwargs):
        return {"storyId": story_id}

    def get_header_parameters(self, session=None, **kwargs):
        return {"accept": "application/json"}

    def get_url(self, *args, **kwargs):
        return super().get_url(*args, **kwargs) + "/{storyId}"


# NewsHeadlines
class NewsHeadlinesUDFRequestFactory(RequestFactory):
    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        if extended_params:
            body_parameters["Entity"]["W"].update(extended_params)
        return body_parameters

    def get_body_parameters(self, session, *args, **kwargs):
        entity = {
            "E": "News_Headlines",
        }
        w = dict()

        query = kwargs.get("query")
        w["query"] = query

        count = kwargs.get("count")
        if count is not None:
            w["number"] = str(count)

        payload = kwargs.get("payload")
        if payload is not None:
            w["payload"] = payload.replace("/headlines?payload=", "", 1)

        repository = kwargs.get("repository")
        if repository is not None:
            w["repository"] = repository

        app_key = session.app_key
        w["productName"] = app_key

        date_from = kwargs.get("date_from")
        if date_from is not None:
            w["dateFrom"] = to_datetime(date_from).isoformat()

        date_to = kwargs.get("date_to")
        if date_to is not None:
            w["dateTo"] = to_datetime(date_to).isoformat()

        entity["W"] = w
        body_parameters = {"Entity": entity}
        return body_parameters

    def get_url(self, session, *args, **kwargs):
        url = session._get_rdp_url_root()
        if isinstance(session, DesktopSession):
            url = session._get_udf_url()
        return url

    def update_url(self, url_root, url, path_parameters, query_parameters):
        return url

    def get_request_method(self, **kwargs) -> RequestMethod:
        return RequestMethod.POST


class NewsHeadlinesRDPRequestFactory(RequestFactory):
    def extend_query_parameters(self, query_parameters, extended_params=None):
        if extended_params:
            # query_parameters -> [("param1", "val1"), ]
            query_parameters = dict(query_parameters)
            # result -> {"param1": "val1"}
            query_parameters.update(extended_params)
            # result -> {"param1": "val1", "extended_param": "value"}
            # return [("param1", "val1"), ("extended_param", "value")]
            return list(query_parameters.items())
        return query_parameters

    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        return body_parameters

    def get_query_parameters(self, *_, **kwargs):
        query_parameters = []

        query = kwargs.get("query")
        query_parameters.append(("query", query))

        count = kwargs.get("count")
        if count is not None:
            query_parameters.append(("limit", count))

        date_from = kwargs.get("date_from")
        if date_from is not None:
            date_from = to_datetime(date_from).isoformat()
            query_parameters.append(("dateFrom", date_from))

        date_to = kwargs.get("date_to")
        if date_to is not None:
            date_to = to_datetime(date_to).isoformat()
            query_parameters.append(("dateTo", date_to))

        sort_order = kwargs.get("sort_order")
        if sort_order is not None:
            sort_order = sort_order_news_arg_parser.get_str(sort_order)
            query_parameters.append(("sort", sort_order))

        # for pagination
        cursor = kwargs.get("cursor")
        if cursor is not None:
            query_parameters.append(("cursor", cursor))

        return query_parameters


# --------------------------------------------------------------------------------------
#   Data provider
# --------------------------------------------------------------------------------------

# NewsStory


class NewsUDFDataProvider(DataProvider):
    @staticmethod
    def change_count(count: int, limit: int, kwargs: dict):
        number = abs(limit - count)
        if number < MAX_LIMIT:
            kwargs["count"] = number

    def get_data(self, *args, **kwargs):
        limit = kwargs.get("count")

        if limit is None:
            return super().get_data(*args, **kwargs)

        responses = []
        headlines = True
        count = 0

        if limit > MAX_LIMIT:
            kwargs["count"] = MAX_LIMIT

        while count < limit and headlines:
            response = super().get_data(*args, **kwargs)
            headlines = response.data.raw.get("headlines", [])
            count += len(headlines)
            kwargs["payload"] = response.data.raw.get("older")
            responses.append(response)
            self.change_count(count, limit, kwargs)

        response = join_responses(
            responses, data_class=self.response.data_class, limit=limit
        )
        response.data._limit = limit

        if not responses:
            response.is_success = True

        return response

    async def get_data_async(self, *args, **kwargs):
        limit = kwargs.get("count")

        if limit is None:
            return await super().get_data_async(*args, **kwargs)

        responses = []
        headlines = True
        count = 0

        if limit > MAX_LIMIT:
            kwargs["count"] = MAX_LIMIT

        while count < limit and headlines:
            response = await super().get_data_async(*args, **kwargs)
            headlines = response.data.raw.get("headlines", [])
            count += len(headlines)
            kwargs["payload"] = response.data.raw.get("older")
            responses.append(response)
            self.change_count(count, limit, kwargs)

        response = join_responses(
            responses, data_class=self.response.data_class, limit=limit
        )
        response.data._limit = limit

        if not responses:
            response.is_success = True

        return response


# NewsHeadlines


class NewsHeadlinesRDPDataProvider(DataProvider):
    def get_data(self, *args, **kwargs):
        on_page_response = kwargs.get("on_page_response")
        limit = kwargs.get("count")
        responses = []
        cursor = True
        count = 0

        if limit > MAX_LIMIT:
            kwargs["count"] = MAX_LIMIT

        while count < limit and cursor:
            response = super().get_data(*args, **kwargs)
            responses.append(response)

            if on_page_response:
                on_page_response(self, response)

            meta = response.data.raw.get("meta", {})
            count += meta.get("count", 0)
            cursor = meta.get("next")
            kwargs = {
                "cursor": cursor,
                "__content_type__": kwargs.get("__content_type__"),
            }

        response = join_responses(
            responses, data_class=NewsHeadlinesRDPData, limit=limit
        )
        response.data._limit = limit

        if not responses:
            response.is_success = True

        return response

    async def get_data_async(self, *args, **kwargs):
        on_page_response = kwargs.get("on_page_response")
        limit = kwargs.get("count")
        responses = []
        cursor = True
        count = 0

        if limit > MAX_LIMIT:
            kwargs["count"] = MAX_LIMIT

        while count < limit and cursor:
            response = await super().get_data_async(*args, **kwargs)
            responses.append(response)

            if on_page_response:
                on_page_response(self, response)

            meta = response.data.raw.get("meta", {})
            count += meta.get("count", 0)
            cursor = meta.get("next")
            kwargs = {
                "cursor": cursor,
                "__content_type__": kwargs.get("__content_type__"),
            }

        response = join_responses(
            responses, data_class=NewsHeadlinesRDPData, limit=limit
        )
        response.data._limit = limit

        if not responses:
            response.is_success = True

        return response


sort_order_news_arg_parser = make_enum_arg_parser(SortOrder)

validator = ValidatorContainer(content_validator=NewsUDFContentValidator())

# NewsStory

news_story_data_provider_rdp = DataProvider(
    response=NewsStoryResponseFactory(
        response_class=NewsStoryResponse,
        data_class=NewsStoryRDPData,
    ),
    request=NewsStoryRDPRequestFactory(),
)

news_story_data_provider_udf = NewsUDFDataProvider(
    response=NewsStoryResponseFactory(
        response_class=NewsStoryResponse,
        data_class=NewsStoryUDFData,
    ),
    request=NewsStoryUDFRequestFactory(),
    validator=validator,
)

# NewsHeadlines

news_headlines_data_provider_rdp = NewsHeadlinesRDPDataProvider(
    response=ResponseFactory(data_class=NewsHeadlinesRDPData),
    request=NewsHeadlinesRDPRequestFactory(),
)
news_headlines_data_provider_udf = NewsUDFDataProvider(
    response=ResponseFactory(data_class=NewsHeadlinesUDFData),
    request=NewsHeadlinesUDFRequestFactory(),
    validator=validator,
)
