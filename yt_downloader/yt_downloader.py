import os
import sys
import yt_dlp

def download_video_as_mp3(url, output_path):
    """
    Download a video from YouTube as an MP3 using yt-dlp.

    :param url: The URL of the YouTube video to download.
    :param output_path: The directory to save the downloaded MP3.
    """
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Download error: {e}")
        except yt_dlp.utils.ExtractorError as e:
            print(f"Extractor error: {e}")
        except yt_dlp.utils.PostProcessingError as e:
            print(f"Post-processing error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python youtube_downloader.py <YouTube_URL> <Output_Directory>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.exists(output_directory):
        print(f"The directory '{output_directory}' does not exist. Creating it now...")
        os.makedirs(output_directory)

    download_video_as_mp3(youtube_url, output_directory)
    print("Download completed.")
