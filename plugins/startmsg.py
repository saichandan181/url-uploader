class Translation(object):
    START_TEXT = """Hi {} ๐

I'm All Saver Bot Developed By Chandan๐ 

<i>Send me a direct link and I will upload it to telegram as a file/video.</i>

<b>Permanent Thumbnail Support๐ฏ.</b>

Click /help for more details...."""
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! ๐คฉ
    
Example: <a href='https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg'>See This!</a> ๐"""
 

    INCORRECT_REQUEST = """Please make sure you submit your request correctly."""
    WAIT_PROCESS_FINISH = """Please wait for your current file to finish downloading before sending more links!

Or use /cancel to terminate incomplete processes."""
    PROCESS_CANCELLED = """File upload cancelled
You can now send a new URL."""
    NO_PROCESS_FOUND = """๐คทโโ๏ธ No pending uploads were found. You can upload files by sending a link now!

/help for more details."""
    FORMAT_SELECTION = "๐๐ฆ๐ฒ๐น๐ฒ๐ฐ๐ ๐๐ป๐ฑ ๐๐ต๐ผ๐๐ฒ ๐ฌ๐ผ๐๐ฟ ๐๐ผ๐ฟ๐บ๐ฎ๐๐"
    SET_CUSTOM_USERNAME_PASSWORD = """\n๐ฎโโ Powered By :</b>@chandan_bots """
    DOWNLOAD_START = "๐ฅ DOWNLOADING..."
    UPLOAD_START = "๐ค UPLOADING..."
    RCHD_TG_API_LIMIT = "<b>Downloaded in:</b> {} seconds.\n<b>Detected file size:</b> {}.\n\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations ๐."
    #AFTER_SUCCESSFUL_UPLOAD_MSG = "๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐ ๐ฅฐ"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐ ๐ฅฐ\n\n@chandan_bots"

    SAVED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail โ."
    DEL_ETED_CUSTOM_THUMB_NAIL = " Delete Your Thumbnail โ."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = """<b>I think you have entered an unaccessible url or a private url.</b>
<i>Go check if you can access the content in the url from your browser first!</i>

<b>YouTubeDL</b> said: {}"""
    HELP_USER = """<b>How to Use Me?</b> ๐ค

1. Send your URL link

2. Send thumbnail photo to save it permanently.

3. Select the desired option

4. Send /delthumbnail To Delete Your Thumbnail.

5.  Use /caption to Set caption as Reply to Media

6. Use this /about and /viewthumbnail
"""
    ABOUT_TEXT = """<b>๐ My Name :</b> URL Uploader Bot V2 ๐

<b>๐ Channel :</b> <a href="https://t.me/chandan_bots">NT BOT</a>

<b>๐ Source :</b> <a href="https://github.com/saichandan181/url-uploader.git">Click Here</a>

<b>๐ Buy Me a Coffee :</b> <a href="https://www.buymeacoffee.com/saichandan">Click Here</a>

<b>๐ Language :</b> <a href="https://www.python.org/">Python 3.10.7</a>

<b>๐ Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 1.4.16</a>

<b>๐ Creater :</b> @chandan_bots"""

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail."
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled โ"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."


