from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 設置憑據
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/Users/liyunyun/Desktop/finalproject-446113-c8489e1729fe.json'

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# 上傳文件到 Google Drive
file_metadata = {
    'name': 'Cars126.png',  # 替換為您要上傳的文件名
    'parents': ['your-folder-id-here']  # 替換為資料夾 ID
}
media = MediaFileUpload('/Users/liyunyun/Desktop/Images/Cars126.png', mimetype='image/png')
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print('Uploaded file ID:', file.get('id'))

# 生成下載 URL
download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
print("Download URL:", download_url)