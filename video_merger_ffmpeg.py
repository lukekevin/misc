import os
import glob
import subprocess

#Write all the names for txt files, out file, extension within a dir
vid_ext='/home/kevin/sam/*.mp4'  #vid extension to be searched in a dir
txt_nm_for_ffmpeg='sam.txt'  #for ffmpeg you need a txt file with each line as 'file /path/to/dir/vid.mp4
out_vid_nm='sam.mp4' #output vid name
#glob out the files to be compiled with a given extension
list=glob.glob(vid_ext)

#for ffmpeg you need a txt file with each line as 'file /path/to/dir/vid.mp4' 
#for each vid file to be merged
new_list=[]
for comp in list:
    appended_list='file'+' '+ comp
    new_list.append(appended_list)

#make the txt file as mentioned above
with open(txt_nm_for_ffmpeg, "w") as txt_nm:
        for item in (new_list):
            txt_nm.write(item + "\n")

#run ffmpeg
subprocess.run("ffmpeg -f concat -safe 0 -i {0:s} -c copy {1:s}".format(txt_nm_for_ffmpeg,
                                                                       out_vid_nm), 
               shell=True,
               cwd=os.getcwd())


#RUN THIS CODE IN THE DIR WHERE ALL VIDS ARE PRESENT
