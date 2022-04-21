from config import RDS_TABLE
from process.process import process_data
from search_data.locations import DIVS, GUS
from search_data.colors import COLORS
from rds.rds import read

# conn db
sellings_exist = read(RDS_TABLE)
processed_sellings = process_data(sellings_exist)
# iterate
#   with one row
#   extract locations
#   extract colors


# func
#   