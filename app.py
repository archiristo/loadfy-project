from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

def download_video(url, format):
    ydl_opts = {
        'format': 'bestaudio/best' if format == 'mp3' else 'best',
        'outtmpl': 'static/downloads/%(title)s.%(ext)s',
        'cookiefile': 'static/cookies.txt',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}] if format == 'mp3' else []
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        filename = os.path.basename(filename)  # Dosya adını al

        # 🔥 Video adı ve thumbnail URL'sini alıyoruz
        title = info.get('title', 'Unknown Title')  
        thumbnail = info.get('thumbnail', '')

        if format == 'mp3':
            filename = filename.replace(".webm", ".mp3")

        print(f"🎬 Video Adı: {title}")
        print(f"🖼️ Thumbnail URL: {thumbnail}")
        
        return filename, title, thumbnail  


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        format = request.form['format']
        
        filename, title, thumbnail = download_video(url, format)

        return redirect(url_for('download', filename=filename, title=title, thumbnail=thumbnail))
    
    return render_template('index.html')


@app.route('/download/<filename>')
def download(filename):
    # URL parametrelerini al
    title = request.args.get('title', 'Unknown Title')
    thumbnail = request.args.get('thumbnail', '')

    return render_template('download.html', filename=filename, title=title, thumbnail=thumbnail)


if __name__ == '__main__':
    app.run(debug=True)
