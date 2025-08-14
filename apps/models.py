# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class App(db.Model):

    __tablename__ = 'App'

    id = db.Column(db.Integer, primary_key=True)

    #__App_FIELDS__
    app_id = db.Column(db.Integer, nullable=True)
    app = db.Column(db.Text, nullable=True)
    platform = db.Column(db.Text, nullable=True)
    framework = db.Column(db.Text, nullable=True)
    cdate = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__App_FIELDS__END

    def __init__(self, **kwargs):
        super(App, self).__init__(**kwargs)


class Device(db.Model):

    __tablename__ = 'Device'

    id = db.Column(db.Integer, primary_key=True)

    #__Device_FIELDS__
    room_id = db.Column(db.Integer, nullable=True)
    device_id = db.Column(db.Integer, nullable=True)
    dmodel_id = db.Column(db.Integer, nullable=True)
    device = db.Column(db.Text, nullable=True)
    ir_id = db.Column(db.Integer, nullable=True)
    cpu_id = db.Column(db.Text, nullable=True)
    app_id = db.Column(db.Integer, nullable=True)
    version = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    mdate = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Device_FIELDS__END

    def __init__(self, **kwargs):
        super(Device, self).__init__(**kwargs)


class User(db.Model):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)

    #__User_FIELDS__
    user_id = db.Column(db.Integer, nullable=True)
    user = db.Column(db.Text, nullable=True)
    pwd = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)
    mobile = db.Column(db.String(255),  nullable=True)
    vcount = db.Column(db.Integer, nullable=True)
    expdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.Integer, nullable=True)
    cdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    mdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    remark = db.Column(db.Text, nullable=True)

    #__User_FIELDS__END

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


class Loc_Home(db.Model):

    __tablename__ = 'Loc_Home'

    id = db.Column(db.Integer, primary_key=True)

    #__Loc_Home_FIELDS__
    home_id = db.Column(db.Integer, nullable=True)
    lat = db.Column(db.Text, nullable=True)
    lng = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    mdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    remark = db.Column(db.Text, nullable=True)

    #__Loc_Home_FIELDS__END

    def __init__(self, **kwargs):
        super(Loc_Home, self).__init__(**kwargs)


class Dev_Cate(db.Model):

    __tablename__ = 'Dev_Cate'

    id = db.Column(db.Integer, primary_key=True)

    #__Dev_Cate_FIELDS__
    image = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    cdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    mdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    remark = db.Column(db.Text, nullable=True)

    #__Dev_Cate_FIELDS__END

    def __init__(self, **kwargs):
        super(Dev_Cate, self).__init__(**kwargs)


class Log_Live(db.Model):

    __tablename__ = 'Log_Live'

    id = db.Column(db.Integer, primary_key=True)

    #__Log_Live_FIELDS__
    room = db.Column(db.Integer, nullable=True)
    device = db.Column(db.Integer, nullable=True)
    bdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    edate = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Log_Live_FIELDS__END

    def __init__(self, **kwargs):
        super(Log_Live, self).__init__(**kwargs)


class Log_Switch(db.Model):

    __tablename__ = 'Log_Switch'

    id = db.Column(db.Integer, primary_key=True)

    #__Log_Switch_FIELDS__
    device = db.Column(db.Integer, nullable=True)
    switch = db.Column(db.Integer, nullable=True)
    state = db.Column(db.Integer, nullable=True)
    uid = db.Column(db.Integer, nullable=True)
    ts = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Log_Switch_FIELDS__END

    def __init__(self, **kwargs):
        super(Log_Switch, self).__init__(**kwargs)


class Log_Meter(db.Model):

    __tablename__ = 'Log_Meter'

    id = db.Column(db.Integer, primary_key=True)

    #__Log_Meter_FIELDS__
    device = db.Column(db.Integer, nullable=True)
    meter = db.Column(db.Integer, nullable=True)
    name = db.Column(db.Text, nullable=True)
    value = db.Column(db.Text, nullable=True)
    ts = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Log_Meter_FIELDS__END

    def __init__(self, **kwargs):
        super(Log_Meter, self).__init__(**kwargs)


class Log_Meter_Env(db.Model):

    __tablename__ = 'Log_Meter_Env'

    id = db.Column(db.Integer, primary_key=True)

    #__Log_Meter_Env_FIELDS__
    device = db.Column(db.Integer, nullable=True)
    sensor = db.Column(db.Integer, nullable=True)
    temp = db.Column(db.Text, nullable=True)
    humi = db.Column(db.Text, nullable=True)
    ts = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Log_Meter_Env_FIELDS__END

    def __init__(self, **kwargs):
        super(Log_Meter_Env, self).__init__(**kwargs)


class Ticket(db.Model):

    __tablename__ = 'Ticket'

    id = db.Column(db.Integer, primary_key=True)

    #__Ticket_FIELDS__
    app_id = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    auth = db.Column(db.Integer, nullable=True)
    invit = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    cdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    mdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    remark = db.Column(db.Text, nullable=True)

    #__Ticket_FIELDS__END

    def __init__(self, **kwargs):
        super(Ticket, self).__init__(**kwargs)


class Token(db.Model):

    __tablename__ = 'Token'

    id = db.Column(db.Integer, primary_key=True)

    #__Token_FIELDS__
    token = db.Column(db.Text, nullable=True)
    auth = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    cdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    uid = db.Column(db.Integer, nullable=True)

    #__Token_FIELDS__END

    def __init__(self, **kwargs):
        super(Token, self).__init__(**kwargs)


class Object(db.Model):

    __tablename__ = 'Object'

    id = db.Column(db.Integer, primary_key=True)

    #__Object_FIELDS__
    parent = db.Column(db.Integer, nullable=True)
    type = db.Column(db.Integer, nullable=True)
    deep = db.Column(db.Integer, nullable=True)
    ord = db.Column(db.Integer, nullable=True)
    name = db.Column(db.Text, nullable=True)
    value = db.Column(db.Text, nullable=True)
    opt1 = db.Column(db.Text, nullable=True)
    opt2 = db.Column(db.Text, nullable=True)
    opt3 = db.Column(db.Text, nullable=True)
    status = db.Column(db.Text, nullable=True)
    cdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    mdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    remark = db.Column(db.Text, nullable=True)

    #__Object_FIELDS__END

    def __init__(self, **kwargs):
        super(Object, self).__init__(**kwargs)



#__MODELS__END
