# 🔐 Kelid

**Kelid** (کلید) یک لایبرری ساده و سبک برای رمزگذاری و اجرای کدهای پایتون با استفاده از `marshal` و `base64` است.  
این ابزار بهت کمک می‌کنه کدهای پایتونت رو به صورت رشته‌ای امن‌تر (اما نه خیلی قوی) کدگذاری و اجرا کنی.

---

## ⚙️ نصب

```bash
pip install kelid
```

---

## 🚀 نمونه‌های استفاده

### استفاده ترمینالی (CLI)

- رمزگذاری یک فایل پایتون و ذخیره خروجی در فایل:

```bash
kelid encode script.py -o locked.txt
```

- رمزگذاری یک فایل پایتون و چاپ خروجی در ترمینال:

```bash
kelid encode script.py
```

- اجرای رشته رمزگذاری شده (base64) در ترمینال:

```bash
kelid run "cHJpbnQoJ1NhbGFtIGRvY3QhJyk="
```

---

### استفاده در فایل پایتون

#### رمزگذاری و اجرای کد به صورت داینامیک

```python
from kelid import encode, run

code = '''
def greet():
    print("سلام داداش، این یه تست Kelid هست!")

greet()
'''

encoded = encode(code)
print("کد رمزگذاری شده:")
print(encoded)

print("\nاجرای کد رمزگذاری شده:")
run(encoded)
```

#### رمزگذاری و ذخیره فایل رمز شده، سپس اجرای آن

```python
from kelid import encode, run

# خواندن کد از فایل و رمزگذاری
with open("script.py", "r", encoding="utf-8") as f:
    source_code = f.read()

encoded_code = encode(source_code)

# ذخیره کد رمز شده در فایل
with open("locked_code.txt", "w", encoding="utf-8") as f:
    f.write(encoded_code)

# خواندن و اجرای کد رمز شده از فایل
with open("locked_code.txt", "r", encoding="utf-8") as f:
    locked_code = f.read()

run(locked_code)
```

---

## ⚠️ هشدار امنیتی

- این روش فقط برای جلوگیری از دیدن مستقیم سورس‌کد استفاده می‌شود و امنیت بالایی ندارد.  
- افراد حرفه‌ای می‌توانند به راحتی کد رمز شده را بازگردانی کنند.  
- برای محافظت واقعی، از ابزارهای پیشرفته‌تری مثل [PyArmor](https://github.com/dashingsoft/pyarmor) استفاده کنید.

---

## 🧑‍💻 نویسنده

- **Ali Jafari**  
- ایمیل: thealiapi@gmail.com  
- گیت‌هاب: [iTs-GoJo](https://github.com/iTs-GoJo)

---

## 🪪 لایسنس

این پروژه تحت مجوز [MIT](LICENSE) منتشر شده است.  
می‌توانید آزادانه استفاده و تغییر دهید. ✌️