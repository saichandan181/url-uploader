class Translation(object):
    START_TEXT = """Hi {} 👋

I'm All Saver Bot Developed By Chandan🚀 

<b>Permanent Thumbnail Support💯.</b>

<b>🔘 IF You like My Work Buy Me a Coffee :</b> <a href="https://www.buymeacoffee.com/saichandan">Click Here</a>
<i>Send me a direct link and I will upload it to telegram as a file/video.</i>

Click /help for more details...."""
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! 🤩
    
Example: <a href='https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg'>See This!</a> 👇"""

    INCORRECT_REQUEST = """Please make sure you submit your request correctly."""
    WAIT_PROCESS_FINISH = """Please wait for your current file to finish downloading before sending more links!

Or use /cancel to terminate incomplete processes."""
    PROCESS_CANCELLED = """File upload cancelled
You can now send a new URL."""
    NO_PROCESS_FOUND = """🤷‍♂️ No pending uploads were found. You can upload files by sending a link now!

/help for more details."""
    FORMAT_SELECTION = "👇𝗦𝗲𝗹𝗲𝗰𝘁 𝗔𝗻𝗱 𝗖𝗵𝗼𝘀𝗲 𝗬𝗼𝘂𝗿 𝗙𝗼𝗿𝗺𝗮𝘁👇"
    SET_CUSTOM_USERNAME_PASSWORD = """\n👮‍♂ Powered By :</b>@chandan_bots """
    DOWNLOAD_START = "📥 DOWNLOADING..."
    UPLOAD_START = "📤 UPLOADING..."
    RCHD_TG_API_LIMIT = "<b>Downloaded in:</b> {} seconds.\n<b>Detected file size:</b> {}.\n\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations 😕."
    #AFTER_SUCCESSFUL_UPLOAD_MSG = "𝘛𝘏𝘈𝘕𝘒𝘚 𝘍𝘖𝘙 𝘜𝘚𝘐𝘕𝘎 𝘔𝘌 🥰"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "𝘛𝘏𝘈𝘕𝘒𝘚 𝘍𝘖𝘙 𝘜𝘚𝘐𝘕𝘎 𝘔𝘌 🥰\n\n@chandan_bots"

    SAVED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail ✅."
    DEL_ETED_CUSTOM_THUMB_NAIL = " Delete Your Thumbnail ✅."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = """<b>I think you have entered an unaccessible url or a private url.</b>
<i>Go check if you can access the content in the url from your browser first!</i>

<b>YouTubeDL</b> said: {}"""
    HELP_USER = """<b>How to Use Me?</b> 🤔

1. Send your URL link

2. Send thumbnail photo to save it permanently.

3. Select the desired option

4. Send /delthumbnail To Delete Your Thumbnail.

5.  Use /caption to Set caption as Reply to Media

6. Use this /about and /viewthumbnail
"""
    ABOUT_TEXT = """<b>🔘 My Name :</b> URL Uploader Bot V2 🚀

<b>🔘 Channel :</b> <a href="https://t.me/chandan_bots">NT BOT</a>

<b>🔘 Source :</b> <a href="https://github.com/saichandan181/url-uploader.git">Click Here</a>

<b>🔘 Buy Me a Coffee :</b> <a href="https://www.buymeacoffee.com/saichandan">Click Here</a>

<b>🔘 Language :</b> <a href="https://www.python.org/">Python 3.10.7</a>

<b>🔘 Framework :</b> <a href="https://docs.pyrogram.org/">Pyrogram 1.4.16</a>

<b>🔘 Creater :</b> @chandan_bots"""

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail."
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled ❌"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."


