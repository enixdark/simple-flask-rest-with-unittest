from app import db


class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_or_404(cls, id):
        return cls.query.get_or_404(id)

    def update(self, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def remove(self, commit=True):
        self.delete = True
        return commit and self.save()
