import scraper

# This program verifies whether web feature extraction for each website is successful.

sites = open("fake.txt", "r").read().split("\n")
checked = open("fake_checked.txt", "w")

for site in sites:
    try:
        #print(site)
        result = scraper.extract("http://www." + site)
        thing = raw_input(">>>")
        if thing == "y":
            checked.write(str(site) + "\n")
            print("Success")
        if thing == "q":
            print("Quitting")
            break
    except Exception as e:
        #print(e)
        pass

checked.close()
