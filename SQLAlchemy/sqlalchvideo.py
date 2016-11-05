from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import desc
from sqlalchemy import func

Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(50))
    cookie_sku = Column(String(55))
    quantity = Column(Integer)
    unit_cost = Column(Integer)

    def __repr__(self):
        return "<User(name='%s')>" % (self.cookie_name)

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    cc_cookie = Cookie(cookie_name='chocolate chip',
                       cookie_recipe_url='xxxxx',
                       cookie_sku='cc01',
                       quantity=12,
                       unit_cost=50)
    c1 = Cookie(cookie_name='peanut butter',
                cookie_recipe_url='yyyyy',
                cookie_sku='cc02',
                quantity=24,
                unit_cost=25)
    c2 = Cookie(cookie_name='oatmeal raisin',
                cookie_recipe_url='zzzzz',
                cookie_sku='cc03',
                quantity=100,
                unit_cost=35)
    session.bulk_save_objects([cc_cookie, c1, c2])
    session.commit()
    cookies = session.query(Cookie)
    print (cookies)
    for cookie in session.query(Cookie):
        print (cookie)
    """print (session.query(Cookie.cookie_name, Cookie.quantity).first())
    for cookie in session.query(Cookie).order_by(Cookie.quantity):
        print (cookie.quantity, cookie.cookie_name)
    for cookie in session.query(Cookie).order_by(desc(Cookie.cookie_name)):
        print (cookie.quantity, cookie.cookie_name)
    query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
    print ([result.cookie_name for result in query])
    inv_count = session.query(func.sum(Cookie.quantity).label('total_quantity')).scalar()
    print (inv_count)
    rec_count = session.query(func.count(Cookie.cookie_name).label('inventory_count')).first()
    print (rec_count.keys(), rec_count.inventory_count)"""
    print (Cookie.__table__)
    """c3 = Cookie(cookie_name='cornflakes',
                cookie_recipe_url='aaaaa',
                cookie_sku='cc04',
                quantity=40,
                unit_cost=70)
    c2.cookie_name = 'dry fruit'
    session.add(c3)
    query = session.query(Cookie).filter(Cookie.cookie_name.in_(['cornflakes', 'oatmeal raisin'])).all()
    print (query)
    cookies = session.query(Cookie).all()
    print (cookies)
    session.rollback()
    cookies = session.query(Cookie).all()
    print (cookies)"""
