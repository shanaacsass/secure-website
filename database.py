import os

from sqlalchemy import create_engine

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(result.all())
