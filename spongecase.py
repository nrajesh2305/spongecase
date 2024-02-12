import random

website_url = "" # Replace later with portfolio website link. 

def printIntro():
    print("sPoNgEcAsE, bY nItHiN rAjEsH " + website_url)

def convert_to_spongecase(message):
    spongecased = ""
    for i in range(len(message)):
        if(not message[i].isalpha()):
            spongecased += message[i]
            continue
        random_case = random.randint(1, 100)
        if random_case >= 40:
            if(message[i].isupper()):
                spongecased += message[i].lower()
                continue
            elif(message[i].islower()):
                spongecased += message[i].upper()
                continue
        else:
            spongecased += message[i]
    return spongecased