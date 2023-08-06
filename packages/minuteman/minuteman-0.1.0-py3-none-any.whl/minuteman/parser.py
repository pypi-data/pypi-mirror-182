from .core import TimeExpressionRequst, transform
from .units import TimeExpression, UnitOfTime

# Sample expression:
# 5 minutes a day in 1 year in days


def validate_parts(
    expression: str,
) -> tuple[TimeExpression, TimeExpression, TimeExpression, UnitOfTime]:
    raw_parts = expression.split()

    # Expressions should always have same length
    assert len(raw_parts) == 9

    # Expressions should always contain certain in-betweens
    assert raw_parts[2] in ["a", "per"]
    assert raw_parts[4] == "in"
    assert raw_parts[7] == "in"

    # Ensure correct types.
    origin_amount = int(raw_parts[0])
    origin_unit = UnitOfTime.from_str(raw_parts[1])

    in_time_amount = 1
    in_time_unit = UnitOfTime.from_str(raw_parts[3])

    comparison_amount = int(raw_parts[5]) if raw_parts[5] != "a" else 1
    comparison_unit = UnitOfTime.from_str(raw_parts[6])

    resolution = UnitOfTime.from_str(raw_parts[8])

    return (
        TimeExpression(amount=origin_amount, unit=origin_unit),
        TimeExpression(amount=in_time_amount, unit=in_time_unit),
        TimeExpression(amount=comparison_amount, unit=comparison_unit),
        resolution,
    )


def parse(expression: str, rounding_decimals: int | None = None) -> str:
    original, in_time, comparison, resolution = validate_parts(expression)
    result = transform(
        TimeExpressionRequst(
            original=original,
            in_time=in_time,
            comparison=comparison,
        ),
        resolution,
    )

    amount = (
        round(result.amount, rounding_decimals) if rounding_decimals else result.amount
    )

    # Indicating zero decimals should result in non-float value
    if rounding_decimals == 0:
        amount = int(amount)

    return f"{amount} {result.unit.value}"
