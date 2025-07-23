#!/bin/bash

# YouTube Downloader Setup Script
echo "🚀 Setting up YouTube Downloader..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"

# Install requirements
echo "📦 Installing requirements..."
python3 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Installation completed successfully!"
    echo ""
    echo "🎬 You can now use the YouTube downloader:"
    echo "   python3 youtube_downloader.py \"https://youtube.com/watch?v=VIDEO_ID\""
    echo ""
    echo "📖 For more options, run:"
    echo "   python3 youtube_downloader.py --help"
else
    echo "❌ Installation failed. Please check your Python and pip installation."
    exit 1
fi
