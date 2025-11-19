# YouTube Video Downloader

A powerful Python script to download YouTube videos in the highest quality MP4 format, perfect for offline viewing on the go.

## Features

- Download videos in highest available quality
- Automatic conversion to MP4 format
- Playlist support
- Batch download from text file
- User-friendly command line interface
- Configurable download location
- Automatic merge of video and audio streams

## Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or download this project
```bash
cd ~/Documents/GitHub
git clone https://github.com/yyyutakaaa/youtube-downloader.git # or download files manually
cd youtube-downloader
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Alternative: Install yt-dlp directly
```bash
pip install yt-dlp
```

## Usage

### Basic usage - Single video
```bash
python youtube_downloader.py "https://youtube.com/watch?v=VIDEO_ID"
```

### Download to specific folder
```bash
python youtube_downloader.py --output ~/Videos "https://youtube.com/watch?v=VIDEO_ID"
```

### Download complete playlist
```bash
python youtube_downloader.py "https://youtube.com/playlist?list=PLAYLIST_ID"
```

### Batch download from file
```bash
python youtube_downloader.py --file urls.txt
```

### View help and options
```bash
python youtube_downloader.py --help
```

## Batch Download Setup

Create a text file (e.g. `urls.txt`) with YouTube URLs:

```text
# My favorite videos
https://youtube.com/watch?v=VIDEO_ID_1
https://youtube.com/watch?v=VIDEO_ID_2
https://youtube.com/playlist?list=PLAYLIST_ID

# Comment lines start with #
https://youtube.com/watch?v=VIDEO_ID_3
```

Download all videos:
```bash
python youtube_downloader.py --file urls.txt
```

## Examples

### Download single video to Desktop
```bash
python youtube_downloader.py --output ~/Desktop "https://youtube.com/watch?v=dQw4w9WgXcQ"
```

### Download playlist to Videos folder
```bash
python youtube_downloader.py --output ~/Videos "https://youtube.com/playlist?list=PLrRWBPJOUcAcLAHFJM56cqXRzFU3_ONJL"
```

### Batch download with custom location
```bash
python youtube_downloader.py --file my_videos.txt --output ~/Movies/YouTube
```

## Quality Settings

The script automatically downloads:
1. **Best quality MP4**: Tries highest quality video + audio in MP4 first
2. **Fallback option**: If MP4 not available, downloads best available format and converts
3. **Automatic merge**: Combines video and audio streams for best quality

## Output Structure

```
downloads/  (or your chosen folder)
├── Video Title 1.mp4
├── Video Title 2.mp4
└── Playlist Video Title.mp4
```

## Troubleshooting

### "yt-dlp not found" error
```bash
pip install --upgrade yt-dlp
```

### Permission errors on macOS/Linux
```bash
chmod +x youtube_downloader.py
```

### Python not found
Make sure Python 3 is installed:
```bash
python3 --version
```

Then use `python3` instead of `python`:
```bash
python3 youtube_downloader.py "https://youtube.com/watch?v=VIDEO_ID"
```

### Video not available
- Check if the video is publicly accessible
- Some videos have geographical restrictions
- Check your internet connection

## Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--output` | `-o` | Download directory (default: ./downloads) |
| `--file` | `-f` | Text file with URLs |
| `--help` | `-h` | Show help information |

## Supported Formats

- **Input**: YouTube video URLs, playlist URLs
- **Output**: MP4 video files (highest quality)
- **Audio**: AAC in M4A container, merged to MP4

## Important Notes

- Respect copyrights and YouTube's Terms of Service
- Only download content you have permission to download
- Some videos may be geographically blocked
- High quality videos can take up significant storage space

## Support

If you encounter issues:
1. Check your internet connection
2. Update yt-dlp: `pip install --upgrade yt-dlp`
3. Verify the video URL is correct
4. Try a different video to test

## License

This project is for educational purposes. Use responsibly and respect copyrights.
