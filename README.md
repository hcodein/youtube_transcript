يمكنك جلب اي transcript لاي فيديو توريد ![Screenshot](https://github.com/user-attachments/assets/5bac6ccb-59d1-4b21-9d0d-ae6fae6eef90)


You can import any transcript of any video.

# YouTube Video Transcript

This program retrieves transcripts from YouTube videos using the `YouTubeTranscriptApi` library and displays the transcripts in a graphical user interface with `tkinter`.

## Requirements

1. Python 3.6 or higher.
2. The `youtube-transcript-api` library for fetching transcripts.
3. The `tkinter` library, which is included with Python (no additional installation required).

## Installation

To install the required library, run the following command:

```bash
pip install youtube-transcript-api


### Instructions as Comments within the Code

```python
"""
YouTube Video Transcript

This program retrieves transcripts from YouTube videos using the `YouTubeTranscriptApi` library and displays 
the transcripts in a graphical user interface with `tkinter`.

Requirements:
1. Python 3.6 or higher.
2. The `youtube-transcript-api` library for fetching transcripts.
3. The `tkinter` library, which is included with Python (no additional installation required).

Installation:
To install the required library, run the following command:

    pip install youtube-transcript-api

Usage:
1. Run the program.
2. Enter the YouTube video URL in the input field.
3. Click the "Get Transcript" button to retrieve the video's transcript.
4. The transcript will be displayed in the text area.
5. You can copy the transcript by clicking the "Copy Transcript" button.
6. If you have a video URL copied to your clipboard, you can paste it into the input field by clicking the "Paste" button.

Notes:
- The program supports fetching transcripts in two languages: Arabic and English. 
  If the transcript is not available for the video, an error may occur.
- Ensure you are connected to the internet, as the program requires access to YouTube to fetch transcripts.
"""
# YouTube Video Transcript

برنامج للحصول على النصوص التوضيحية من مقاطع فيديو YouTube باستخدام مكتبة `YouTubeTranscriptApi`، وعرض النصوص داخل واجهة باستخدام `tkinter`.

## المتطلبات

1. Python 3.6 أو أحدث.
2. مكتبة `youtube-transcript-api` لجلب النصوص التوضيحية.
3. مكتبة `tkinter` مضمنة في Python (لا تحتاج إلى تثبيت إضافي).

## كيفية التثبيت

لتثبيت المكتبة المطلوبة، قم بتشغيل الأمر التالي:

```bash
pip install youtube-transcript-api


### التعليمات كتعليقات داخل الكود

```python
"""
YouTube Video Transcript

برنامج للحصول على النصوص التوضيحية من مقاطع فيديو YouTube باستخدام مكتبة `YouTubeTranscriptApi`، 
وعرض النصوص داخل واجهة باستخدام `tkinter`.

المتطلبات:
1. Python 3.6 أو أحدث.
2. مكتبة `youtube-transcript-api` لجلب النصوص التوضيحية.
3. مكتبة `tkinter` مضمنة في Python (لا تحتاج إلى تثبيت إضافي).

كيفية التثبيت:
لتثبيت المكتبة المطلوبة، قم بتشغيل الأمر التالي:

    pip install youtube-transcript-api

كيفية الاستخدام:
1. شغل البرنامج.
2. أدخل رابط فيديو YouTube في حقل الإدخال.
3. اضغط على زر "Get Transcript" للحصول على النصوص التوضيحية للفيديو.
4. سيتم عرض النصوص التوضيحية في مربع النص.
5. يمكنك نسخ النصوص بالنقر على زر "Copy Transcript".
6. إذا كان لديك رابط فيديو منسوخ في الحافظة، يمكنك لصقه في حقل الإدخال بالنقر على زر "Paste".

ملاحظات:
- البرنامج يدعم جلب النصوص التوضيحية بلغتين: العربية والإنجليزية. 
  إذا لم تتوفر الترجمة في الفيديو، قد يظهر خطأ.
- تأكد من أنك متصل بالإنترنت لأن البرنامج يحتاج للاتصال بـ YouTube لجلب النصوص التوضيحية.
"""

