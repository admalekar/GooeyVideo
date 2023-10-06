from __future__ import absolute_import
from gooey import Gooey, GooeyParser

from gooey_video import gif
from gooey_video import screen_recorder
from gooey_video import slideshow
from gooey_video import trim_crop
from gooey_video import watermark
from gooey_video import extract_audio
from gooey_video import remove_audio




@Gooey(program_name='Gooey Video Tools')
def main():
    parser = GooeyParser(description='A collection of common FFMPEG commands')
    subparsers = parser.add_subparsers(help='commands', dest='command')
    screen_recorder.add_parser(subparsers)
    gif.add_parser(subparsers)
    trim_crop.add_parser(subparsers)
    slideshow.add_parser(subparsers)
    watermark.watermark_parser(subparsers)
    extract_audio.extract_audio_parser(subparsers)
    remove_audio.remove_audio_parser(subparsers)
    

    args = parser.parse_args()
    globals()[args.command].run(args)


if __name__ == '__main__':
    main()