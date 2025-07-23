#!/usr/bin/env python3
"""
YouTube Video Downloader
Download YouTube videos in highest quality MP4 format
"""

import os
import sys
import argparse
from pathlib import Path
import yt_dlp
from datetime import datetime

class YouTubeDownloader:
    def __init__(self, download_path="./downloads"):
        """
        Initialize YouTube Downloader
        
        Args:
            download_path (str): Path where videos will be downloaded
        """
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Configure yt-dlp options for highest quality MP4
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': str(self.download_path / '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'writeinfojson': False,
            'writesubtitles': False,
            'writeautomaticsub': False,
            'ignoreerrors': True,
            'no_warnings': False,
        }
    
    def download_video(self, url):
        """
        Download a single video
        
        Args:
            url (str): YouTube video URL
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                print(f"Downloading: {url}")
                
                # Get video info first
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)
                
                # Format duration
                duration_str = f"{duration//60}:{duration%60:02d}" if duration else "Unknown"
                
                print(f"Title: {title}")
                print(f"Duration: {duration_str}")
                print(f"Saving to: {self.download_path}")
                
                # Download the video
                ydl.download([url])
                
                print(f"Download completed: {title}")
                return True
                
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")
            return False
    
    def download_playlist(self, url):
        """
        Download all videos from a playlist
        
        Args:
            url (str): YouTube playlist URL
            
        Returns:
            tuple: (successful_downloads, total_videos)
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                print(f"Processing playlist: {url}")
                
                # Get playlist info
                info = ydl.extract_info(url, download=False)
                playlist_title = info.get('title', 'Unknown Playlist')
                entries = info.get('entries', [])
                
                print(f"Playlist: {playlist_title}")
                print(f"Found {len(entries)} videos")
                
                successful = 0
                for i, entry in enumerate(entries, 1):
                    if entry:
                        video_url = entry.get('webpage_url') or f"https://youtube.com/watch?v={entry['id']}"
                        print(f"\n[{i}/{len(entries)}] Processing video...")
                        
                        if self.download_video(video_url):
                            successful += 1
                
                print(f"\nPlaylist download completed!")
                print(f"Successfully downloaded: {successful}/{len(entries)} videos")
                
                return successful, len(entries)
                
        except Exception as e:
            print(f"Error processing playlist {url}: {str(e)}")
            return 0, 0
    
    def download_from_file(self, file_path):
        """
        Download videos from a text file containing URLs
        
        Args:
            file_path (str): Path to text file with YouTube URLs
            
        Returns:
            tuple: (successful_downloads, total_urls)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            print(f"Found {len(urls)} URLs in {file_path}")
            
            successful = 0
            for i, url in enumerate(urls, 1):
                print(f"\n[{i}/{len(urls)}] Processing URL: {url}")
                if self.download_video(url):
                    successful += 1
            
            print(f"\nBatch download completed!")
            print(f"Successfully downloaded: {successful}/{len(urls)} videos")
            
            return successful, len(urls)
            
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return 0, 0
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")
            return 0, 0

def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos in highest quality MP4 format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://youtube.com/watch?v=VIDEO_ID"
  %(prog)s "https://youtube.com/playlist?list=PLAYLIST_ID"
  %(prog)s --file urls.txt
  %(prog)s --output ~/Videos "https://youtube.com/watch?v=VIDEO_ID"
        """
    )
    
    parser.add_argument(
        'url',
        nargs='?',
        help='YouTube video or playlist URL'
    )
    
    parser.add_argument(
        '--file', '-f',
        help='Text file containing YouTube URLs (one per line)'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='./downloads',
        help='Output directory for downloaded videos (default: ./downloads)'
    )
    
    args = parser.parse_args()
    
    # Check if we have either URL or file
    if not args.url and not args.file:
        parser.print_help()
        sys.exit(1)
    
    print("YouTube Downloader Started")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Initialize downloader
    downloader = YouTubeDownloader(args.output)
    
    try:
        if args.file:
            # Download from file
            successful, total = downloader.download_from_file(args.file)
            
        elif 'playlist' in args.url.lower():
            # Download playlist
            successful, total = downloader.download_playlist(args.url)
            
        else:
            # Download single video
            success = downloader.download_video(args.url)
            successful = 1 if success else 0
            total = 1
        
        print("\n" + "=" * 50)
        print(f"Download session completed!")
        print(f"Success rate: {successful}/{total} ({(successful/total*100):.1f}%)" if total > 0 else "No videos processed")
        
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
