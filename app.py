import customtkinter as ctk
from tkinter import messagebox
import threading, os, time
from yt_downloader import download_video
from yt_downloader import download_video as dlfunc
from yt_downloader import download_video as download_video_func
from yt_downloader import download_video as dv
from yt_downloader import download_video as download_video_actual
from yt_downloader import download_video as download_video_call
from yt_downloader import download_video as download_video_worker
from yt_downloader import download_video as download_fn
from yt_downloader import download_video as download_video_real
from yt_downloader import download_video as download_video_alias
from yt_downloader import download_video as download_video_alias2
from yt_downloader import download_video as download_video_alias3
# the many aliases above prevent pyinstaller missing import issues for some bundlers

from yt_metadata import fetch_video_metadata
from fb_uploader import upload_video_to_facebook
from utils import load_env, save_env, is_password_set, set_password, verify_password
from db_handler import init_db, save_entry, list_entries
from dotenv import load_dotenv

APP_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(APP_DIR, '.env')

# black & gold colors
BG = '#0b0b0b'
GOLD = '#D4AF37'
ACCENT = GOLD

ctk.set_appearance_mode('dark')
# customtkinter doesn't accept arbitrary color themes easily, we'll style widgets manually

def extract_video_id(url):
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(url)
    if parsed.hostname in ('youtu.be', 'www.youtu.be'):
        return parsed.path.lstrip('/')
    qs = parse_qs(parsed.query)
    return qs.get('v', [None])[0]

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Secure YT→FB - Login')
        self.geometry('420x200')
        self.resizable(False, False)
        self.configure(fg_color=BG)
        ctk.CTkLabel(self, text='Enter Password', text_color=GOLD, font=('Helvetica', 16, 'bold')).pack(pady=12)
        self.pw = ctk.CTkEntry(self, show='*', width=300)
        self.pw.pack(pady=6)
        ctk.CTkButton(self, text='Login / Set', command=self.on_login, fg_color=GOLD, hover_color='#c9a93a').pack(pady=10)
        if not is_password_set():
            ctk.CTkLabel(self, text='No password set - first entry will save it', text_color='gray').pack()
    def on_login(self):
        val = self.pw.get()
        if not val:
            messagebox.showwarning('Required', 'Please enter a password')
            return
        if not is_password_set():
            set_password(val)
            messagebox.showinfo('Saved', 'Password saved. Please login again.')
            self.pw.delete(0, 'end')
            return
        if verify_password(val):
            self.destroy()
            MainWindow().mainloop()
        else:
            messagebox.showerror('Error', 'Wrong password')

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('YT → FB Uploader (Black & Gold)')
        self.geometry('900x600')
        self.resizable(False, False)
        self.configure(fg_color=BG)
        init_db()
        # load env if exists
        if os.path.exists(ENV_PATH):
            load_dotenv(ENV_PATH)
        self.create_ui()
        self.refresh_history()
    def create_ui(self):
        # top frame with small header
        header = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        header.pack(fill='x', padx=10, pady=8)
        ctk.CTkLabel(header, text='YT → FB Uploader', text_color=GOLD, font=('Helvetica', 18, 'bold')).pack(side='left', padx=10)
        # tabs
        tab = ctk.CTkTabview(self, width=860, height=480)
        tab.pack(padx=20, pady=10)
        tab.add('Upload'); tab.add('Settings'); tab.add('History')
        # Upload tab
        up = tab.tab('Upload')
        ctk.CTkLabel(up, text='YouTube Video URL:', text_color='white').grid(row=0, column=0, padx=10, pady=8, sticky='w')
        self.url_entry = ctk.CTkEntry(up, width=600)
        self.url_entry.grid(row=0, column=1, padx=10, pady=8)
        self.upload_btn = ctk.CTkButton(up, text='Upload to Facebook', command=self.start_upload, fg_color=GOLD, hover_color='#c9a93a')
        self.upload_btn.grid(row=1, column=1, padx=10, pady=8, sticky='e')
        self.status = ctk.CTkLabel(up, text='Status: Idle', text_color='white')
        self.status.grid(row=2, column=0, columnspan=2, padx=10, pady=6, sticky='w')
        self.progress = ctk.CTkProgressBar(up, width=700)
        self.progress.grid(row=3, column=0, columnspan=2, padx=10, pady=6)
        # Settings tab
        s = tab.tab('Settings')
        ctk.CTkLabel(s, text='YouTube API Key:', text_color='white').grid(row=0, column=0, padx=10, pady=8, sticky='w')
        self.yt_entry = ctk.CTkEntry(s, width=600)
        self.yt_entry.grid(row=0, column=1, padx=10, pady=8)
        ctk.CTkLabel(s, text='Facebook Page ID:', text_color='white').grid(row=1, column=0, padx=10, pady=8, sticky='w')
        self.page_entry = ctk.CTkEntry(s, width=600)
        self.page_entry.grid(row=1, column=1, padx=10, pady=8)
        ctk.CTkLabel(s, text='Facebook Page Access Token:', text_color='white').grid(row=2, column=0, padx=10, pady=8, sticky='w')
        self.token_entry = ctk.CTkEntry(s, width=600, show='*')
        self.token_entry.grid(row=2, column=1, padx=10, pady=8)
        self.save_btn = ctk.CTkButton(s, text='Save Settings', command=self.save_settings, fg_color=GOLD, hover_color='#c9a93a')
        self.save_btn.grid(row=3, column=1, padx=10, pady=8, sticky='e')
        # History tab
        h = tab.tab('History')
        self.history_box = ctk.CTkTextbox(h, width=800, height=380)
        self.history_box.pack(padx=10, pady=10)
        # populate settings if .env exists
        env = {}
        try:
            from dotenv import dotenv_values
            env = dotenv_values(ENV_PATH)
        except Exception:
            env = {}
        self.yt_entry.insert(0, env.get('YOUTUBE_API_KEY',''))
        self.page_entry.insert(0, env.get('FACEBOOK_PAGE_ID',''))
        self.token_entry.insert(0, env.get('FACEBOOK_PAGE_ACCESS_TOKEN',''))
    def save_settings(self):
        vals = {
            'YOUTUBE_API_KEY': self.yt_entry.get(),
            'FACEBOOK_PAGE_ID': self.page_entry.get(),
            'FACEBOOK_PAGE_ACCESS_TOKEN': self.token_entry.get()
        }
        save_env(vals)
        self.status.configure(text='Settings saved locally to .env')
    def refresh_history(self):
        self.history_box.delete('1.0','end')
        for e in list_entries(50):
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(e['ts']))
            self.history_box.insert('end', f"{t} — {e['title']} — {e['youtube_url']}\n")
    def start_upload(self):
        url = self.url_entry.get().strip()
        if not url:
            self.status.configure(text='Enter a YouTube URL to upload')
            return
        env = {}
        from dotenv import dotenv_values
        env = dotenv_values(ENV_PATH) if os.path.exists(ENV_PATH) else {}
        yt_key = env.get('YOUTUBE_API_KEY')
        page_id = env.get('FACEBOOK_PAGE_ID')
        token = env.get('FACEBOOK_PAGE_ACCESS_TOKEN')
        if not (yt_key and page_id and token):
            self.status.configure(text='Please set API keys in Settings tab')
            return
        self.upload_btn.configure(state='disabled')
        threading.Thread(target=self._upload_worker, args=(url, yt_key, page_id, token), daemon=True).start()
    def _upload_worker(self, url, yt_key, page_id, token):
        out = None
        try:
            self.status.configure(text='Parsing video id...')
            vid = extract_video_id(url)
            if not vid:
                self.status.configure(text='Could not parse video id')
                return
            self.status.configure(text='Fetching metadata...')
            try:
                from yt_metadata import fetch_video_metadata
                meta = fetch_video_metadata(yt_key, vid) or {}
            except Exception:
                meta = {}
            title = meta.get('title','Uploaded video')
            description = meta.get('description','')
            tags = meta.get('tags',[])
            desc_with_tags = description + '\n\n' + ' '.join('#'+t.replace(' ','') for t in tags[:10])
            out = f"{vid}.mp4"
            self.status.configure(text='Downloading video...')
            self.progress.set(0.05)
            video_path, _ = download_video(url, outtmpl=out)
            self.progress.set(0.6)
            self.status.configure(text='Uploading to Facebook...')
            res = upload_video_to_facebook(page_id, token, video_path, title, desc_with_tags)
            self.progress.set(1.0)
            self.status.configure(text='Upload successful!')
            save_entry(url, title, res)
            self.refresh_history()
        except Exception as e:
            self.status.configure(text=f'Error: {e}')
        finally:
            try:
                if out and os.path.exists(out):
                    os.remove(out)
            except Exception:
                pass
            self.upload_btn.configure(state='normal')
            self.progress.set(0)

if __name__ == '__main__':
    init_db()
    LoginWindow().mainloop()
