from typing import List, TYPE_CHECKING

from .._content_data_validator import ContentDataValidator
from ..holidays._holidays_data_provider import Holiday
from ...._df_builder import build_dates_calendars_df
from .....content.ipa._content_provider import DatesAndCalendarsRequestFactory
from .....delivery._data._data_provider import (
    ResponseFactory,
    DataProvider,
    ValidatorContainer,
    Data,
)

if TYPE_CHECKING:
    from .....delivery._data._data_provider import ParsedData


class WorkingDay:
    def __init__(
        self,
        is_weekend: bool,
        is_working_day: bool,
        tag: str = "",
        holidays: list = None,
    ):
        self._is_weekend = is_weekend
        self._response_holidays_items = holidays or []
        self._is_working_day = is_working_day
        self._tag = tag
        self._holidays = []
        self._holidays_data = []

    @property
    def is_weekend(self):
        return self._is_weekend

    @property
    def is_working_day(self):
        return self._is_working_day

    @property
    def tag(self):
        return self._tag

    @property
    def holidays(self) -> List[Holiday]:
        if self._holidays:
            return self._holidays

        for holiday in self._response_holidays_items:
            holiday_ = Holiday(holiday=holiday, tag=self.tag)
            self._holidays.append(holiday_)
        return self._holidays


class IsWorkingDay(Data):
    def __init__(self, raw: dict, tag: str = ""):
        super().__init__(raw, dfbuilder=build_dates_calendars_df)
        self._day = WorkingDay(
            is_weekend=raw[0]["isWeekEnd"],
            is_working_day=raw[0]["isWorkingDay"],
            tag=tag,
            holidays=raw[0].get("holidays", []),
        )

    @property
    def day(self):
        return self._day


class IsWorkingDays(Data):
    def __init__(self, raw: dict):
        super().__init__(raw, dfbuilder=build_dates_calendars_df)
        self._raw = raw
        self._is_working_days = []

        filtered_working_days_response = []
        for raw_item in self.raw:
            if not raw_item.get("error"):
                filtered_working_days_response.append(raw_item)

        for item in filtered_working_days_response:
            _is_working_days = WorkingDay(
                item["isWeekEnd"],
                item.get("isWorkingDay"),
                tag=item.get("tag"),
                holidays=item.get("holidays"),
            )
            self._is_working_days.append(_is_working_days)

    @property
    def days(self):
        return self._is_working_days

    def __getitem__(self, item: int):
        return self._is_working_days[item]


class IsWorkingDayResponseFactory(ResponseFactory):
    def create_success(
        self, data: "ParsedData", session: "Session" = None, **kwargs: dict
    ):
        response = self.response_class(True, data)

        if len(response.data) > 1:
            is_working_day = IsWorkingDays(data.content_data)
            response.data = is_working_day

        else:
            raw_response_item = response.data[0]
            response.data = IsWorkingDay(
                data.content_data, raw_response_item.get("tag")
            )

        return response

    def create_fail(self, data: "ParsedData", **kwargs: dict):
        if data.status.get("error", {}).get("errors"):
            message = data.status["error"]["errors"][0]["reason"]
            data.error_messages = f"{data.first_error_message}. {message}"

        return super().create_fail(data, **kwargs)


is_working_day_data_provider = DataProvider(
    request=DatesAndCalendarsRequestFactory(),
    response=IsWorkingDayResponseFactory(),
    validator=ValidatorContainer(content_validator=ContentDataValidator()),
)
