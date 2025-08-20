# # 🪖 Soldiers Management System
## מערכת ניהול חיילים פשוטה ויעילה

### 📋 תיאור
מערכת CRUD פשוטה לניהול חיילים עם MongoDB
- שם פרטי, שם משפחה, מספר טלפון, דרגה
- DAL גנרי פשוט וקל לשימוש
- REST API מלא

### 🚀 התחלה מהירה

#### 1. התקנת תלויות
```bash
pip install -r requirements.txt
```

#### 2. הרצת MongoDB
וודא שמונגו DB פועל על:
```
localhost:27017
```

#### 3. הרצת דוגמה
```bash
python example.py
```

#### 4. הרצת השרת
```bash
python services/api.py
```

### 🛠️ API Endpoints

| Method | URL | תיאור |
|--------|-----|-------|
| `POST` | `/soldiers` | יצירת חייל חדש |
| `GET` | `/soldiers` | קבלת כל החיילים |
| `GET` | `/soldiers/{id}` | קבלת חייל לפי מזהה |
| `PUT` | `/soldiers/{id}` | עדכון חייל |
| `DELETE` | `/soldiers/{id}` | מחיקת חייל |
| `GET` | `/soldiers/search?name={name}` | חיפוש לפי שם |
| `GET` | `/soldiers/rank/{rank}` | קבלת חיילים לפי דרגה |
| `GET` | `/soldiers/stats` | סטטיסטיקות |

### 📝 דוגמת שימוש

#### יצירת חייל חדש:
```bash
curl -X POST http://localhost:5000/soldiers \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "ישראל",
    "last_name": "כהן", 
    "phone_number": "050-1234567",
    "rank": "רב-טוראי"
  }'
```

#### קבלת כל החיילים:
```bash
curl http://localhost:5000/soldiers
```

#### חיפוש לפי שם:
```bash
curl http://localhost:5000/soldiers/search?name=ישראל
```

### 📁 מבנה הפרוייקט
```
services/
├── solider_entity.py    # Entity של חייל
├── dal.py              # Data Access Layer  
├── connection_dal.py   # חיבור למסד נתונים
├── config.py          # הגדרות
└── api.py             # REST API
```

### ⚙️ הגדרות

ניתן לשנות את הגדרות המסד נתונים ב-`services/config.py`:
```python
MONGODB_HOST = "mongodb://localhost"
MONGODB_PORT = 27017
MONGODB_DATABASE = "restdb"
MONGODB_COLLECTION = "soldiers"
```

### 🎯 פיצ'רים
- ✅ CRUD מלא
- ✅ חיפוש לפי שם
- ✅ סינון לפי דרגה
- ✅ סטטיסטיקות
- ✅ טיפול בשגיאות
- ✅ API פשוט ונקי

---
**פותח בפשטות ובמקצועיות** 🚀
# This project provides a RESTful API for CRUD operations on MongoDB documents.