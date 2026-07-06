def login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    if username == correct_username and password == correct_password:
        return True
    else:
        return False

print("===== نظام تسجيل الدخول =====")
attempt = 1

while attempt <= 3:
    username = input("اسم المستخدم : ")
    password = input("كلمة المرور : ")
    
    if login(username, password):
        print("\n. تم تسجيل الدخول بنجاح")
        break
    else:
        print("\n. اسم المستخدم أو كلمة المرور غير صحيحة")
        attempt += 1

if attempt > 3:
    print("\n. تم إيقاف الحساب بعد ثلاث محاولات فاشلة")
