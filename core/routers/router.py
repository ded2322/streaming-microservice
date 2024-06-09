from fastapi import APIRouter

from core.dao.dao import BaseDao

router = APIRouter(
    prefix="/show-video-service",
    tags=["Show-video-service"],
)


@router.get("/last-videos", status_code=200, summary="Show all videos")
async def show_video_service():
    """
    Отображает последние 50 видео
    """
    return await BaseDao.show_50_video()


@router.get("/load")
async def load_video(video_id: int):
    """
    Подгружает дополнительные 50 видео
    """
    return await BaseDao.show_50_video(load_previous=True, video_id=video_id)
