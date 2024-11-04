import tkinter as tk
from tkinter import scrolledtext, messagebox
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript():
    video_url = url_entry.get()
    try:
        # استخراج معرف الفيديو من رابط اليوتيوب
        video_id = video_url.split("v=")[-1]
        
        # جلب النصوص الخاصة بالفيديو
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ar', 'en'])
        
        # مسح النصوص السابقة من المربع
        text_area.delete(1.0, tk.END)
        
        # عرض النصوص في مربع النصوص
        for item in transcript:
            text_area.insert(tk.END, f"{item['text']} (Time: {item['start']}s)\n")
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve transcript: {e}")

def copy_text():
    # نسخ محتوى مربع النص إلى الحافظة
    window.clipboard_clear()
    window.clipboard_append(text_area.get(1.0, tk.END))
    messagebox.showinfo("Copy Text", "Transcript copied to clipboard!")

def paste_text():
    # لصق النص من الحافظة إلى حقل الإدخال
    url_entry.delete(0, tk.END)  # مسح النص الحالي
    url_entry.insert(tk.END, window.clipboard_get())

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("YouTube Video Transcript")
window.geometry("600x450")
window.configure(bg="#2e2e2e")  # تغيير خلفية التطبيق إلى الأسود الداكن

# إعدادات الألوان
label_fg = "#ffffff"  # لون النص الأبيض
entry_bg = "#404040"  # خلفية المدخلات
entry_fg = "#ffffff"  # لون النص في المدخلات
button_bg = "#1e90ff"  # خلفية زر النص
button_fg = "#ffffff"  # لون نص الزر
text_bg = "#2e2e2e"  # خلفية مربع النص
text_fg = "#ffffff"  # لون النص داخل مربع النص

# إدخال رابط الفيديو
url_label = tk.Label(window, text="Enter YouTube Video URL:", fg=label_fg, bg=window['bg'], font=("Arial", 12, "bold"))
url_label.pack(pady=5)

# إطار لحقل الإدخال وزر اللصق ليكونا بجانب بعضهما البعض
url_frame = tk.Frame(window, bg=window['bg'])
url_frame.pack(pady=5)

url_entry = tk.Entry(url_frame, width=40, bg=entry_bg, fg=entry_fg, font=("Arial", 10))
url_entry.pack(side=tk.LEFT, padx=(0, 5))

paste_button = tk.Button(url_frame, text="Paste", command=paste_text, bg=button_bg, fg=button_fg, font=("Arial", 10), relief="solid")
paste_button.pack(side=tk.LEFT)

# زر للحصول على النصوص
transcript_button = tk.Button(window, text="Get Transcript", command=get_transcript, bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"), relief="solid")
transcript_button.pack(pady=10)

# زر لنسخ النصوص
copy_button = tk.Button(window, text="Copy Transcript", command=copy_text, bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"), relief="solid")
copy_button.pack(pady=10)

# مربع النصوص للعرض
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15, bg=text_bg, fg=text_fg, font=("Arial", 10))
text_area.pack(pady=10)

# بدء التطبيق
window.mainloop()
