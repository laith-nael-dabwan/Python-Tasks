class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


books_stack = Stack()

books_stack.push("رياضيات")
books_stack.push("لغة عربية")
books_stack.push("علوم")
books_stack.push("تاريخ")

while not books_stack.is_empty():
    print("\n----------------------------------")
    print("الكتب المتاحة:", books_stack.items)
    
    selected_book = input("اكتب اسم الكتاب الذي تريد أخذه: ").strip()

    if selected_book in books_stack.items:
        temp_stack = Stack()
        
        while not books_stack.is_empty():
            item = books_stack.pop()
            if item == selected_book:
                print(f"تم أخذ كتاب: {item}")
                break
            else:
                temp_stack.push(item)
        
        while not temp_stack.is_empty():
            books_stack.push(temp_stack.pop())

        if books_stack.is_empty():
            print("لقد أخذت جميع الكتب! المكتبة فارغة الآن.")
        else:
            print("الكتب المتبقية:", books_stack.items)

    else:
        print("هذا الكتاب ليس موجوداً في القائمة!")
