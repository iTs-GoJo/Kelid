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

```bash
kelid encode script.py -o locked.txt
kelid encode script.py
kelid run "cHJpbnQoJ1NhbGFtIGRvY3QhJyk="
```

### استفاده در پایتون

```python
from kelid import encode, run

code = '''
def greet():
    print("سلام داداش، این یه تست Kelid هست!")

greet()
'''

encoded = encode(code)
print("Encoded:", encoded)
run(encoded)
```

---

### 📸 نمونه اسکرین‌شات‌ها

<div align="center">
  <img src="https://raw.githubusercontent.com/iTs-GoJo/Kelid/main/images/img1.jpg" alt="Screenshot 1" style="width: 25%; height: auto; margin: 5px; border-radius: 9px;">
  <img src="https://raw.githubusercontent.com/iTs-GoJo/Kelid/main/images/img2.jpg" alt="Screenshot 2" style="width: 25%; height: auto; margin: 5px; border-radius: 9px;">
</div>

---

## ⚠️ هشدار امنیتی

- این روش امنیت بالا ندارد و فقط برای جلوگیری از مشاهده مستقیم کد است.
- برای امنیت بیشتر از [PyArmor](https://github.com/dashingsoft/pyarmor) استفاده کنید.

---

## 🧑‍💻 نویسنده

- **Ali Jafari**  
- ایمیل: thealiapi@gmail.com  
- گیت‌هاب: [iTs-GoJo](https://github.com/iTs-GoJo)

---

## 🪪 لایسنس

تحت مجوز [MIT](LICENSE) منتشر شده است.
