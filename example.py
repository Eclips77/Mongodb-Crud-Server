"""
🎯 דוגמה לשימוש ב-DAL - Soldiers Management
פשוט ונקי - ללא סיבוכים!
"""

from services.dal import SoldierDAL
from services.solider_entity import Soldier

def main():
    """הרצת דוגמה פשוטה לניהול חיילים"""
    print("🚀 התחלת דוגמה לניהול חיילים")
    print("=" * 50)
    
    try:
        # יצירת DAL
        soldier_dal = SoldierDAL()
        print("✅ חיבור למסד נתונים הושלם בהצלחה")
        
        # יצירת חיילים לדוגמה
        print("\n📝 יצירת חיילים חדשים...")
        
        soldiers_data = [
            {"first_name": "ישראל", "last_name": "כהן", "phone_number": "050-1234567", "rank": "רב-טוראי"},
            {"first_name": "דוד", "last_name": "לוי", "phone_number": "052-9876543", "rank": "טוראי"},
            {"first_name": "מיכל", "last_name": "אבנר", "phone_number": "054-5555555", "rank": "סמל"}
        ]
        
        created_ids = []
        for data in soldiers_data:
            soldier = Soldier(**data)
            soldier_id = soldier_dal.create(soldier)
            created_ids.append(soldier_id)
            print(f"✅ נוצר חייל: {data['first_name']} {data['last_name']} (ID: {soldier_id})")
        
        # קריאת כל החיילים
        print(f"\n📋 רשימת כל החיילים:")
        all_soldiers = soldier_dal.get_all()
        for soldier in all_soldiers:
            print(f"   👤 {soldier.first_name} {soldier.last_name} - {soldier.rank} - {soldier.phone_number}")
        
        # חיפוש לפי שם
        print(f"\n🔍 חיפוש חיילים עם השם 'דוד':")
        search_results = soldier_dal.search_by_name("דוד")
        for soldier in search_results:
            print(f"   🎯 נמצא: {soldier.first_name} {soldier.last_name}")
        
        # קבלת חיילים לפי דרגה
        print(f"\n🎖️ חיילים בדרגת 'טוראי':")
        rank_results = soldier_dal.get_by_rank("טוראי")
        for soldier in rank_results:
            print(f"   🪖 {soldier.first_name} {soldier.last_name}")
        
        # עדכון חייל
        if created_ids:
            print(f"\n✏️ עדכון טלפון של החייל הראשון...")
            update_success = soldier_dal.update(created_ids[0], {"phone_number": "050-9999999"})
            if update_success:
                updated_soldier = soldier_dal.get_by_id(created_ids[0])
                if updated_soldier:
                    print(f"✅ טלפון עודכן ל: {updated_soldier.phone_number}")
        
        # סטטיסטיקות
        total_count = soldier_dal.count()
        print(f"\n📊 סה\"כ חיילים במערכת: {total_count}")
        
        # מחיקת חייל לדוגמה
        if len(created_ids) > 1:
            print(f"\n🗑️ מחיקת חייל לדוגמה...")
            delete_success = soldier_dal.delete(created_ids[-1])
            if delete_success:
                print("✅ החייל נמחק בהצלחה")
                new_count = soldier_dal.count()
                print(f"📊 מספר חיילים עכשיו: {new_count}")
        
        print(f"\n🎉 הדוגמה הושלמה בהצלחה!")
        print("🌐 להרצת השרת: python services/api.py")
        
    except Exception as e:
        print(f"❌ שגיאה: {e}")
        print("💡 וודא שמונגו DB פועל על localhost:27017")

if __name__ == "__main__":
    main()
