<div align="center">
  <h3>🔐 Kelid - Simple Python Code Encoder & Runner</h3>
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/iTs-GoJo/Kelid/main/logo.png" alt="Kelid Logo" width="150">
</p>

![GitHub stars](https://img.shields.io/github/stars/iTs-GoJo/Kelid?style=social)
![GitHub forks](https://img.shields.io/github/forks/iTs-GoJo/Kelid?style=social)
![GitHub release](https://img.shields.io/github/v/release/iTs-GoJo/Kelid)
![Commit Activity](https://img.shields.io/github/commit-activity/m/iTs-GoJo/Kelid)
[![GitHub contributors](https://img.shields.io/github/contributors/iTs-GoJo/Kelid)](https://github.com/iTs-GoJo/Kelid/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/iTs-GoJo/Kelid)](https://github.com/iTs-GoJo/Kelid/commits/)

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

کلید تحت لایسنس[MIT](LICENSE) منتشر شده است.