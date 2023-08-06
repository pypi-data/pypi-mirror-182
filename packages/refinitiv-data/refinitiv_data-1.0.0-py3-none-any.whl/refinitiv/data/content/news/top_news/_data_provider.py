from typing import List

from ._top_news_headline import TopNewsHeadline
from ...._tools import cached_property, ParamItem
from ....delivery._data._content_data import Data
from ....delivery._data._data_provider import DataProvider
from ....delivery._data._request_factory import RequestFactory
from ....delivery._data._response_factory import ResponseFactory


class TopNewsData(Data):
    @cached_property
    def headlines(self) -> "List[TopNewsHeadline]":
        return [
            TopNewsHeadline.from_dict(headline_data)
            for headline_data in self.raw.get("data", [])
        ]


query_params = [ParamItem("revision_id", "revisionId")]


class TopNewsRequestFactory(RequestFactory):
    def get_path_parameters(self, session=None, *, top_news_id=None, **kwargs):
        return {"topNewsId": top_news_id}

    def get_url(self, *args, **kwargs):
        return f"{super().get_url(*args, **kwargs)}/{{topNewsId}}"

    @property
    def query_params_config(self):
        return query_params


news_top_news_data_provider = DataProvider(
    request=TopNewsRequestFactory(),
    response=ResponseFactory(data_class=TopNewsData),
)
