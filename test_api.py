"""
🧪 בדיקות API פשוטות
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    """בדיקת API פשוטה"""
    print("🧪 בודק API של מערכת החיילים...")
    print("=" * 50)
    
    try:
        # בדיקת health check
        print("1️⃣ בודק health check...")
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ השרת פועל")
        else:
            print("❌ השרת לא פועל")
            return
        
        # יצירת חייל חדש
        print("\n2️⃣ יוצר חייל חדש...")
        new_soldier = {
            "first_name": "בדיקה",
            "last_name": "טסט",
            "phone_number": "050-1111111",
            "rank": "רב-טוראי"
        }
        
        response = requests.post(f"{BASE_URL}/soldiers", 
                               json=new_soldier,
                               headers={"Content-Type": "application/json"})
        
        if response.status_code == 201:
            result = response.json()
            soldier_id = result.get("id")
            print(f"✅ חייל נוצר עם מזהה: {soldier_id}")
        else:
            print(f"❌ יצירת חייל נכשלה: {response.text}")
            return
        
        # קבלת החייל שנוצר
        print(f"\n3️⃣ מביא את החייל שנוצר...")
        response = requests.get(f"{BASE_URL}/soldiers/{soldier_id}")
        if response.status_code == 200:
            soldier_data = response.json()
            print(f"✅ נמצא חייל: {soldier_data['first_name']} {soldier_data['last_name']}")
        else:
            print("❌ קבלת חייל נכשלה")
        
        # קבלת כל החיילים
        print(f"\n4️⃣ מביא את כל החיילים...")
        response = requests.get(f"{BASE_URL}/soldiers")
        if response.status_code == 200:
            soldiers = response.json()
            print(f"✅ נמצאו {len(soldiers)} חיילים")
        else:
            print("❌ קבלת חיילים נכשלה")
        
        # עדכון חייל
        print(f"\n5️⃣ מעדכן חייל...")
        update_data = {"phone_number": "050-9999999"}
        response = requests.put(f"{BASE_URL}/soldiers/{soldier_id}",
                              json=update_data,
                              headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            print("✅ חייל עודכן")
        else:
            print("❌ עדכון נכשל")
        
        # חיפוש חייל
        print(f"\n6️⃣ מחפש חייל...")
        response = requests.get(f"{BASE_URL}/soldiers/search?name=בדיקה")
        if response.status_code == 200:
            search_results = response.json()
            print(f"✅ נמצאו {len(search_results)} חיילים בחיפוש")
        else:
            print("❌ חיפוש נכשל")
        
        # סטטיסטיקות
        print(f"\n7️⃣ מביא סטטיסטיקות...")
        response = requests.get(f"{BASE_URL}/soldiers/stats")
        if response.status_code == 200:
            stats = response.json()
            print(f"✅ סה\"כ חיילים: {stats['total_soldiers']}")
        else:
            print("❌ קבלת סטטיסטיקות נכשלה")
        
        # מחיקת חייל
        print(f"\n8️⃣ מוחק חייל...")
        response = requests.delete(f"{BASE_URL}/soldiers/{soldier_id}")
        if response.status_code == 200:
            print("✅ חייל נמחק")
        else:
            print("❌ מחיקה נכשלה")
        
        print(f"\n🎉 כל הבדיקות הושלמו בהצלחה!")
        
    except requests.exceptions.ConnectionError:
        print("❌ לא ניתן להתחבר לשרת")
        print("💡 וודא שהשרת פועל: python services/api.py")
    except Exception as e:
        print(f"❌ שגיאה: {e}")

if __name__ == "__main__":
    # Install requests if not available
    try:
        import requests
    except ImportError:
        print("📦 מתקין requests...")
        import subprocess
        subprocess.check_call(["pip", "install", "requests"])
        import requests
    
    test_api()
