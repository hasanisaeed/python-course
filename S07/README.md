> جلسه هفتم


## نصب برنامه

1. برای اجرا این کد من از پایتون ۳.۱۰ استفاده میکنم.
2. باید `ffmpeg` رو نصب داشته باشین
    - توی لینوکس که براحتی میتونین با یه سرچ ساده نصب  کنین
    - برای نصب توی محیط ویندوز هم این [لینک ](https://phoenixnap.com/kb/ffmpeg-windows)رو ببینین
3. فولدر جلسه ۷ام رو به لیتاب خودتون ببرین و بعد پکیجها رو توی این فولدر با دستور زیر نصب کنین
```
pip install -r requirements.txt
```
4. این فایل [onnx](https://drive.google.com/file/d/1eu60OrRtn4WhKrzM4mQv4F3rIuyUXqfl/view?usp=drive_link) رو دانلود کنین و کنار فایل `run.py` بذارین.
5. برای اجرای برنامه هم به راحتی در فولدری که فایل `run.py` قرار داره، دستور زیر رو بزنین
   
   `python3 run.py`

## Credits

- [roop](https://github.com/s0md3v/roop/): as main repo
- [ffmpeg](https://ffmpeg.org/): for making video related operations easy
- [deepinsight](https://github.com/deepinsight): for their [insightface](https://github.com/deepinsight/insightface) project which provided a well-made library and models.
