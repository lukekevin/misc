from moviepy.editor import *

def clip_videos(file_list):
    print('Enter start and end times for clipping:')
    start_time = float(input("Start time (in seconds): "))
    end_time = float(input("End time (in seconds): "))
    
    for file in file_list:
        video = VideoFileClip(file)
        clipped = video.subclip(start_time, end_time)
        clipped.write_videofile(file[:-4] + "_clipped.mp4")

def resize_videos(file_list):
    height_val = int(input('Enter the height for resizing: '))
    
    for file in file_list:
        video = VideoFileClip(file)
        resized = video.resize(height=height_val)
        resized.write_videofile(file[:-4] + "_resized.mp4")

def merge_videos(file_list):
    merged = concatenate_videoclips([VideoFileClip(file) for file in file_list])
    merged.write_videofile('merged.mp4')

def flip_videos(file_list):
    flip_angle = int(input('Enter the flip angle (in degrees): '))
    
    for file in file_list:
        video = VideoFileClip(file)
        flipped = video.rotate(flip_angle)
        flipped.write_videofile(file[:-4] + "_flipped.mp4")

def mute_videos(file_list):
    for file in file_list:
        video = VideoFileClip(file)
        muted = video.without_audio()
        muted.write_videofile(file[:-4] + "_muted.mp4")

def main():
    print('***********Welcome to Kevin Lukes simple Python-based video editor.************\n')
    print('This video editor uses MoviePy library which itself is built upon FFmpeg.\n')
    print('My code provides a clean wrapper to enable various video editing options from MoviePy.\n')
    
    operation = input("Select the operation to perform (clip, resize, merge, flip, mute): ").lower()
    
    file_list = input("Enter a list of video files separated by spaces: ").split()
    
    if operation == "clip":
        clip_videos(file_list)

    elif operation == "resize":
        resize_videos(file_list)

    elif operation == "merge":
        merge_videos(file_list)

    elif operation == "flip":
        flip_videos(file_list)

    elif operation == "mute":
        mute_videos(file_list)

if __name__ == "__main__":
    main()
