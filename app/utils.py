from __future__ import annotations

import datetime as dt
from dataclasses import dataclass


INCOMING_CATEGORIES = ["Daraz Me", "Client", "Other"]
OUTGOING_CATEGORIES = [
    "Employee",
    "Polish Wala",
    "Poshish Wala",
    "Polish & Poshish Material",
    "Karkhanay Wala",
    "Karaya",
    "Committee",
    "Rent",
    "Bill",
    "Kharcha",
    "Zaati Kharcha",
]

EMPLOYEE_CATEGORIES = [
    "Factory Worker (Karkhanay Wala)",
    "Polish Worker",
    "Upholstery / Poshish Worker",
    "Helper / Mazdoor",
    "Delivery / Loader",
    "Supervisor / Office Staff",
    "Contract / Per-Work Employee",
]

EMPLOYEE_WORK_TYPES = [
    "daily",
    "weekly",
    "per_item",
    "contract",
]

EMPLOYEE_TX_TYPES = [
    "salary",
    "advance",
    "per_work",
    "expense",
]

PAYMENT_METHODS = [
    "cash",
    "bank",
    "jazzcash",
    "easypaisa",
]


def parse_date(value: str | None) -> dt.date | None:
    if not value:
        return None
    return dt.date.fromisoformat(value)


def pkr_format(amount_pkr: int) -> str:
    return f"PKR {amount_pkr:,.0f}"


@dataclass(frozen=True)
class WeekRange:
    start: dt.date
    end: dt.date


def sat_thu_week_range(anchor: dt.date) -> WeekRange:
    weekday = anchor.weekday()
    days_since_sat = (weekday - 5) % 7
    start = anchor - dt.timedelta(days=days_since_sat)
    end = start + dt.timedelta(days=5)
    return WeekRange(start=start, end=end)


def clamp_date_range(from_date: dt.date | None, to_date: dt.date | None) -> tuple[dt.date | None, dt.date | None]:
    if from_date and to_date and from_date > to_date:
        return to_date, from_date
    return from_date, to_date
