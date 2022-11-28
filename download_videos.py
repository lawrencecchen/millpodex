import os

channel_url = "https://www.youtube.com/@MyFirstMillionPod/videos"

os.system(f"yt-dlp -x --audio-format mp3 -o \"audio/%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s __id__=##%(id)s##.%(ext)s\" -- \"{channel_url}\"")