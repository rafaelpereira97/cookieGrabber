import browser_cookie3

cookies = list(browser_cookie3.firefox())


#get all cookies and write them to a txt file :)
f= open("todasascookies.txt","w+")

for item in cookies:
        f.write("%s\n" % item)