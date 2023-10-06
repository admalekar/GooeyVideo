from gooey import Gooey, GooeyParser, options
import subprocess
'''

ffmpeg -i $input_file -c copy -an $output_file

'''
def remove_audio_parser(parent):
    parser = parent.add_parser('remove_audio', prog="Remove audio from Video", help='Where does this show??')
    input_group = parser.add_argument_group('Input', gooey_options=options.ArgumentGroup(
        show_border=True
    ))
    input_group.add_argument(
        'input',
        metavar='Input',
        help='The video you want to extract audio from',
        default=r'C:\Users\Chris\Desktop\Recording #1.mp4',
        widget='FileChooser',
        gooey_options=options.FileChooser(
            wildcard='video files (*.mp4)|*.mp4',
            full_width=True
    ))


    output_group = parser.add_argument_group('Output', gooey_options=options.ArgumentGroup(
        show_border=True
    ))
    output_group.add_argument(
        'output',
        help='Choose where to save the output video file',
        default=r'C:\Users\Chris\Desktop\output.mp4',
        widget='FileSaver',
        gooey_options=options.FileSaver(
            wildcard='video files (*.mp4)|*.mp4',
            default_file='output.mp4',
            full_width=True
        ))

    output_group.add_argument(
        '--overwrite',
        metavar='Overwrite existing',
        help='Overwrite the output video if it already exists?',
        action='store_const',
        default=True,
        const='-y',
        widget='CheckBox')

    
    return parser



def run(args):
    cmd_template = 'ffmpeg.exe -i "{input}" ' \
                    '{overwrite} ' \
                   '-c copy -an ' \
                   '"{output}"'

    final_cmd = cmd_template.format(
        input=args.input,
        overwrite=args.overwrite,
        output=args.output
    )

    process = subprocess.Popen(
        final_cmd,
        bufsize=1,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        shell=True
    )
    for line in process.stdout:
        print(line)
