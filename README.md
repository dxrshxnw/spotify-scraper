# Spotify to YouTube Downloader

This script fetches all songs from a Spotify playlist and downloads them from YouTube as MP3 files using `yt-dlp`.

## Requirements

Before running the script, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg] (https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z)
- [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/) (to interact with Spotify API)

To install dependencies, run:
```sh
pip install -r requirements.txt
```

## Setting Up Spotify API
1. Register an application on [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Get your `CLIENT_ID` and `CLIENT_SECRET`.
3. Set up environment variables:
   ```sh
   export SPOTIPY_CLIENT_ID="your_client_id"
   export SPOTIPY_CLIENT_SECRET="your_client_secret"
   export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"
   ```
   For Windows (PowerShell):
   ```powershell
   $env:SPOTIPY_CLIENT_ID="your_client_id"
   $env:SPOTIPY_CLIENT_SECRET="your_client_secret"
   $env:SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"
   ```
    OR

    just create a `.env` file and copy paste the following (recommended)
    ```env
    SPOTIFY_CLIENT_ID = ""
    SPOTIFY_CLIENT_SECRET = ""
    SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"
     = ""
    ```PLAYLIST_ID

## Usage

Run the script with:
```sh
python main.py
```

### Inside the Script
The script:
1. Fetches all songs from the given Spotify playlist.
2. Searches each song on YouTube.
3. Downloads the best-quality MP3 using `yt-dlp`.



## Troubleshooting

### Permission Denied Error
If you encounter a `Permission denied` error:
- Run the script as Administrator (Windows) or with `sudo` (Linux/macOS).
- Ensure `songs` is not a file but a directory.

### FFmpeg Not Found
If `yt-dlp` fails with an FFmpeg error:
- Ensure ffmpeg.exe is present withing the same directory

### Spotify API Authentication Issues
- Double-check `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI` and `PLAYLIST_ID`.
- Ensure your Spotify account has access to the playlist.

## License
This project is open-source under the MIT License.

