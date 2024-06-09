from sqlalchemy import select, desc
from core.database import async_session_maker
from core.models.models import Video


class BaseDao:
    model = Video

    @classmethod
    async def show_50_video(cls,load_previous=False, video_id=None):
        async with async_session_maker() as session:
            query = (select(cls.model.__table__.columns).
                     limit(50).order_by(desc(cls.model.id)))

            if load_previous and video_id is not None:
                query = query.where(cls.model.id < video_id)

            result = await session.execute(query)

            return result.mappings().all()
