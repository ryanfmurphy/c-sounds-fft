import sqlite3
import uuid

sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
sqlite3.register_adapter(uuid.UUID, lambda u: buffer(u.bytes_le))

conn = sqlite3.connect(
    'db.sqlite',
    detect_types=sqlite3.PARSE_DECLTYPES
)

def init_db():
    uuid_setup();
    c = conn.cursor()
    c.executescript('''

    create table if not exists test (
        id guid primary key,
        name text
    );

    create table if not exists sound (
        id guid primary key,
        name text,
        time timestamp default current_timestamp,
        rating integer
    );

    create table if not exists var (
        id guid primary key,
        name text,
        val text,
        sound_id guid,
        time timestamp default current_timestamp
    );

    ''')

def uuid_setup():
    sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
    sqlite3.register_adapter(uuid.UUID, lambda u: buffer(u.bytes_le))

init_db()

def uuid_test():
    data = (uuid.uuid4(), 'foo')
    print 'Input Data:', data
    c.execute('''
        INSERT INTO test VALUES (?,?)
        ''', data)

    c.execute('''
        SELECT * FROM test
        ''')
    print 'Result Data:', c.fetchone()

