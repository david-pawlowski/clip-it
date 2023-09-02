import cv2
import os


def make_video(image_folder, video_name):
    """
    Creates video from screenshots
    """

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter(
        video_name, cv2.VideoWriter_fourcc(*"mp4v"), 10, (width, height)
    )

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
