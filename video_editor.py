from moviepy.editor import *


print('***********Welcome to Kevin Lukes simple python based video editor.************\n')
print('This video editor uses moviepy library which itself is built upon ffmpeg.\n')
print('My code provides a clean wrapper to enable various video editing options from moviepy.\n')

#Pass the names of the video or videos with their paths here
file_list=['vid1.mp4','vid2.mp4', 'vid3.mp4']
editing='resizing'

if editing=='clipping':
    print('Video/s will be clipped')
    start_time=int(input())
    end_time=int(input())
    for file in file_list:
        #Load the videoflies in moviepy
        video=VideoFileClip(file)
        clipped=video.subclip(start_time,end_time)
        #Save the video file
        clipped.write_videofile(file[:-4]+"_clipped.mp4")

elif editing=='resizing':
    print('Write the height of the video to be resized')
    height_val=int(input())
    for file in file_list:
        video=VideoFileClip(file)
        resized=video.resize(height=height_val)
        resized.write_videofile(file[:-4]+"_resized.mp4")

elif editing=='merging': 
    merged=concatenate_videoclips([VideoFileClip(file) for file in file_list])
    merged.write_videofile('merged.mp4')

elif editing=='flipping':
    flip_angle=int(input())
    for file in file_list:
        video=VideoFileClip(file)
        flipped=video.rotate(flip_angle)
        flipped.write_videofile(file[:-4]+"_flipped.mp4")

elif editing=='muting':
    for file in file_list:
        video=VideoFileClip(file)
        mutted=video.without_audio()
        mutted.write_videofile(file[:-4]+"_mutted.mp4")