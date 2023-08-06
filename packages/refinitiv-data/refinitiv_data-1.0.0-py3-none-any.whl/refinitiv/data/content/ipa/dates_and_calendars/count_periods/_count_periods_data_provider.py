from typing import TYPE_CHECKING

from .._content_data_validator import ContentDataValidator
from ...._df_builder import default_build_df
from .....content.ipa._content_provider import DatesAndCalendarsRequestFactory
from .....delivery._data._data_provider import (
    ResponseFactory,
    DataProvider,
    ValidatorContainer,
    Data,
)

if TYPE_CHECKING:
    from .....delivery._data._data_provider import (
        ParsedData,
    )


class Period:
    def __init__(self, count: float, tenor: str, tag: str = ""):
        self._count = count
        self._tenor = tenor
        self._tag = tag

    @property
    def count(self):
        return self._count

    @property
    def tenor(self):
        return self._tenor

    @property
    def tag(self):
        return self._tag


class CountedPeriods(Data):
    def __init__(self, raw: dict):
        super().__init__(raw, dfbuilder=default_build_df)
        self._raw = raw
        self._counted_periods = []
        for item in self._raw:
            _counted_periods = Period(item["count"], item["tenor"], tag=item.get("tag"))
            self._counted_periods.append(_counted_periods)

    @property
    def counted_periods(self):
        return self._counted_periods

    def __getitem__(self, item: int):
        return self._counted_periods[item]


class CountedPeriod(Data):
    def __init__(self, raw: dict, count: float, tenor: str, tag: str = ""):
        super().__init__(raw, dfbuilder=default_build_df)
        self._period = Period(count, tenor, tag)

    @property
    def counted_period(self):
        return self._period


class CountPeriodsResponseFactory(ResponseFactory):
    def create_success(
        self, data: "ParsedData", session: "Session" = None, **kwargs: dict
    ):
        response = self.response_class(True, data)

        for item in data.content_data:
            if item.get("error"):
                return self.create_fail(item, **kwargs)

        if len(response.data) > 1:
            counted_periods = CountedPeriods(data.content_data)
            response.data = counted_periods
        else:
            raw_response_item = response.data[0]
            response.data = CountedPeriod(
                data.content_data,
                raw_response_item["count"],
                raw_response_item["tenor"],
                raw_response_item.get("tag"),
            )

        return response

    def create_fail(self, data: "ParsedData", **kwargs: dict):
        if data.status.get("error", {}).get("errors"):
            message = data.status["error"]["errors"][0]["reason"]
            data.error_messages = f"{data.first_error_message}. {message}"

        return super().create_fail(data, **kwargs)


count_periods_data_provider = DataProvider(
    request=DatesAndCalendarsRequestFactory(),
    response=CountPeriodsResponseFactory(),
    validator=ValidatorContainer(content_validator=ContentDataValidator()),
)
