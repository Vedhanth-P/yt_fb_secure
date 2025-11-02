import requests
from urllib.parse import urlencode
def fetch_video_metadata(youtube_api_key: str, video_id: str):
    params = {
        'part': 'snippet',
        'id': video_id,
        'key': youtube_api_key
    }
    url = 'https://www.googleapis.com/youtube/v3/videos?' + urlencode(params)
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    data = r.json()
    items = data.get('items', [])
    if not items:
        return None
    snip = items[0]['snippet']
    tags = snip.get('tags', [])
    return {
        'title': snip.get('title'),
        'description': snip.get('description'),
        'tags': tags,
        'thumbnails': snip.get('thumbnails', {})
    }
