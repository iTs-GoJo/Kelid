<div align="center">
  <h3>🔐 Kelid - Simple Python Code Encoder & Runner</h3>
</div>

<p align="center">
  <img src="https://uploadkon.ir/uploads/a2af09_25file-000000009ac0620a95ec4a89feb80a83.png" alt="Kelid Logo" width="150">
</p>

![GitHub stars](https://img.shields.io/github/stars/iTs-GoJo/Kelid?style=social)
![GitHub forks](https://img.shields.io/github/forks/iTs-GoJo/Kelid?style=social)
![GitHub release](https://img.shields.io/github/v/release/iTs-GoJo/Kelid)
![Commit Activity](https://img.shields.io/github/commit-activity/m/iTs-GoJo/Kelid)
[![GitHub contributors](https://img.shields.io/github/contributors/iTs-GoJo/Kelid)](https://github.com/iTs-GoJo/Kelid/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/iTs-GoJo/Kelid)](https://github.com/iTs-GoJo/Kelid/commits/)

---

## ⚙️ Install

```bash
pip install kelid
```

---

## 🚀 Use samples

### Use Terminal (CLI)

- Encrypting a Python file and saving output in the file:

```bash
kelid encode script.py -o locked.txt
```

- Encrypting a Python file and output printing in terminal:

```bash
kelid encode script.py
```

- Run the encrypted string (Base64) in Terminal:

```bash
kelid run "cHJpbnQoJ1NhbGFtIGRvY3QhJyk="
```

---

### Use in Python file:

#### Encryption and execute the code as dynamic

```python
from kelid import encode, run

code = '''
def greet():
    print("This test is the kelid ")

greet()
'''

encoded = encode(code)
print("encoded code:")
print(encoded)

print("\nRun the encrypted code:")
run(encoded)
```

#### Encrypted and saved the encrypted file, then run it

```python
from kelid import encode, run

with open("script.py", "r", encoding="utf-8") as f:
    source_code = f.read()

encoded_code = encode(source_code)

with open("locked_code.txt", "w", encoding="utf-8") as f:
    f.write(encoded_code)


with open("locked_code.txt", "r", encoding="utf-8") as f:
    locked_code = f.read()

run(locked_code)
```

---

## ❗ Security Alert 

 This method is only used to prevent the source from seeing the source and not high security.   - Professionals can easily restore encrypted code.   - For real protection, use more advanced tools such as [Pyarmor](https://github.com/dashingsoft/pyarmor) .

---

## 🧑‍💻 Author

- **Ali Jafari**  
- Email: thealiapi@gmail.com  
- GitHub: [iTs-GoJo](https://github.com/iTs-GoJo)

---

##🪪LICENSE 

Key is released under the [MIT](LICENSE) license.