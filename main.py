from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--source', help=' the source of the image ')
    parser.add_argument('--model', help='The model which you want to use to predict')
    parser.add_argument('--img_path', help='path of the image tou want to evaluate')
    parser.add_argument('--device', default='cuda:0', help='Device used for inference')
    parser.add_argument("--show_img", default=True, help="if you want ot show the image")
    parser.add_argument("--save_img", default=True, help="If you want to save the image")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.model == 'mediapipe':
        from model_mediapipe import model_mediapipe
        model_mediapipe(img_path=args.img_path, show_img=args.show_img)


if __name__ == '__main__':
    main()
