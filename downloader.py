import json
import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime as dt

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
JSON_FILE = 'out.json'

def main():
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    timeA = dt.now()

    with open(JSON_FILE, 'r') as f:    
        data = json.load(f)
        for i, entry in enumerate(data):

            id = entry['id']
            output = './images/' + str(id) + '.png'
            
            if os.path.exists(output):
                print("[{0}/{1}] Photo #{2} already exists! Skipping...".format(i + 1, len(data), id))
            else:
                print("[{0}/{1}] Downloading photo #{2}".format(i + 1, len(data), id))

                id = entry['file_url'].split('=')[1]
                
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

    timeB = dt.now()
    
    print('Time taken: ' + str(timeB - timeA))

if __name__ == "__main__":
    main()