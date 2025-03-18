import sqlalchemy
from .db_session import SqlAlchemyBase
from .user import User


class Department(SqlAlchemyBase):
    __tablename__ = 'Department'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)

    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(User.id))

    members = sqlalchemy.Column(sqlalchemy.String)

    email = sqlalchemy.Column(sqlalchemy.String)

    user = sqlalchemy.orm.relationship(User, backref='Department')
