from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition', backref='roles')

    def __repr__(self) -> str:
        return f'Role(id: {self.id}, character_name: {self.character_name})'
    
    def auditions_list(self):
        return [audition for audition in self.auditions]
    
    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        audition_lead_list = []

        for audition in self.auditions:
            if audition.hired == True:
                audition_lead_list.append(audition)
        
        if len(audition_lead_list) > 0:    
            return audition_lead_list[0]
        else:
            return f'no actor has been hired for this role.'
        
    def understudy(self):
        audition_us_list = []

        for audition in self.auditions:
            if audition.hired == True:
                audition_us_list.append(audition)
        
        if len(audition_us_list) > 1:    
            return audition_us_list[1]
        else:
            return f'no actor has been hired for understudy for this role.'
    
class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(String())
    hired = Column(Integer())
    
    role_id = Column(Integer(), ForeignKey('roles.id'))

    def __repr__(self) -> str:
        return f'Audition(id: {self.id}, hired: {self.hired}, role_id: {self.role_id})'
    
    def role(self):
        return self.roles
    
    def call_back(self):
        self.hired == 1
        return self.hired

breakpoint()