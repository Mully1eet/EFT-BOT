import sqlite3



connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON')


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS ammo (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# caliber TEXT NOT NULL,
# penetrationPower INTEGER NOT NULL,
# armorDamage INTEGER NOT NULL,
# damage INTEGER NOT NULL
# )
# ''')

def search_ammo(target_ammo):
    cursor.execute("SELECT *, row_number() over(partition by caliber order by penetrationPower desc) as top, count(caliber) over (partition by caliber) as all_top from ammo")
    conclusion = cursor.fetchall()
    for row in conclusion:
        if row[1] == target_ammo:
            return f"Название: {row[1]}\nКалибр: {row[2]}\nПроникаюшщая способность: {row[3]}\nУрон по броне: {row[4]}\nУрон: {row[5]}\nМесто: {row[6]} из {row[7]}"



