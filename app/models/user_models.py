import ormar


from ..db import metadata, database


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id = ormar.Integer(primary_key=True)
    first_name = ormar.String(max_length=50, unique=False, nullable=True)
    last_name = ormar.String(max_length=50, unique=False, nullable=True)
    company_name = ormar.String(max_length=100, unique=False, nullable=True)
    address = ormar.String(max_length=100, unique=False, nullable=True)
    city = ormar.String(max_length=50, unique=False, nullable=True)
    state = ormar.String(max_length=2, unique=False, nullable=True)
    zip = ormar.String(max_length=10, unique=False, nullable=True)
    phone1 = ormar.String(max_length=20, unique=False, nullable=True)
    phone2 = ormar.String(max_length=20, unique=False, nullable=True)
    email = ormar.String(max_length=100, unique=False, nullable=True)
    department = ormar.String(max_length=50, unique=False, nullable=True)
