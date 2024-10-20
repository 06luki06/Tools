import os
import sys
import argparse
from pydub import AudioSegment

def trim_mp3(file_path, begin=None, end=None):
    """
    Trim an MP3 file based on the given start and end times.

    :param file_path: Path to the MP3 file to be trimmed.
    :param begin: Start time in seconds. All audio before this point will be removed.
    :param end: End time in seconds. All audio after this point will be removed.
    """
    try:
        audio = AudioSegment.from_mp3(file_path)

        start_ms = begin * 1000 if begin is not None else 0
        end_ms = end * 1000 if end is not None else len(audio)

        trimmed_audio = audio[start_ms:end_ms]

        base, _ = os.path.splitext(file_path)
        output_file = f"{base}_trimmed.mp3"

        trimmed_audio.export(output_file, format="mp3")
        print(f"Trimmed file saved as: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim an MP3 file by specifying start and end times.")
    parser.add_argument("-f", "--file", required=True, help="Path to the MP3 file to be trimmed.")
    parser.add_argument("-b", "--begin", type=float, help="Start time in seconds. Everything before this point will be removed.")
    parser.add_argument("-e", "--end", type=float, help="End time in seconds. Everything after this point will be removed.")

    args = parser.parse_args()

    if args.begin is None and args.end is None:
        print("Error: You must specify at least one of --begin or --end.")
        sys.exit(1)

    trim_mp3(args.file, args.begin, args.end)
