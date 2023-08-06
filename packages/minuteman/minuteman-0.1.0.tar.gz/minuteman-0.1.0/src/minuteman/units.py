from enum import Enum
from typing import Final

from pydantic import BaseModel


class UnitOfTime(str, Enum):
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"
    DECADES = "decades"

    @staticmethod
    def from_str(request: str) -> "UnitOfTime":
        if request[-1] != "s":
            request = f"{request}s"

        return UnitOfTime(request)


TIME_EXPRESSION_MULTIPLIERS: Final[dict[tuple[UnitOfTime, UnitOfTime], float]] = {
    (UnitOfTime.SECONDS, UnitOfTime.SECONDS): 1,
    (UnitOfTime.SECONDS, UnitOfTime.MINUTES): 1 / 60,
    (UnitOfTime.SECONDS, UnitOfTime.HOURS): 1 / 60 / 60,
    (UnitOfTime.SECONDS, UnitOfTime.DAYS): 1 / 60 / 60 / 24,
    (UnitOfTime.SECONDS, UnitOfTime.WEEKS): 1 / 60 / 60 / 24 / 7,
    (UnitOfTime.SECONDS, UnitOfTime.MONTHS): 1 / 60 / 60 / 24 / 30,
    (UnitOfTime.SECONDS, UnitOfTime.YEARS): 1 / 60 / 60 / 24 / 365,
    (UnitOfTime.SECONDS, UnitOfTime.DECADES): 1 / 60 / 60 / 24 / 365 / 10,
    (UnitOfTime.MINUTES, UnitOfTime.SECONDS): 60,
    (UnitOfTime.MINUTES, UnitOfTime.MINUTES): 1,
    (UnitOfTime.MINUTES, UnitOfTime.HOURS): 1 / 60,
    (UnitOfTime.MINUTES, UnitOfTime.DAYS): 1 / 60 / 24,
    (UnitOfTime.MINUTES, UnitOfTime.WEEKS): 1 / 60 / 24 / 7,
    (UnitOfTime.MINUTES, UnitOfTime.MONTHS): 1 / 60 / 24 / 30,
    (UnitOfTime.MINUTES, UnitOfTime.YEARS): 1 / 60 / 24 / 365,
    (UnitOfTime.MINUTES, UnitOfTime.DECADES): 1 / 60 / 24 / 365 / 10,
    (UnitOfTime.HOURS, UnitOfTime.SECONDS): 60 * 60,
    (UnitOfTime.HOURS, UnitOfTime.MINUTES): 60,
    (UnitOfTime.HOURS, UnitOfTime.HOURS): 1,
    (UnitOfTime.HOURS, UnitOfTime.DAYS): 1 / 24,
    (UnitOfTime.HOURS, UnitOfTime.WEEKS): 1 / 24 / 7,
    (UnitOfTime.HOURS, UnitOfTime.MONTHS): 1 / 24 / 30,
    (UnitOfTime.HOURS, UnitOfTime.YEARS): 1 / 24 / 30 / 12,
    (UnitOfTime.HOURS, UnitOfTime.DECADES): 1 / 24 / 30 / 12 / 10,
    (UnitOfTime.DAYS, UnitOfTime.SECONDS): 24 * 60 * 60,
    (UnitOfTime.DAYS, UnitOfTime.MINUTES): 24 * 60,
    (UnitOfTime.DAYS, UnitOfTime.HOURS): 24,
    (UnitOfTime.DAYS, UnitOfTime.DAYS): 1,
    (UnitOfTime.DAYS, UnitOfTime.WEEKS): 1 / 7,
    (UnitOfTime.DAYS, UnitOfTime.MONTHS): 1 / 30,
    (UnitOfTime.DAYS, UnitOfTime.YEARS): 1 / 365,
    (UnitOfTime.DAYS, UnitOfTime.DECADES): 1 / 365 / 10,
    (UnitOfTime.WEEKS, UnitOfTime.SECONDS): 1 / 7 / 24 / 60 / 60,
    (UnitOfTime.WEEKS, UnitOfTime.MINUTES): 1 / 7 / 24 / 60,
    (UnitOfTime.WEEKS, UnitOfTime.HOURS): 1 / 7 / 24,
    (UnitOfTime.WEEKS, UnitOfTime.DAYS): 1 / 7,
    (UnitOfTime.WEEKS, UnitOfTime.WEEKS): 1,
    (UnitOfTime.WEEKS, UnitOfTime.MONTHS): 1 / 4,
    (UnitOfTime.WEEKS, UnitOfTime.YEARS): 1 / 52,
    (UnitOfTime.WEEKS, UnitOfTime.DECADES): 1 / 52 / 10,
    (UnitOfTime.MONTHS, UnitOfTime.SECONDS): 720 * 60 * 60,
    (UnitOfTime.MONTHS, UnitOfTime.MINUTES): 720 * 60,
    (UnitOfTime.MONTHS, UnitOfTime.HOURS): 720,
    (UnitOfTime.MONTHS, UnitOfTime.DAYS): 30,
    (UnitOfTime.MONTHS, UnitOfTime.WEEKS): 4,
    (UnitOfTime.MONTHS, UnitOfTime.MONTHS): 1,
    (UnitOfTime.MONTHS, UnitOfTime.YEARS): 1 / 12,
    (UnitOfTime.MONTHS, UnitOfTime.DECADES): 1 / 12 / 10,
    (UnitOfTime.YEARS, UnitOfTime.SECONDS): 31536000,
    (UnitOfTime.YEARS, UnitOfTime.MINUTES): 525600,
    (UnitOfTime.YEARS, UnitOfTime.HOURS): 8760,
    (UnitOfTime.YEARS, UnitOfTime.DAYS): 365,
    (UnitOfTime.YEARS, UnitOfTime.WEEKS): 52,
    (UnitOfTime.YEARS, UnitOfTime.MONTHS): 12,
    (UnitOfTime.YEARS, UnitOfTime.YEARS): 1,
    (UnitOfTime.YEARS, UnitOfTime.DECADES): 1 / 10,
    (UnitOfTime.DECADES, UnitOfTime.SECONDS): 315360000,
    (UnitOfTime.DECADES, UnitOfTime.MINUTES): 5256000,
    (UnitOfTime.DECADES, UnitOfTime.HOURS): 87600,
    (UnitOfTime.DECADES, UnitOfTime.DAYS): 3650,
    (UnitOfTime.DECADES, UnitOfTime.WEEKS): 520,
    (UnitOfTime.DECADES, UnitOfTime.MONTHS): 120,
    (UnitOfTime.DECADES, UnitOfTime.YEARS): 10,
    (UnitOfTime.DECADES, UnitOfTime.DECADES): 1,
}


class TimeExpression(BaseModel):
    amount: float
    unit: UnitOfTime

    @staticmethod
    def get_multiplier_for(old_unit: UnitOfTime, new_unit: UnitOfTime) -> float:
        return TIME_EXPRESSION_MULTIPLIERS[(old_unit, new_unit)]

    def to_unit(self, new_unit: UnitOfTime) -> "TimeExpression":
        return TimeExpression(
            amount=self.amount * self.get_multiplier_for(new_unit, self.unit),
            unit=new_unit,
        )
