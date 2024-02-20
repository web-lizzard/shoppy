import uuid
from datetime import timezone, datetime

from sqlalchemy import Column, String, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, TypeDecorator


class TimezoneAwareDateTime(TypeDecorator):
    """Results returned as aware datetimes, not naive ones."""

    impl = DateTime

    def process_result_value(self, value, _):
        if value:
            return value.replace(tzinfo=timezone.utc)
        return value


class IdentifierMixin:
    id = Column(
        String(36),
        primary_key=True,
        index=True,
        unique=True,
        nullable=True,
        default=lambda: str(uuid.uuid4()),
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TimezoneAwareDateTime, default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        TimezoneAwareDateTime, default=func.now()
    )
