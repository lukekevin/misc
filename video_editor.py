import argparse
from moviepy.editor import *

def clip_videos(file_list, start_time, end_time):
    for file in file_list:
        video = VideoFileClip(file)
        clipped = video.subclip(start_time, end_time)
        clipped.write_videofile(file[:-4] + "_clipped.mp4")

def resize_videos(file_list, height_val):
    for file in file_list:
        video = VideoFileClip(file)
        resized = video.resize(height=height_val)
        resized.write_videofile(file[:-4] + "_resized.mp4")

def merge_videos(file_list):
    merged = concatenate_videoclips([VideoFileClip(file) for file in file_list])
    merged.write_videofile('merged.mp4')

def flip_videos(file_list, flip_angle):
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
    parser = argparse.ArgumentParser(description="Simple video editor using MoviePy.")
    parser.add_argument("operation", choices=["clip", "resize", "merge", "flip", "mute"], help="Select the operation to perform")
    parser.add_argument("files", nargs="+", help="List of video files to edit")
    
    args = parser.parse_args()

    if args.operation == "clip":
        print('Enter start and end times for clipping:')
        start_time = int(input())
        end_time = int(input())
        clip_videos(args.files, start_time, end_time)

    elif args.operation == "resize":
        print('Enter the height for resizing:')
        height_val = int(input())
        resize_videos(args.files, height_val)

    elif args.operation == "merge":
        merge_videos(args.files)

    elif args.operation == "flip":
        print('Enter the flip angle:')
        flip_angle = int(input())
        flip_videos(args.files, flip_angle)

    elif args.operation == "mute":
        mute_videos(args.files)

if __name__ == "__main__":
    main()
