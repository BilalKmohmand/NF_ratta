from __future__ import annotations

import datetime as dt

from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from .db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    type = Column(String(16), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    amount_pkr = Column(Integer, nullable=False)

    category = Column(String(64), nullable=False, index=True)
    name = Column(String(128), nullable=True, index=True)
    bill_no = Column(String(64), nullable=True, index=True)
    notes = Column(Text, nullable=True)

    is_deleted = Column(Boolean, nullable=False, default=False, index=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"<Transaction id={self.id} type={self.type} date={self.date} amount_pkr={self.amount_pkr}>"
