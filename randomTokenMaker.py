import random
import string
from enum import Enum

# basic deviceToken (length: 32)
deviceToken_template = "EA94E25EBEFA4642BE0C12825B871020"

# basic fireBaseToken (length: 163)
firebaseToken_template = "dAZoNolZf0xcsv5qWN3yjn:APA91bHis8PVMqM2w4aCMpMaJlxd3mK5YXiuqsn_oi46xEE6tNFVJNbCLxHAnMPBpKjTd6540G5YZO5g_uiFzqfK49NU4TjKVVueAy4mzHNAYXuI2M3s4sF-RldVt4YrCZzMwbNJxF9C"

# enum the type of token
class Token(Enum):
	FIREBASE = 1
	DEVICEID = 2

# get random token from TokenType
def getRandomToken(tokenType=Token):

	# if type is FireBase token
	if tokenType is Token.FIREBASE:
		return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + "=" + "-" + ":" + "_") for _ in range(len(firebaseToken_template)))
	
	# if type is Device id token
	elif tokenType is Token.DEVICEID:
		return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len(deviceToken_template)))

# tokenArr init
tokenArr = []

# mixString init
mixString = ""

# total count of data
totalDataCount = 10000

# loop the number of range
for num in range(totalDataCount):

	# create randomToken from rules
	randomToken = getRandomToken(tokenType=Token.FIREBASE)

	# create random deviceToken from rules
	randomDeviceId = getRandomToken(tokenType=Token.DEVICEID)

	# check if token exist in tokenArr until is not
	while randomToken in tokenArr:

		# if exist, renew a randomToken
		randomToken = getRandomToken(tokenType=Token.FIREBASE)

		break

	# append new token in tokenArr
	tokenArr.append(randomToken)

	# create a mixString for dataBase
	mixString+="('202109030000001', '{randomDeviceId}', '{randomToken}'),\n".format(randomDeviceId=randomDeviceId, randomToken=randomToken)

	print(num)

# write the mixString to a .txt file and save it to Desktop
with open("{amount}筆測試資料.txt".format(amount=str(int(totalDataCount/10000)) + "萬" if len(str(totalDataCount)) >= 5 else totalDataCount), "w") as text_file:
    text_file.write("%s" % mixString)

# print the total count about tokenArr
print("測試資料總筆數：{amount}".format(amount=len(tokenArr)))
