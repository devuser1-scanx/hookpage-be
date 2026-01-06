from dataclasses import dataclass


@dataclass(frozen=True)
class Coupon:
    id: int
    coupon_name: str
    discount: int
    coupon_usage: int
