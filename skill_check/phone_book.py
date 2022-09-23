
def solution(phone_book):
    phone_book_count = list(map(len, phone_book))
    phone_book_dict = dict(zip(phone_book, phone_book_count))

    for key, value in phone_book_dict.items():
        if value == min(phone_book_count):
            phone_book.remove(key)
            for i in phone_book:
                if key in i:
                    return False
                    break
    else:
        return True


print(solution(["12", "123", "1235", "567", "88"]))
