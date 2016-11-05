from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.bulk_save_objects([User(name='wendy', fullname='Wendy Williams', password='foobar'), User(name='mary',
        fullname='Mary Contrary', password='xxg527'),User(name='fred', fullname='Fred Flinstone', password='blah')])
    session.commit()
    """users = session.query(User).all()
    print(users)
    query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
    User.addresses = relationship("Address", order_by=Address.id, back_populates="user")
    jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
    print (jack)"""
