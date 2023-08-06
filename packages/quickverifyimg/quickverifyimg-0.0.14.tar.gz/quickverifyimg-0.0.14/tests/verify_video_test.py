import time

from quickverifyimg.log.logger import get_logger
from quickverifyimg.quick_verify import QuickVerify
from quickverifyimg.quick_verify_video import QuickVerifyVideo

logger = get_logger(__name__)

if __name__ == '__main__':
    """
    crop_place：{ size: 需要识别的区域的大小， 百分比, offset: 需要识别的区域的左上角坐标点位置， 百分比}
    quick_verify: 是否快速校验，即不对已校验过的对照集图片继续校验
    """
    start_time = time.time()
    verify_engine_list = [
        ('ac_tpl', 0.99),
        ('hist', 0.995)
    ]
    origin_video = "./images/video/origin_video.mp4"
    target_video = "./images/video/target_video.mp4"
    crop_place = {"size": (0.48, 0.95), "offset": (0.13, 0)}
    verify_engine_list = [
        ('ac_tpl', 0.99, 0.9998),
        ('hist', 0.995, 0.9998)
    ]
    quick_v = QuickVerifyVideo(verify_engine_list, 0.8, crop_place=crop_place)
    quick_v.verify_video_effect(origin_video, target_video)