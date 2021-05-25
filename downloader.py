import json
import gdown

import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

JSON_FILE = 'out.json'
with open(JSON_FILE, 'r') as f:    
    data = json.load(f)
    for i, entry in enumerate(data):

        id = entry['id']
        print("[{0}/{1}] Downloading photo #{2}".format(i + 1, len(data), id))

        id = entry['file_url'].split('=')[1]
        output = './images/' + id + '.png'
        
        request = service.files().get_media(fileId=id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False

        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)

        with open(os.path.join(output), 'wb') as f:
            f.write(fh.read())
            f.close()
        # gdown.download(url, output, quiet=False)
