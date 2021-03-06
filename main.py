from config import EXISTS_RDS_TABLE, PROCESSED_RDS_TABLE
from process.process import process_data
from rds.rds import create_table_if_exists_drop, read

# conn db
sellings_exist = read(EXISTS_RDS_TABLE)
create_table_if_exists_drop(PROCESSED_RDS_TABLE)
process_data(PROCESSED_RDS_TABLE, sellings_exist)