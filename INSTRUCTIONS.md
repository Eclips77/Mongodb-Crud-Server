# 🚀 הוראות הרצה מהירות

## קודם כל - וודא שמונגו DB פועל!

### אופציה 1: הרצה אוטומטית (Windows)
```bash
.\run.bat
```

### אופציה 2: הרצה צעד אחר צעד

#### 1. התקנת תלויות
```bash
pip install -r requirements.txt
```

#### 2. בדיקת חיבור למונגו
```bash
python test_connection.py
```

#### 3. הרצת דוגמה
```bash
python example.py
```

#### 4. הרצת השרת
```bash
python services/api.py
```

#### 5. בדיקת API (בטרמינל נפרד)
```bash
python test_api.py
```

## 🧪 בדיקות מהירות עם curl

### יצירת חייל:
```bash
curl -X POST http://localhost:5000/soldiers -H "Content-Type: application/json" -d "{\"first_name\":\"ישראל\",\"last_name\":\"כהן\",\"phone_number\":\"050-1234567\",\"rank\":\"רב-טוראי\"}"
```

### קבלת כל החיילים:
```bash
curl http://localhost:5000/soldiers
```

### בדיקת תקינות:
```bash
curl http://localhost:5000/health
```

## 📁 מה יש לנו:

### Core Files:
- `services/solider_entity.py` - Entity של חייל ✅
- `services/dal.py` - DAL גנרי מלא ✅  
- `services/connection_dal.py` - ניהול חיבור ✅
- `services/api.py` - REST API מלא ✅
- `services/config.py` - הגדרות ✅

### Helper Files:
- `example.py` - דוגמה מלאה לשימוש ✅
- `test_connection.py` - בדיקת חיבור מהירה ✅
- `test_api.py` - בדיקת API ✅
- `run.bat` - הרצה אוטומטית ✅
- `requirements.txt` - תלויות ✅

## 🎯 מה המערכת יודעת לעשות:

### CRUD מלא:
- ✅ Create - יצירת חיילים
- ✅ Read - קריאת חייל/חיילים
- ✅ Update - עדכון חיילים  
- ✅ Delete - מחיקת חיילים

### פיצ'רים נוספים:
- ✅ חיפוש לפי שם
- ✅ סינון לפי דרגה
- ✅ סטטיסטיקות
- ✅ טיפול בשגיאות
- ✅ API תיעוד

---
**הכל פשוט, נקי ועובד!** 🚀
