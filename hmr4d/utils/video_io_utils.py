import numpy as np
import imageio as iio

def read_video_np(video_path, scale=1):
    try:
        # 方法1：使用 opencv 替代
        import cv2
        cap = cv2.VideoCapture(video_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if scale != 1:
                frame = cv2.resize(frame, None, fx=scale, fy=scale)
            frames.append(frame)
        cap.release()
        return np.array(frames)
        
        # 或者方法2：修改 imageio 参数
        # return np.asarray(iio.imread(video_path, plugin="pyav"))  # 移除 filter_sequence
    except Exception as e:
        print(f"Error reading video: {e}")
        return None 