# Gooey Video

<p align="center">
    <img src="https://github.com/chriskiehl/GooeyVideo/raw/main/images/title.PNG" />
</p>


## Overview 
This project was started by chriskiehl but its not being developed further. I would like to expand the toolset to other small but handy tools to quickly edit the audio or video with a nice UI.

Currently it handles:  

 * Screen recording 
 * GIF conversion 
 * General Trim/Crop/Scaling utils 
 * Timelapse / Slideshow creation 
 * Watermarking
 * extracting Audio from video

This is not aimed at being a general purpose UI for FFMPEG. Its library aspirations climb only to the heights of: moderately useful for specific work flows.     

## Installation and Quick Start 

I ahve changed the setup from the original. 
_Be warned_, the [FFMPEG](https://ffmpeg.org/) binary is attached, which makes the installation footprint a whopping 70mb! 

```
git clone https://github.com/admalekar/GooeyVideo.git
cd GooeyVideo
python.exe -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
```
After the requirements are installed double click on start_gooeyVid.bat to start the GUI.

## Demos 

Screen Recording: 

<p align="center" width="400">
    <img src="https://github.com/chriskiehl/GooeyVideo/raw/main/images/demo-screen-recording.gif" />
</p>


Triming / Cropping / Scaling: 

<p align="center">
    <img src="https://github.com/chriskiehl/GooeyVideo/raw/main/images/demo-trim-crop-and-scale.gif" />
</p>

 ## TO DO

 * Added the demos for new tools
 * Remove audio from video
 * GIF to video
 * MP3 to WAV and WAV to MP3 


  
 

 


     

