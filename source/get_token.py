import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# スコープを設定
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def main():
    creds = None
    # 既存のトークンがある場合はロード
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # 有効なトークンがない場合は、新しく取得
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # 取得したトークンを保存
        with open("token.json", "w") as token:
            token.write(creds.to_json())

if __name__ == "__main__":
    main()
