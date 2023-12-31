import sqlite3
import time
from apscheduler.schedulers.background import BackgroundScheduler

def get_all_contacts():
    conn = sqlite3.connect('data.db') 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contact")
    
    contacts = cursor.fetchall()

    conn.close()
    return contacts

if __name__ == '__main__':
    all_contacts = get_all_contacts()
    for contact in all_contacts():
        print(contact)
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_new_contacts, 'interval', minutes=5)  # Check every 5 minutes
    scheduler.start()

    try:
        # Keep the script running
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    """