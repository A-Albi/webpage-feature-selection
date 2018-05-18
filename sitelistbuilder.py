import scraper

sites = open("legit.txt", "a")

while True:
    try:
        site = raw_input(">>> ")
        if site == "q":
            break
        result = scraper.extract(site)
        sites.write(str(site) + "\n")
        print("Success")
    except:
        print("Failed")

sites.close()
