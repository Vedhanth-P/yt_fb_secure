import requests, os, json
def upload_video_to_facebook(page_id: str, access_token: str, video_path: str, title: str, description: str):
    url = f"https://graph.facebook.com/{page_id}/videos"
    files = {'source': open(video_path, 'rb')}
    data = {
        'title': title,
        'description': description,
        'access_token': access_token
    }
    r = requests.post(url, files=files, data=data, timeout=600)
    try:
        res = r.json()
    except Exception:
        r.raise_for_status()
    if 'error' in res:
        raise Exception(res['error'])
    return res
