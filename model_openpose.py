import os
import pandas as pd
import numpy as np
import json
import re
import os
import subprocess
import json
import numpy as np
from pathlib import Path

def model_openpose(openPoseExePath,VidPath):
    """
    Run OpenPose on synced videos, and save bdoy tracking data to be parsed
    """
    openPoseDataPath = VidPath
    os.chdir(openPoseExePath)

    openPose_jsonPathList = []
    openPose_imgPathList = []
    openPose_imgPathList_yaml = []
    openPose_jsonPathList_yaml = []
    outvidname=0
    for (
            thisVidPath
    ) in (
            VidPath.iterdir()
    ):  # Run OpenPose ('Windows Portable Demo') on each video in the raw video folder
        if (
                thisVidPath.suffix == ".mp4"
        ):  # NOTE - build some list of 'synced video names' and check against that
            print("OpenPosing: ", thisVidPath.name)
            outvidname += 1
            vidPath = openPoseDataPath /"output"/ thisVidPath.stem
            jsonPath = vidPath / "json"
            jsonPath.mkdir(
                parents=True, exist_ok=True
            )  # this camera's json files (with keypoints)
            imgPath = vidPath / "img"
            imgPath.mkdir(parents=True, exist_ok=True)
            outvidPath = vidPath / "video"
            outvidPath.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                [
                    "bin\OpenPoseDemo.exe",
                    "--video",
                    str(thisVidPath),
                    "--write_json",
                    str(jsonPath),
                    "--write_video",
                    str(outvidPath / (str(outvidname) + ".avi")),
                    # "--write_images",
                    # str(imgPath),
                    # "--write_images_format",
                    # "png",
                    "--net_resolution",
                    "-1x320", #The default resolution is -1x368, any resolution smaller will improve speed
                    # "--hand",
                    # "--face",
                    "--number_people_max",
                    "1",
                ],
                shell=True,
            )
        else:
            print("Skipping: ", thisVidPath.name)

    # os.chdir(sessionPath)



def json_to_csv(openpose_dir,JSON_dir):
    # initializes empty dataframe with names columns
    columns = ["NoseX", "NeckX", "RShoulderX", "RElbowX", "RWristX", "LShoulderX", "LElbowX", "LWristX", "MidHipX",
               "RHipX", "RKneeX", "RAnkleX", "LHipX", "LKneeX", "LAnkleX", "REyeX", "LEyeX", "REarX", "LEarX",
               "LBigToeX", "LSmallToeX", "LHeelX", "RBigToeX", "RSmallToeX", "RHeelX", "NoseY", "NeckY", "RShoulderY",
               "RElbowY", "RWristY", "LShoulderY", "LElbowY", "LWristY", "MidHipY", "RHipY", "RKneeY", "RAnkleY",
               "LHipY", "LKneeY", "LAnkleY", "REyeY", "LEyeY", "REarY", "LEarY", "LBigToeY", "LSmallToeY", "LHeelY",
               "RBigToeY", "RSmallToeY", "RHeelY", "File", "FrameNo", "Violation"]
    # creates empty dataframe with columns above
    df = pd.DataFrame(columns=columns)
    # Sets working directory to what is given by openpose_dir
    os.chdir(openpose_dir)
    if not os.path.isdir(JSON_dir):
        os.mkdir(JSON_dir)