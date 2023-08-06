from pydantic import BaseModel

from .units import TimeExpression, UnitOfTime


class TimeExpressionRequst(BaseModel):
    original: TimeExpression
    in_time: TimeExpression
    comparison: TimeExpression


def transform(
    request: TimeExpressionRequst,
    resolution: UnitOfTime,
) -> TimeExpression:
    in_time_converted = request.in_time.to_unit(request.comparison.unit)

    amount = (
        request.original.amount
        * in_time_converted.amount
        * TimeExpression.get_multiplier_for(request.original.unit, resolution)
        * request.comparison.amount
    )

    return TimeExpression(amount=amount, unit=resolution)
