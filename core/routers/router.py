from fastapi import APIRouter

from core.dao.dao import BaseDao

router = APIRouter(
    prefix="/streaming-microservice",
    tags=["Streaming microservice"],
)


@router.get("/last-videos", status_code=200, summary="Loading last 50 videos")
async def show_video_service():
    """
    Отображает последние 50 видео
    """
    return await BaseDao.show_50_video()


@router.get("/loading-videos", status_code=200, summary="Loading loading additional 50 messages")
async def load_video(video_id: int):
    """
    Подгружает дополнительные 50 видео
    """
    return await BaseDao.show_50_video(load_previous=True, video_id=video_id)
