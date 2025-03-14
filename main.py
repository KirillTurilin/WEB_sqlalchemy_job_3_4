import data.db_session
from data.user import User
from data.jobs import Jobs


def add_user():
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = data.db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def add_job():
    user = Jobs()
    user.team_leader = 1
    user.job = "deployment of residential modules 1 and 2"
    user.work_size = 15
    user.collaborators = "2, 3"
    user.is_finished = False
    db_sess = data.db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

def main():
    data.db_session.global_init("db/bd.db")
    add_job()
    add_user()



if __name__ == '__main__':
    main()