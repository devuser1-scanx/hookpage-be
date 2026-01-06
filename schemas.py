from pydantic import BaseModel

class CouponBase(BaseModel):
    coupon_name: str
    discount: int
    coupon_usage: int

class CouponCreate(CouponBase):
    pass

class Coupon(CouponBase):
    id: int
