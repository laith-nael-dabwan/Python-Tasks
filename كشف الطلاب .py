def calculate_total(mark1, mark2):
    total = mark1 + mark2
    return total

def calculate_average(total):
    average = total / 2
    return average

def get_grade(average):
    if average >= 90:
        return "ممتاز"
    elif average >= 80:
        return "جيد جداً"
    elif average >= 70:
        return "جيد"
    elif average >= 60:
        return "مقبول"
    else:
        return "راسب"

print("===== نظام نتائج الطلاب =====")
student_name = input("أدخل اسم الطالب : ")

mark1 = float(input("أدخل الدرجة الأولى : "))
mark2 = float(input("أدخل الدرجة الثانية : "))

total = calculate_total(mark1, mark2)
average = calculate_average(total)
grade = get_grade(average)

print("\n------ النتيجة ------")
print("اسم الطالب :", student_name)
print("المجموع :", total)
print("المتوسط :", average)
print("التقدير :", grade)

if average >= 60:
    print("النتيجة: ناجح")
else:
    print("النتيجة: راسب")

print("\n... جاري طباعة رسالة التهنئة")
for i in range(3):
    print("أحسنت يا", student_name)

print(". انتهى البرنامج")
