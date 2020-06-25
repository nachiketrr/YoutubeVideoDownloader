from flask import Flask,request,render_template
import pytube
import os
import youtube_dl

app = Flask(__name__, template_folder='front')

def youtube_downloader(url):
    video_url = url # copy and paste url
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download('Download/') # path, where to video download



@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/thankyou', methods=['POST'])
def getValue():
    print("Hello")
    url = request.form['search']
    print(url)
    youtube_downloader(url)
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)