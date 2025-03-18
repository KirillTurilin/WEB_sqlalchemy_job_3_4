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
    database_file = input()
    data.db_session.global_init(f"db/{database_file}")
    db_sess = data.db_session.create_session()
    max_work = []
    for job in db_sess.query(Jobs).all():
        max_work.append(job.work_size)
    for job in db_sess.query(Jobs).filter(Jobs.work_size == max(max_work)).all():
        id_lider = job.team_leader
    for user in db_sess.query(User).filter(User.id == id_lider).all():
        print(user.name, user.surname)




if __name__ == '__main__':
    main()