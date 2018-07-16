class User:
    __total_users = 0

    def __init__(self, first_name, last_name, username, role = "Regular User"):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.role = role
        User.__total_users += 1

    def post(self, post_details):
        print(f"{self.username} posted {post_details}" )

    def comment(self, comment_details):
        print(f"{self.username} commented {comment_details}")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_info(self):
        print(f"Name: {self.full_name()}\nUsername: {self.username}\nRole: {self.role}")

    @classmethod
    def get_total_users(cls):
        print(f"Total Users: {cls.__total_users}")

class Moderator(User):
    __total_moderators = 0

    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username, role = "Moderator")
        Moderator.__total_moderators += 1
        self._spam_removed = 0

    def remove_spam(self):
        self._spam_removed += 1
        print(f"{self.username} has removed a spam")

    def get_total_spam_removed(self):
        print(f"{self.username} has removed {self._spam_removed} spams")

    @property
    def spam_removed(self):
        return self._spam_removed

    @classmethod
    def get_total_moderators(cls):
        print(f"Moderator Total: {cls.__total_moderators}")

user1 = User("Sarah", "Opena", "sarahdelica")
user1.post("Hello erverybody!")
user2 = User("Jeg", "Ramos", "jegramos")
User.get_total_users()
user3 = Moderator("Juilius", "Gorospe", "julius.gorospe")
User.get_total_users()
user1.get_user_info()
user4 = Moderator("Japeth", "Aguilar", "namBOGBOG")
user4.get_user_info()
Moderator.get_total_moderators()
User.get_total_users()