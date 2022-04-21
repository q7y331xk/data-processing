from search_func.match_str import match_keywords

def match_title_main(selling, keywords, default=None):
    title = selling[1]
    main = selling[10]
    found_in_title = match_keywords(title,keywords, default)
    if found_in_title != default:
        return found_in_title
    found_in_main = match_keywords(main, keywords, default)
    if found_in_main != default:
        return found_in_main
    return default
