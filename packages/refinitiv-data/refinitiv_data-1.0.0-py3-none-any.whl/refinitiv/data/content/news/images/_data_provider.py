from ._image import Image
from ...._tools import ParamItem
from ....delivery._data._data_provider import (
    DataProvider,
    RequestFactory,
)
from ....delivery._data._endpoint_data import EndpointData
from ....delivery._data._response_factory import ResponseFactory


class ImageData(EndpointData):
    @property
    def image(self) -> "Image":
        return Image(self.raw)


query_params = [
    ParamItem("width"),
    ParamItem("height"),
]


class ImagesRequestFactory(RequestFactory):
    @property
    def query_params_config(self):
        return query_params

    def get_path_parameters(self, session=None, *, image_id=None, **kwargs):
        return {"imageId": image_id}

    def get_url(self, *args, **kwargs):
        return f"{super().get_url(*args, **kwargs)}/{{imageId}}"


news_images_data_provider = DataProvider(
    request=ImagesRequestFactory(), response=ResponseFactory(data_class=ImageData)
)
