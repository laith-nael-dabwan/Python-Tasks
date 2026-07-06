balance = 1000

def check_pin(pin):
    correct_pin = "1234"
    if pin == correct_pin:
        return True
    else:
        return False

def show_balance(balance):
    print("\nرصيدك الحالي =", balance, "ريال")

def withdraw(balance):
    amount = float(input("أدخل مبلغ السحب : "))
    if amount <= 0:
        print("المبلغ غير صحيح")
    elif amount <= balance:
        balance = balance - amount
        print("تم السحب بنجاح")
    else:
        print("الرصيد غير كاف")
    return balance

def deposit(balance):
    amount = float(input("أدخل مبلغ الإيداع: "))
    if amount > 0:
        balance = balance + amount
        print("تم الإيداع بنجاح")
    else:
        print("المبلغ غير صحيح")
    return balance

print("===== مرحباً بك في جهاز الصراف الآلي =====")
pin = input("أدخل الرقم السري: ")

if check_pin(pin):
    print("\n. تم تسجيل الدخول بنجاح")
    choice = 0
    
    while choice != 4:
        print("\n========== القائمة ==========")
        print("1- عرض الرصيد")
        print("2- سحب مبلغ")
        print("3- إيداع مبلغ")
        print("4- خروج")
        
        choice = int(input("اختر العملية : "))
        
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            balance = deposit(balance)
        elif choice == 4:
            print("\n. شكراً لاستخدامك جهاز الصراف الآلي")
else:
    print("الرقم السري غير صحيح")
