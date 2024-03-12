from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# 指定存放多个 AVI 视频文件的文件夹路径
video_folder_path = r"E:\seg-master\VIDEO"

# 获取视频文件列表
video_files = [f for f in os.listdir(video_folder_path) if f.endswith(".avi")]

# 读取每个 AVI 视频文件并转换为 VideoFileClip 对象
video_clips = []
for video_file in video_files:
    video_clip = VideoFileClip(os.path.join(video_folder_path, video_file))
    video_clips.append(video_clip)

# 将所有 VideoFileClip 对象连接起来
final_clip = concatenate_videoclips(video_clips)

# 将合成的视频保存为 MP4 格式
final_clip.write_videofile("output_video.mp4", codec="libx264")

# 关闭视频对象
final_clip.close()