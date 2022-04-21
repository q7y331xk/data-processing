from search_data.colors import COLORS
from search_data.locations import DIVS, GUS
from search_func.match_str import match_keywords
from search_func.match_title_main import match_title_main

def process_data(sellings_exist):
    processed_sellings = []
    for selling in sellings_exist:
        default = '.'
        div = default
        gu = default
        processed_selling = list(selling)

        div_in_location = match_keywords(processed_selling[9], DIVS, default)
        if div_in_location != default:
            div = div_in_location
        else:
            div = match_title_main(processed_selling, DIVS, default)

        gu_in_location = match_keywords(processed_selling[9], GUS, default)
        if gu_in_location != default:
            gu = gu_in_location
        else:
            gu = match_title_main(processed_selling, GUS, default)

        color = match_title_main(processed_selling, COLORS, default)

        processed_selling.append(div)
        processed_selling.append(gu)
        processed_selling.append(color)
        print(processed_selling)
    