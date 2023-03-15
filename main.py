from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief @ mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

    user.surname = "Jonson"
    user.name = "Roby"
    user.age = 19
    user.position = "cook"
    user.speciality = "kitchen captain"
    user.address = "kitchen"
    user.email = "Jonson @ mars.org"
    user.hashed_password = "cook"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

    user.surname = "Wine"
    user.name = "Jone"
    user.age = 20
    user.position = "sailor"
    user.speciality = "scout"
    user.address = "module_2"
    user.email = "Jone @ mars.org"
    user.hashed_password = "sail"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

    user.surname = "Tomson"
    user.name = "Mike"
    user.age = 21
    user.position = "lieutenant"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = " Mike @ mars.org"
    user.hashed_password = "cook"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of resident modules 1 and 2"
    job.work_size = 15
    job.collacorators = "2, 3"
    job.is_finished


if __name__ == "__main__":
    main()