import uuid
from datetime import timezone

from sqlalchemy import Column, String, func
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
    created_at = Column(TimezoneAwareDateTime, default=func.now())
    modified_at = Column(TimezoneAwareDateTime, default=func.now())
    deleted_at = Column(TimezoneAwareDateTime)
