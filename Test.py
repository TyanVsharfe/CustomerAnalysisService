role = ["user", "manager", "admin"]
reports = ["отчет 1", "отчет 2", "отчет 3", "отчет 4", "отчет 5", "отчет 6", "отчет 7", "отчет 8", "отчет 9",
           "отчет 10", "отчет 11", "отчет 12", "отчет 13", "отчет 14"]

favourite_reports = ["отчет 1", "отчет 2", "отчет 3", "отчет 4", "отчет 5", "отчет 6", "отчет 7"]


class UserTest:
    def __init__(self, username, token_count):
        self.username = username
        self.token_count = token_count
        self.registration = "05.09.2002"
        self.role = role[0]
        self.status = "active"

    username = "vlad"
    token_count = 3000
    registration = "05.09.2002"
    role = role[2]
    # status = "banned"
    status = "active"


UserOne = UserTest("biba", 2150)
UserTwo = UserTest("boba", 21230)

Users = [UserOne, UserTwo]
