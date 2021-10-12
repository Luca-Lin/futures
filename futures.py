import re

def ValidateUrl(url):
    # url regex https://www.codegrepper.com/code-examples/python/regex+for+url+python
    regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    if re.fullmatch(regex, url):
        return True
    else:
        return False

def Search():
    url = input("請輸入網址 URL: ")
    verify = ValidateUrl(url)
    if not verify:
        return
    ans2 = input("輸入要要擷取的範圍")
    if ans2 != "":
        print(ans2)
    else:
        print("ohoh")

Search()