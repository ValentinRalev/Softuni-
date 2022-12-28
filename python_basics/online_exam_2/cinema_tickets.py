input_line = input()
movie = input_line
all_tickets = 0
student_ticket = 0
standart_ticket = 0
kid_ticket = 0
while input_line != "Finish":
    tickets = 0

    empty_seat = int(input())


    type_of_ticket = input()
    while type_of_ticket != "End":
        tickets += 1
        all_tickets += 1

        if type_of_ticket == "student":
            student_ticket += 1
        elif type_of_ticket == "standard":
            standart_ticket += 1
        elif type_of_ticket == "kid":
            kid_ticket += 1
        if tickets == empty_seat:
            break

        type_of_ticket = input()


    movie_percent = tickets / empty_seat * 100
    print(f"{input_line} - {movie_percent:.2f}% full.")


    input_line = input()
student_percent = student_ticket / all_tickets * 100
standart_percent = standart_ticket / all_tickets * 100
kid_percent = kid_ticket / all_tickets * 100
print(f"Total tickets: {all_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standart_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")

