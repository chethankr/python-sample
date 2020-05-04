'''
https://www.imagetracking.org.uk/2017/12/how-to-write-lossless-video-in-python/
To make something as cross-platform compatible as possible it would be nice to use FFmpeg.
There are a few python wrappers around, but as far as I can tell they are mainly used for transcoding type applications.
One solution is run FFmpeg as a subprocess and set its input to accept a pipe. Then every video frame is passed
through the pipe. You write this yourself, in fact it's only a few lines of code.
However, the scikit-video package will do this for us, with some nice boilerplate to make life easier.

The steps are:

install FFmpeg -- if you running on Linux use your system's package manager if it's not already installed.
If you're unlucky enough to be using Windows you need to download the zip file from here,
and add the bin directory to your system's path.

install scikit-video --I tried installing scikit-video via pip on my Anaconda distro but the version was too old.
Instead, I cloned the github version and installed that. Instructions are provided on github.
Below is a simple example the grabs from your webcam and records lossless video.
'''

#test recording of video
import cv2
import skvideo.io


capture=cv2.VideoCapture(0) #open the default webcam
outputfile = "test.mp4"   #our output filename
writer = skvideo.io.FFmpegWriter(outputfile, outputdict={
  '-vcodec': 'libx264',  #use the h.264 codec
  '-crf': '0',           #set the constant rate factor to 0, which is lossless
  '-preset':'veryslow'   #the slower the better compression, in princple, try 
                         #other options see https://trac.ffmpeg.org/wiki/Encode/H.264
}) 
while True:
    ret,frame=capture.read()
    if ret==False:
        print("Bad frame")
        break
    cv2.imshow('display',frame)
    writer.writeFrame(frame[:,:,::-1])  #write the frame as RGB not BGR
    ret=cv2.waitKey(10)
    if ret==27: #esc
        break

writer.close() #close the writer
capture.release()
cv2.destroyAllWindows()