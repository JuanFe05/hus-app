from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

class DocumentType(db.Model):

    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name, id = None):
        self.name = name
        if id is not None :
            self.id = id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        self = DocumentType.query.filter_by(id=self.id).first()
    
    @staticmethod
    def get_by_id(id):
        return DocumentType.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return DocumentType.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return DocumentType.query.all()

    def __repr__(self):
        return '<DocumentType {}>'.format(self.name)

class Role(db.Model):

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name, id = None):
        self.name = name
        if id is not None :
            self.id = id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        self = Role.query.filter_by(id=self.id).first()
    
    @staticmethod
    def get_by_id(id):
        return Role.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Role.query.all()

    def __repr__(self):
        return '<Role {}>'.format(self.name)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lastName = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    documentTypeId = db.Column(db.Integer, db.ForeignKey('document_type.id', ondelete='CASCADE'), nullable=False)
    documentNumber = db.Column(db.String(256), unique=True, nullable=False)
    birthDate = db.Column(db.Date, nullable=True)
    phoneNumber = db.Column(db.String(128), nullable=True)
    gender = db.Column(db.String(128), nullable=False)
    accessDate = db.Column(db.Date, nullable=True)
    typeId = db.Column('role', db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    level = db.Column(db.Integer, nullable=True)
    specialty = db.Column(db.String(128), nullable=True)
    documentType = relationship("DocumentType", foreign_keys=[documentTypeId])
    type = relationship("Role", foreign_keys=[typeId])

    def __init__(self, name, lastName, password, documentTypeId, documentNumber, birthDate, phoneNumber, gender, accessDate, typeId, level:int, specialty, is_active=True, isAuthenticated=False):
        self.name = name
        self.lastName = lastName
        self.password = generate_password_hash(password)
        self.documentTypeId = documentTypeId
        self.documentNumber = documentNumber
        self.birthDate = birthDate
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.accessDate = accessDate
        self.typeId = typeId
        self.is_active = is_active
        self.is_authenticated = isAuthenticated
        self.level = level
        self.specialty = specialty

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def set_is_authenticated(self, is_authenticated):
        self.is_authenticated = is_authenticated

    def get_is_authenticated(self):
        return self.is_authenticated

    def is_authenticated(self):
        return self.is_authenticated

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_documentType(self):
        return self.documentType

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_lastName(self) :
        return self.lastName

    def get_password(self) :
        return self.password

    def get_documentNumber(self) :
        return self.documentNumber

    def get_birthDate(self) :
        return self.birthDate

    def get_phoneNumber(self) :
        return self.phoneNumber

    def get_gender(self) :
        return self.gender

    def get_accessDate(self) :
        return self.accessDate

    def get_is_active(self) :
        return self.is_active
        
    def get_level(self) :
        return self.level

    def get_specialty(self) :
        return self.specialty

    def set_documentTypeId(self, documentTypeId) :
        self.documentTypeId = documentTypeId

    def set_typeId(self, typeId) :
        self.typeId = typeId

    def set_id(self, id):
         self.id = id

    def set_type(self, type):
         self.type = type

    def set_name(self, name):
         self.name = name

    def set_lastName(self, lastName) :
         self.lastName = lastName

    def set_documentNumber(self, documentNumber) :
         self.documentNumber = documentNumber

    def set_birthDate(self, birthDate) :
         self.birthDate = birthDate

    def set_phoneNumber(self, phoneNumber) :
         self.phoneNumber = phoneNumber

    def set_gender(self, gender) :
         self.gender = gender
        
    def set_level(self, level) :
         self.level = level

    def set_specialty(self, specialty) :
         self.specialty = specialty

    def set_is_active(self, is_active) :
        self.is_active = is_active
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        self = User.query.filter_by(id=self.id).first()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(name=name).first()

    @staticmethod
    def get_by_type(typeId):
        return User.query.filter_by(typeId=typeId).all()

    @staticmethod
    def get_all():
        return User.query.all()

    def __repr__(self):
        return '<User {}>'.format(self.name)

class UserSimple(User) :

    def __init__(self, name, lastName, id = None):
        self.name = name
        self.lastName = lastName
        if id is not None :
            self.id = id
    
    def __repr__(self):
        return '<UserSimple {}>'.format(self.name)

class Admin(User) :

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, level:int, type=1, is_active=True, isAuthenticated=False):
        super().__init__(name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, level, None, is_active, isAuthenticated)

    def __repr__(self):
        return '<Admin {}>'.format(self.name)

class Doctor(User) :

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, specialty, type=2, is_active=True, isAuthenticated=False):
        super().__init__(name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, None, specialty, is_active, isAuthenticated)

    def __repr__(self):
        return '<Doctor {}>'.format(self.name)

class Patient(User) :

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type =3, is_active=True, isAuthenticated=False):
        super().__init__(name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, None, None, is_active, isAuthenticated)

    def __repr__(self):
        return '<Patient {}>'.format(self.name)

class AppointmentType(db.Model):

    __tablename__ = 'appointment_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name, id = None):
        self.name = name
        if id is not None :
            self.id = id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        self = AppointmentType.query.filter_by(id=self.id).first()
    
    @staticmethod
    def get_by_id(id):
        return AppointmentType.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return AppointmentType.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return AppointmentType.query.all()

    def __repr__(self):
        return '<AppointmentType {}>'.format(self.id)

class Appointment(db.Model):

    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    doctorId = db.Column('doctor', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    patientId = db.Column('patient', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    creationDate = db.Column(db.Date, nullable=False)
    appointmentTypeId = db.Column('appointment_type', db.Integer, db.ForeignKey('appointment_type.id', ondelete='CASCADE'), nullable=False)

    doctor = relationship("User", foreign_keys=[doctorId])
    patient = relationship("User", foreign_keys=[patientId])
    appointmentType = relationship("AppointmentType", foreign_keys=[appointmentTypeId])

    def __init__(self, doctorId:Doctor, date, creationDate, patientId:Patient, appointmentTypeId:AppointmentType):
        self.doctorId = doctorId
        self.date = date
        self.creationDate = creationDate
        self.patientId = patientId
        self.appointmentTypeId = appointmentTypeId
    
    def get_id(self):
        return self.id

    def set_date(self, date):
        self.date = date

    def set_doctorId(self, doctorId):
        self.doctorId = doctorId
    
    def set_patientId(self, patientId):
        self.patientId = patientId

    def set_appointmentTypeId(self, appointmentTypeId):
        self.appointmentTypeId = appointmentTypeId

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        self = Appointment.query.filter_by(id=self.id).first()
    
    @staticmethod
    def get_by_id(id):
        return Appointment.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Appointment.query.filter_by(name=name).first()
    
    @staticmethod
    def get_by_doctor(id):
        return Appointment.query.filter_by(doctorId=id)

    @staticmethod
    def get_by_patient(id):
        return Appointment.query.filter_by(patientId=id)

    @staticmethod
    def get_all():
        return Appointment.query.all()

    def __repr__(self):
        return '<Appointment {}>'.format(self.id)

class Comment(db.Model):

    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    doctorId = db.Column('doctor', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    appointmentId = db.Column('appointment', db.Integer, db.ForeignKey('appointment.id', ondelete='CASCADE'), nullable=False)
    txt = db.Column(db.Text, nullable=False)

    doctor = relationship("User", foreign_keys=[doctorId])
    appointment = relationship("Appointment", foreign_keys=[appointmentId])

    def __init__(self, date, doctorId:Doctor, txt, appointmentId:Appointment):
        self.date = date
        self.doctorId = doctorId
        self.txt = txt
        self.appointmentId = appointmentId

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date
    
    def get_doctor(self):
        return self.doctor

    def get_doctorId(self):
        return self.doctorId

    def get_appointmentId(self):
        return self.appointmentId

    def get_appointment(self):
        return self.appointment

    def get_txt(self):
        return self.txt

    def set_date(self, date):
        self.date = date
    
    def set_doctorId(self, doctorId):
        self.doctorId = doctorId

    def set_appointmentId(self, appointmentId):
        self.appointmentId = appointmentId

    def set_txt(self, txt):
        self.txt = txt

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        self = Comment.query.filter_by(id=self.id).first()

    @staticmethod
    def get_by_id(id):
        return Comment.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Comment.query.filter_by(name=name).firappointmentst()

    @staticmethod
    def get_all():
        return Comment.query.all()

    def __repr__(self):
        return '<Comment {}>'.format(self.id)

""" ========================================================================== """
""" Lista de usuarios para hacer pruebas """

def loadAppointmentType() :
    list = AppointmentType.get_all()
    if not list :
        AppointmentType('General').save()
        AppointmentType('Especialista').save()
        AppointmentType('Pediatra').save()

def loadDocumentType() :
    documentTypes = DocumentType.get_all()
    if not documentTypes :
        DocumentType('C.C.').save()
        DocumentType('T.I.').save()
        DocumentType('Pasaporte').save()
        documentTypes = DocumentType.get_all()
    return documentTypes

def loadRole():
    roles = Role.get_all()
    if not roles :
        Role('Admin').save()
        Role('Doctor').save()
        Role('Paciente').save()
        roles = Role.get_all()
    return roles

def loadData():
    loadAppointmentType()
    loadUsers(loadDocumentType(), loadRole())

def loadUsers(documentTypes, roles) :
    if not User.get_all() :
        Admin('admin', 'admin', 'admin', documentTypes[0].get_id(), '12304566', datetime.now(), '3129989898', 'M', datetime.now(), 1).save()
        Doctor('medico', 'medico', 'medico', documentTypes[1].get_id(), '12304576', datetime.now(), '3129989898', 'M', datetime.now(), "General").save()
        Patient('paciente', 'paciente', 'paciente', documentTypes[2].get_id(), '12304586', datetime.now(), '3129989898', 'M', datetime.now()).save()
    

def get_user(name):
    user = User.get_by_name(name)
    if not user or user.is_active == False :
        user = None
    return user