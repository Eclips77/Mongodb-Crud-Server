"""
🔧 בדיקת חיבור מהירה למונגו DB
"""

from services.connection_dal import DatabaseConnection

def test_connection():
    """בדיקת חיבור למסד נתונים"""
    print("🔗 בודק חיבור למונגו DB...")
    
    try:
        db_conn = DatabaseConnection()
        
        if db_conn.test_connection():
            print("✅ החיבור למונגו DB תקין!")
            db_name = db_conn.database.name if db_conn.database is not None else 'לא ידוע'
            print(f"📊 מסד נתונים: {db_name}")
            return True
        else:
            print("❌ לא ניתן להתחבר למונגו DB")
            return False
            
    except Exception as e:
        print(f"❌ שגיאה בחיבור: {e}")
        print("💡 וודא שמונגו DB פועל על localhost:27017")
        return False

if __name__ == "__main__":
    test_connection()
