from flask import Flask
from data.db_session import global_init, create_session
from data.users import User

app = Flask(__name__)


def main():
    global_init(input())
    session = create_session()
    for user in session.query(User).filter(User.address == "module_1",
                                           User.speciality.notlike("%engineer%"),
                                           User.position.notlike("%engineer%")):
        print(user)


def __repr__(self):
    return f'<Colonist> {self.id} {self.surname} {self.name}'


if __name__ == "__main__":
    main()