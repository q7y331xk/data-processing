import re

def keywords_extracter(text ,targets):
    founds = []
    for target in targets:
        target_founds = re.findall(target, text)
        for target_found in target_founds:
            founds.append(target_found)
    return founds

def keywords_finder(text, targets):
    isExists = False   
    for target in targets:
        if len(re.findall(target, text)):
            isExists = True
    return isExists

def remove_white_space(text):
    return text.replace(' ','')

founds = keywords_extracter(text = '서울 경 기 남광진', targets = ['서울', '경기', '광진'])
print(founds)

isExists = keywords_finder(text = '서울 경 기 남광진', targets = ['지프', '그랜드 포레스트', '광진'])
print(isExists)

no_white_space = remove_white_space('alkdsfj; alsjfals jfasl;djf ;as jaskl fj')
print(no_white_space)