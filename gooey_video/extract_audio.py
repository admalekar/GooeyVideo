from gooey import Gooey, GooeyParser, options
import subprocess

def extract_audio_parser(parent):
    parser = parent.add_parser('extract_audio', prog="Extract audio from Video", help='Where does this show??')
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
        help='Choose where to save the output audio file',
        default=r'C:\Users\Chris\Desktop\output.mp4',
        widget='FileSaver',
        gooey_options=options.FileSaver(
            wildcard='audio files (*.mp3)|*.mp3',
            default_file='output.mp3',
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

    settings = parser.add_argument_group(
        'Audio Settings',
        gooey_options=options.ArgumentGroup(
            show_border=True
    ))
    start_position = settings.add_mutually_exclusive_group(gooey_options=options.MutexGroup(
        initial_selection=0
    ))
    start_position.add_argument(
        '--start-ss',
        metavar='Start position',
        help='Start position in seconds',
        widget='IntegerField',
        gooey_options=options.IntegerField(
            min=0,
            max=99999,
            increment_size=1
        ))
    start_position.add_argument(
        '--start-ts',
        metavar='Start position',
        help='start-position as a concrete timestamp',
        gooey_options=options.TextField(
            placeholder='HH:MM:SS',
            validator=options.RegexValidator(
                test='^\d{2}:\d{2}:\d{2}$',
                message='Must be in the format HH:MM:SS'
            )
        ))

    end = settings.add_mutually_exclusive_group(
        gooey_options=options.MutexGroup(
        initial_selection=0
    ))
    end.add_argument(
        '--end-ss',
        metavar='End position',
        help='Total duration from the start (seconds)',
        widget='IntegerField',
        gooey_options=options.IntegerField(
            min=0,
            max=99999,
            increment_size=1
        ))
    end.add_argument(
        '--end-ts',
        metavar='End position',
        help='End position as a concrete timestamp',
        gooey_options=options.TextField(
            placeholder='HH:MM:SS',
            validator=options.RegexValidator(
                test='^\d{2}:\d{2}:\d{2}$',
                message='Must be in the format HH:MM:SS'
            )
        ))
    
    return parser



def run(args):
    cmd_template = 'ffmpeg.exe -i "{input}" ' \
                   '-q:a 0 -map a ' \
                   '"{output}"'

    final_cmd = cmd_template.format(
        input=args.input,
        #overwrite=args.overwrite,
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
