from argparse import ArgumentParser
from pathlib import Path  # Import the Path module
from model_mediapipe import model_mediapipe_image
from model_mediapipe import model_mediapipe_video
from model_mediapipe import mediapipe_process_videos_in_directory


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--source', help=' the source of the image ')
    parser.add_argument('--model', help='The model which you want to use to predict')
    parser.add_argument('--input_type', default="video", help='video or image')
    parser.add_argument('--img_path', help='path of the image tou want to evaluate')
    parser.add_argument('--vid_path', default= 0, help='path of the video(s) you want to evaluate')
    parser.add_argument('--device', default='cuda:0', help='Device used for inference')
    parser.add_argument("--show_img", default=True, help="if you want ot show the image")
    parser.add_argument("--save_img", default=True, help="If you want to save the image")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.model == 'mediapipe':
        if args.input_type == 'image':
            model_mediapipe_image(img_path=args.img_path, show_img=args.show_img)
        if args.input_type == 'video':
            mediapipe_process_videos_in_directory(args.vid_path)
        if args.input_type == 'webcam':
            model_mediapipe_video(0)
    elif args.model == 'openpose':
        from model_openpose import model_openpose
        # Convert the paths to Path objects
        openpose_exe_path = Path(r"F:\UoA\IDEALab\MMC_models\openpose1.6")
        vid_path = Path(str(args.vid_path))
        model_openpose(openPoseExePath=openpose_exe_path, VidPath=vid_path)
#s
if __name__ == '__main__':
    main()

#test