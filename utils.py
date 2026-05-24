
def cleanPhone(phone):
    removeSpaceFromPhone = phone.replace(" ", "")
    removeDashFromPhone = removeSpaceFromPhone.replace("-", "")
    updatedPhone = removeDashFromPhone
    if updatedPhone[0] == "+" and len(updatedPhone) == 14:
        return updatedPhone
    elif updatedPhone[0] == "0" and len(updatedPhone) == 11:
        return "+234"+updatedPhone[1:]
    else:
        return "not valid format"

def cleanEmail(email):
    splitEmail = email.split("@")
    if len(splitEmail) == 2:
        return email
    else:
        return "not valid format"

def getEmailDomain(email):
    splitEmail = email.split(".")
    return splitEmail[len(splitEmail)-1]

def checkIfBusiness(x):
    if x == "biz":
        return "BUSINESS"
    else:
        return "INDIVIDUAL"