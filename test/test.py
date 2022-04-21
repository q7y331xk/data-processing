import re

def main_find_location(main_text):
    si= r"[가-힣]+군"
    si= r"[가-힣]+시"
    si= r"[가-힣]+구"
    si= r"[가-힣]+동"
    find_si = re.findall(si, main_text)
    if si:
        print(find_si)
    return 0

main_find_location(" 서울시 광진구 자양동")