class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    schedule = []
    remaining_subjects = set(subjects)
    available_teachers = sorted(teachers, key=lambda t: (-len(t.can_teach_subjects), t.age))
    
    while remaining_subjects:
        best_teacher = None
        best_covered = set()
        
        for teacher in available_teachers:
            covered = teacher.can_teach_subjects & remaining_subjects
            if len(covered) > len(best_covered):
                best_teacher = teacher
                best_covered = covered
        
        if not best_teacher:
            return None  # Неможливо покрити всі предмети
        
        best_teacher.assigned_subjects = best_covered
        schedule.append(best_teacher)
        remaining_subjects -= best_covered
        available_teachers.remove(best_teacher)
    
    return schedule

if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
    ]
    
    schedule = create_schedule(subjects, teachers)
    
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
