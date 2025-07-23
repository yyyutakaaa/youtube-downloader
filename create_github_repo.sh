#!/bin/bash

# GitHub Repository Creator Script
# This script helps you create a new GitHub repository for the YouTube Downloader

echo "GitHub Repository Setup for YouTube Downloader"
echo "=============================================="

# Check if we're in the right directory
if [ ! -f "youtube_downloader.py" ]; then
    echo "Error: This script should be run from the youtube-downloader directory"
    echo "Please navigate to the correct directory first:"
    echo "cd ~/Documents/GitHub/youtube-downloader"
    exit 1
fi

# Repository details
REPO_NAME="youtube-downloader"
DESCRIPTION="A Python script to download YouTube videos in highest quality MP4 format"

echo "Repository Name: $REPO_NAME"
echo "Description: $DESCRIPTION"
echo ""

# Method 1: GitHub CLI (recommended)
echo "Method 1: Using GitHub CLI (recommended)"
echo "========================================"
echo "If you have GitHub CLI installed, run:"
echo ""
echo "gh repo create $REPO_NAME --public --description \"$DESCRIPTION\" --source=."
echo ""
echo "This will:"
echo "- Create a new repository on GitHub"
echo "- Add the remote origin"
echo "- Push your code"
echo ""

# Method 2: Manual setup
echo "Method 2: Manual Setup"
echo "======================"
echo "1. Go to https://github.com/new"
echo "2. Repository name: $REPO_NAME"
echo "3. Description: $DESCRIPTION"
echo "4. Make it Public"
echo "5. Don't initialize with README (we already have one)"
echo "6. Click 'Create repository'"
echo ""

# Git commands to run after creating repository
echo "After creating the repository, run these commands:"
echo "=================================================="
echo ""
echo "# Initialize git (if not already done)"
echo "git init"
echo ""
echo "# Add all files"
echo "git add ."
echo ""
echo "# Create initial commit"
echo "git commit -m \"Initial commit: YouTube video downloader with MP4 support\""
echo ""
echo "# Add your GitHub repository as remote (replace YOUR_USERNAME)"
echo "git remote add origin https://github.com/YOUR_USERNAME/$REPO_NAME.git"
echo ""
echo "# Set main branch"
echo "git branch -M main"
echo ""
echo "# Push to GitHub"
echo "git push -u origin main"
echo ""

# Check if GitHub CLI is installed
echo "Checking for GitHub CLI..."
if command -v gh &> /dev/null; then
    echo "✓ GitHub CLI is installed!"
    echo ""
    read -p "Do you want to create the repository now using GitHub CLI? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Creating repository..."
        gh repo create $REPO_NAME --public --description "$DESCRIPTION" --source=.
        echo "Repository created successfully!"
    fi
else
    echo "✗ GitHub CLI not found"
    echo "Install it with: brew install gh"
    echo "Or use Method 2 (Manual Setup) above"
fi

echo ""
echo "Done! Your YouTube Downloader repository is ready to share!"
