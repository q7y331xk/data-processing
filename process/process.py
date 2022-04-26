from rds.rds import write
from search_data.colors import COLORS
from search_data.locations import DIVS, GUS
from search_data.status import BUYS
from search_func.match_str import match_keywords
from search_func.match_title_main import match_title_main

def process_datum(selling):
    default = '.'
    div = default
    gu = default
    processed_selling = list(selling)

    # div
    div_in_location = match_keywords(processed_selling[9], DIVS, default)
    if div_in_location != default:
        div = div_in_location
    else:
        div = match_title_main(processed_selling, DIVS, default)

    # gu
    gu_in_location = match_keywords(processed_selling[9], GUS, default)
    if gu_in_location != default:
        gu = gu_in_location
    else:
        gu = match_title_main(processed_selling, GUS, default)

    # color
    color = match_title_main(processed_selling, COLORS, default)

    # buy (also in scrapping)
    buy = match_title_main(processed_selling, BUYS, default)
    if buy != default:
        processed_selling[4] = '구매'

    processed_selling[1] = processed_selling[1].replace('\\', ' ')
    processed_selling.append(div)
    processed_selling.append(gu)
    processed_selling.append(color)
    return processed_selling

def process_data(table, sellings_exist):
    for selling in sellings_exist:
        processed_selling = process_datum(selling)
        write(table, processed_selling)