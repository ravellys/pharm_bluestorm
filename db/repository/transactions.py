from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from schemas.transactions import ShowTransactions


def list_transactions(db: Session):
    keys = ShowTransactions.__fields__.keys()
    query = """
select T.PATIENT_UUID
     , P.FIRST_NAME
     , P.LAST_NAME
     , date(P.DATE_OF_BIRTH) as DATE_OF_BIRTH
     , T.PHARMACY_UUID
     , PH.NAME
     , PH.CITY
     , T.UUID as TRANSACTION_UUID
     , T.AMOUNT
     , strftime('%Y-%m-%d %H:%M', T.TIMESTAMP) as TIMESTAMP
from TRANSACTIONS T
         join PATIENTS P on T.PATIENT_UUID = P.UUID
         join PHARMACIES PH on T.PHARMACY_UUID = PH.UUID
    """
    statement = text(query)

    with db as con:
        result = con.execute(statement)
        rows = result.all()
    values = [dict(zip(keys, row)) for row in rows]
    return values
