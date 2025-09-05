# ⏳ PomodoroApp — Jamshidbek Isroilov tomonidan

Bu oddiy, intuitiv Pomodoro taymer ilovasi bo‘lib, foydalanuvchiga vazifalarni bo‘lib bajarish va diqqatni jamlashda yordam beradi. Ilova Python va Tkinter yordamida yaratilgan.

---

## 📦 Loyiha tarkibi

PomodoroApp/ 
│── pomodoro_single.py # Barcha kod bitta faylda 
│── dist/ │ 
          └── PomodoroApp.exe # Tayyor Windows ilovasi (.exe) │
 ── README.md # Loyihani tushuntiruvchi hujjat
 
---

## ⚙️ Asosiy funksiyalar

- 25 daqiqalik ish sessiyasi + 5 daqiqalik dam olish
- Har bir sessiyadan so‘ng signal (beep)
- Tasklar ro‘yxatini boshqarish
- Har bir vazifaga pomidorka belgisi qo‘shiladi
- GUI interfeys: pastel ranglar, tugmalar, yordam matni

---

## 🚀 Ishga tushirish

### 1. `.exe` fayl orqali (Windows foydalanuvchilari uchun)

`dist/PomodoroApp.exe` faylini ishga tushiring — hech qanday o‘rnatish talab qilinmaydi.

> ⚠️ Agar antivirus ogohlantirsa, bu PyInstaller orqali yaratilgan `.exe` fayl ekanligini tushuntiring.

### 2. Python orqali

Agar sizda Python o‘rnatilgan bo‘lsa:


python pomodoro_single.py
📁 dist papkasi haqida
Ushbu repozitoriyda dist/ papkasi mavjud bo‘lib, unda PyInstaller yordamida yaratilgan .exe fayl joylashgan. Bu sizga ilovani to‘g‘ridan-to‘g‘ri yuklab olib ishlatish imkonini beradi, Python o‘rnatilmagan bo‘lsa ham.

📘 Foydalanish tartibi
"Add Task" tugmasi orqali vazifa qo‘shing

"Start" tugmasi bilan Pomodoro sessiyasini boshlang

Har bir sessiyadan so‘ng dam oling va taskga pomidorka qo‘shiladi

Tasklar ro‘yxatini kuzatib boring

👨‍💻 Muallif
Jamshidbek Isroilov 📬 Telegram

📌 Loyiha maqsadi
Bu ilova Pomodoro metodologiyasini oddiy va qulay tarzda taqdim etadi. Diqqatni jamlash, samarali ishlash va progressni kuzatish uchun mo‘ljallangan.