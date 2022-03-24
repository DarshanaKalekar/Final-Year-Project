from difflib import SequenceMatcher
f = open('Hinglish_Profanity_List.csv', "r")
#f = open("demofile.txt", "r")
dic=[]
profaneSubstitutes = {
    '1': 'i',
    '$': 's',
    '@': 'a',
    '3': 'e',
    '0': 'o',
    '5': 's',
    '#':'h'
}
profaneSubstitutes_keys=profaneSubstitutes.keys()
for x in f:
    f1=x.split(",")
    for l in f1[:-1]:
        dic.append(l)

f.close()
f= open('Hindi.csv', "r")
for x in f:
    dic.append(x[:-1])
#print(list(set(dic)))
Words1 = [
    'cuntfucker', 'assfucker', 'nigga', 'fuckface', 'ballsack', 'cuntlick',
    'negro', 'dickweed', 'camslut', 'dyke', 'biatch', 'pussy', 'boner',
    'Goddamn', 'clitoris', 'flange', 'muff', 'dickless', 'twat', 'knobend',
    'negroes', 'coon', 'labia', 'feck', 'balllicker', 'smegma', 'gangbang',
    'dicksucker', 'slutty', 'pussylover', 'butt', 'bugger', 'boob', 'bastard',
    'whore', 'anus', 'horseshit', 'bitch', 'fellate', 'fuck', 'bum',
    'mothafucka', 'bollock', 'asspacker', 'sex', 'bloody', 'prick', 'blowjob',
    'piss', 'fudgepacker', 'meatbeater', 'vagina', 'dick', 'buttplug',
    'dammit', 'shit', 'crap', 'clit', 'felching', 'fuckbag', 'dildo', 'wank',
    'fucking', 'wanker', 'cocklover', 'ass', 'homo', 'damn', 'turd',
    'fellatio', 'asshat', 'fucker', 'cocksucker', 'bullcrap', 'jerk', 'tosser',
    'cunt', 'nigger', 'shag', 'titjob', 'slut', 'cumslut', 'motherfucking',
    'shithead', 'cockblock', 'scrotum', 'bollok', 'spunk', 'orgy', 'jizz',
    'hell', 'anal', 'poop', 'arse', 'cock', 'balls', 'asswhore', 'fag',
    'bullshit'
]


words=dic+Words1
print(len(words))
from jellyfish import soundex
sen=[]
abusive_sent={}
for word in words:
    sound=soundex(word)
    sen.append(sound)
    if(sound in abusive_sent.keys()):
        abusive_sent[sound].append(word)
    else:
        abusive_sent[sound]=[]
        abusive_sent[sound].append(word)
print(len((sen)))

print(abusive_sent)

print(soundex("chutiya"),soundex("hutya"))
def similar(a, b):
    return SequenceMatcher(None,a, b).ratio()

inp_word=input()
new_inp_word=""
for letter in inp_word:
    if(letter in profaneSubstitutes_keys):
        new_inp_word+=profaneSubstitutes[letter]
    else:
        new_inp_word+=letter
print(new_inp_word)



x=similar("chutiya",new_inp_word)
y=similar("chutiya",inp_word)
print(x,y)
print(soundex("ek"),soundex("egggggs"))





















z={'badir': 'B360', 'idiot': 'I330', 'badirchand': 'B362', 'bakland': 'B245', 'bhadva': 'B310', 'pimp': 'P510', 'bhootnika': 'B352', 'son of a witch': 'S513', 'chinaal': 'C540', 'whore': 'W600', 'chup': 'C100', 'shut up': 'S310', 'chutia': 'C300', 'fucker ': 'F260', 'ghasti': 'G230', 'hooker': 'H260', 'chutiya': 'C300', 'fucker': 'F260', 'haraami': 'H650', 'bastard': 'B236', 'haraam': 'H650', 'hijra': 'H260', 'transsexual ': 'T652', 'hinjda': 'H523', 'jaanvar': 'J516', 'animal': 'A554', 'kutta': 'K300', 'dog': 'D200', 'kutiya': 'K300', 'bitch': 'B320', 'khota': 'K300', 'donkey': 'D520', 'auladheen': 'A435', 'sonless': 'S542', 'jaat': 'J300', 'breed': 'B630', 'najayaz': 'N220', 'illegitimate': 'I423', 'gandpaidaish': 'G531', 'badborn': 'B316', 'saala': 'S400', 'sister’s husband': 'S236', 'kutti': 'K300', 'soover': 'S160', 'swine': 'S500', 'tatti': 'T300', 'shit': 'S300', 'potty': 'P300', 'bahenchod': 'B523', 'sister fucker': 'S236', 'bahanchod': 'B523', 'bahencho': 'B520', 'bancho': 'B520', 'bahenke': 'B520', 'sister’s ': 'S236', 'laude': 'L300', 'dick': 'D200', 'takke': 'T200', 'balls': 'B420', 'betichod': 'B323', 'daughter fucker': 'D236', 'bhaichod': 'B230', 'brother fucker': 'B636', 'bhains': 'B520', 'buffalo': 'B140', 'jhalla': 'J400', 'faggot': 'F230', 'jhant': 'J530', 'pubic': 'P120', 'nabaal': 'N140', 'hairless': 'H642', 'pissu': 'P200', 'bug': 'B200', 'kutte': 'K300', 'maadherchod': 'M362', 'mother fucker': 'M361', 'madarchod': 'M362', 'motherfucker': 'M361', 'padma': 'P350', 'fat bitch': 'F313', 'raand': 'R530', 'jamai': 'J500', 'son-in-law': 'S554', 'randwa': 'R530', 'male prostitute': 'M416', 'randi': 'R530', 'bachachod': 'B223', 'son fucker': 'S512', 'bachichod': 'B223', 'soower': 'S600', 'bachchechod': 'B223', 'children fucker': 'C436', 'ullu': 'U400', 'pathe': 'P300', 'banda': 'B530', 'semi-dick': 'S532', 'booblay': 'B140', 'boobs': 'B120', 'booby': 'B100', 'buble': 'B140', 'babla': 'B140', 'bhonsriwala': 'B526', 'bhonsdiwala': 'B523', 'ched': 'C300', 'pussy': 'P200', 'chut': 'C300', 'chod': 'C300', 'fuck': 'F200', 'chodu': 'C300', 'chodra': 'C360', 'choochi': 'C200', 'chuchi': 'C200', 'gaandu': 'G530', 'asshole': 'A240', 'gandu': 'G530', 'gaand': 'G530', 'ass': 'A200', 'lavda': 'L130', ' dick ': ' 320', 'lawda': 'L300', 'lauda': 'L300', 'lund\xa0': 'L530', ' dick': ' 320', 'balchod': 'B423', 'hair fucker': 'H612', 'lavander': 'L153', 'dick head': 'D230', 'muth': 'M300', 'masturbate ': 'M236', 'maacho': 'M200', 'mammey': 'M500', 'tatte': 'T300', 'toto': 'T300', 'penis': 'P520', 'toota': 'T300', 'broken': 'B625', 'backar': 'B260', 'gossip': 'G210', 'bhandwe': 'B530', 'bhosadchod': 'B232', 'ass fucker': 'A212', 'bhosad': 'B230', 'bumchod': 'B523', 'bum': 'B500', 'bur': 'B600', 'chatani': 'C350', 'ketchup': 'K321', 'cunt': 'C530', 'cuntmama': 'C535', 'chipkali': 'C124', 'lizzard': 'L263', 'pasine': 'P250', 'sweat': 'S300', 'jhaat': 'J300', 'chodela': 'C340', 'fucked up': 'F231', 'bhagatchod': 'B232', 'saint fucker': 'S531', 'chhola': 'C400', 'clit': 'C430', 'chudai': 'C300', 'fucking': 'F252', 'chudaikhana': 'C325', 'whore house': 'W620', 'chunni': 'C500', 'choot': 'C300', 'bhoot': 'B300', 'ghost': 'G230', 'dhakkan': 'D250', 'bhajiye': 'B200', 'snack': 'S520', 'fateychu': 'F320', 'torn pussy': 'T651', 'gandnatije': 'G535', 'Bad result': 'B362', 'lundtopi': 'L531', 'condom': 'C535', 'gaandfat': 'G531', 'gaandmasti': 'G535', 'makhanchudai': 'M252', 'gaandmarau': 'G535', 'ass fuck': 'A212', 'chaatu': 'C300', 'licker': 'L260', 'beej': 'B200', 'semen': 'S550', 'choosu': 'C200', 'sucker': 'S260', 'fakeerchod': 'F262', 'lundoos': 'L532', 'shorba': 'S610', 'binbheja': 'B512', 'brainless': 'B654', 'bhadwe': 'B300', 'parichod': 'P623', 'angel fucker': 'A524', 'nirodh': 'N630', 'condom.': 'C535', 'pucchi': 'P200', 'baajer': 'B260', 'choud': 'C300', 'bhosda': 'B230', 'sadi': 'S300', 'stinking': 'S352', 'choos': 'C200', 'suck': 'S200', 'maka': 'M200', 'mother’s': 'M362', 'prostitute': 'P623', 'gadde': 'G300', 'joon': 'J500', 'chullugand': 'C425', 'handful dirt': 'H531', 'doob': 'D100', 'drown': 'D650', 'khatmal': 'K354', 'gandkate': 'G532', 'bambu': 'B510', 'bamboo': 'B510', 'lassan': 'L250', 'garlic': 'G642', 'danda': 'D530', 'stick': 'S320', 'keera': 'K600', 'keeda': 'K300', 'hazaarchu': 'H262', 'thousand pussy': 'T253', 'paidaishikeeda': 'P322', 'born bug': 'B651', 'kali': 'K400', 'nigger': 'N260', 'safaid': 'S130', 'american': 'A562', 'poot': 'P300', 'son': 'S500', 'behendi': 'B530', 'sister': 'S236', 'chus': 'C200', 'machudi': 'M230', 'chodoonga': 'C352', 'baapchu': 'B120', 'father pussy': 'F361', 'laltern': 'L436', 'lantern': 'L536', 'suhaagchudai': 'S230', 'wedding fuck': 'W352', 'raatchuda': 'R323', 'night fuck': 'N231', 'kaalu': 'K400', 'migga': 'M200', 'neech': 'N200', 'low caste': 'L223', 'chikna': 'C250', 'gay': 'G000', 'meetha': 'M300', 'beechka': 'B200', 'chooche': 'C200', 'patichod': 'P323', 'husband': 'H215', 'rundi': 'R530', 'makkhi': 'M200', 'fly': 'F400', 'biwichod': 'B230', 'wife fucker': 'W112', 'chodhunga': 'C352', 'haathi': 'H300', 'elephant': 'E415', 'kute': 'K300', 'jhanten': 'J535', 'pubic hair': 'P126', 'kaat': 'K300', 'cut': 'C300', 'gandi': 'G530', 'filthy': 'F430', 'gadha': 'G300', 'bimaar': 'B560', 'ill': 'I400', 'badboodar': 'B313', 'smelly': 'S540', 'dum': 'D500', 'tail': 'T400', 'raandsaala': 'R532', 'sister’s brother pimp': 'S236', 'phudi': 'P300', 'chute': 'C300', 'kussi': 'K200', 'khandanchod': 'K535', 'family fucker': 'F541', 'ghussa': 'G200', 'maarey': 'M600', 'dead': 'D300', 'chipkili': 'C124', 'lizard': 'L263', 'unday': 'U530', 'eggs': 'E200', 'budh': 'B300', 'chaarpai': 'C610', 'cot': 'C300', 'chodun': 'C350', 'chatri': 'C360', 'chode': 'C300', 'chodho': 'C300', 'mullekatue': 'M423', 'Derogatory abuse to muslims': 'D623', 'mullikatui': 'M423', 'Derogatory Abuse to female muslim': 'D623', 'mullekebaal': 'M421', 'Derogatory Abuse to muslim': 'D623', 'momedankatue': 'M535', 'katua': 'K300', 'dick cut': 'D223', 'chutiyapa': 'C310', 'fuck all': 'F240', 'bc': 'B200', 'mc': 'M200', 'chudwaya': 'C300', 'kutton': 'K350', 'jungli': 'J524', 'wild': 'W430', 'vahiyaat': 'V300', 'disgusting': 'D223', 'jihadi': 'J300', 'terrorist': 'T662', 'atankvadi': 'A352', 'atankwadi': 'A352', 'aatanki': 'A352', 'terorist': 'T662', 'aand': 'A530', 'aandu': 'A530', 'balatkar': 'B432', 'beti chod': 'B323', 'bhadve': 'B310', 'bhandve': 'B531', 'bhootni ke': 'B352', 'bhosadi ke': 'B232', 'boobe': 'B100', 'chakke': 'C200', 'chinki': 'C520', 'chodu bhagat': 'C312', 'choot ke baal': 'C321', 'chootia': 'C300', 'chootiya': 'C300', 'chuche': 'C200', 'chudai khanaa': 'C325', 'chudan chudai': 'C352', 'chut ke baal': 'C321', 'chut ke dhakkan': 'C323', 'chut maarli': 'C356', 'chutad': 'C330', 'chutadd': 'C330', 'chutan': 'C350', 'gaandufad': 'G531', 'gashti': 'G230', 'gasti': 'G230', 'ghassa': 'G200', 'harami': 'H650', 'haramzade': 'H652', 'hawas': 'H200', 'hawas ke pujari': 'H221', 'hijda': 'H230', 'jhant chaatu': 'J532', 'jhant ke baal': 'J532', 'jhantu': 'J530', 'kamine': 'K550', 'kaminey': 'K550', 'kanjar': 'K526', 'kutta kamina': 'K325', 'kutte ki aulad': 'K324', 'kutte ki jat': 'K322', 'kuttiya': 'K300', 'loda': 'L300', 'lodu': 'L300', 'lund': 'L530', 'lund choos': 'L532', 'lund khajoor': 'L532', 'lundure': 'L536', 'maa ki chut': 'M223', 'maal': 'M400', 'madar chod': 'M362', 'mooh mein le': 'M554', 'mutth': 'M300', 'najayaz aulaad': 'N224', 'najayaz paidaish': 'N221', 'paki': 'P200', 'pataka': 'P320', 'patakha': 'P320', 'saala kutta': 'S423', 'saali kutti': 'S423', 'saali randi': 'S465', 'suar': 'S600', 'suar ki aulad': 'S624', 'teri maa ka bhosada': 'T652', 'teri maa ka boba chusu': 'T652', 'teri maa ki chut': 'T652', 'tharak': 'T620', 'tharki': 'T620', 'cuntfucker': 'C531', 'assfucker': 'A212', 'nigga': 'N200', 'fuckface': 'F212', 'ballsack': 'B422', 'cuntlick': 'C534', 'negro': 'N260', 'dickweed': 'D230', 'camslut': 'C524', 'dyke': 'D200', 'biatch': 'B320', 'boner': 'B560', 'Goddamn': 'G350', 'clitoris': 'C436', 'flange': 'F452', 'muff': 'M100', 'dickless': 'D242', 'twat': 'T300', 'knobend': 'K515', 'negroes': 'N262', 'coon': 'C500', 'labia': 'L100', 'feck': 'F200', 'balllicker': 'B426', 'smegma': 'S525', 'gangbang': 'G521', 'dicksucker': 'D226', 'slutty': 'S430', 'pussylover': 'P241', 'butt': 'B300', 'bugger': 'B260', 'boob': 'B100', 'anus': 'A520', 'horseshit': 'H622', 'fellate': 'F430', 'mothafucka': 'M312', 'bollock': 'B420', 'asspacker': 'A212', 'sex': 'S200', 'bloody': 'B430', 'prick': 'P620', 'blowjob': 'B421', 'piss': 'P200', 'fudgepacker': 'F321', 'meatbeater': 'M313', 'vagina': 'V250', 'buttplug': 'B314', 'dammit': 'D530', 'crap': 'C610', 'felching': 'F425', 'fuckbag': 'F212', 'dildo': 'D430', 'wank': 'W520', 'wanker': 'W526', 'cocklover': 'C241', 'homo': 'H500', 'damn': 'D500', 'turd': 'T630', 'fellatio': 'F430', 'asshat': 'A230', 'cocksucker': 'C226', 'bullcrap': 'B426', 'jerk': 'J620', 'tosser': 'T260', 'shag': 'S200', 'titjob': 'T321', 'slut': 'S430', 'cumslut': 'C524', 'motherfucking': 'M361', 'shithead': 'S330', 'cockblock': 'C214', 'scrotum': 'S635', 'bollok': 'B420', 'spunk': 'S152', 'orgy': 'O620', 'jizz': 'J200', 'hell': 'H400', 'anal': 'A540', 'poop': 'P100', 'arse': 'A620', 'cock': 'C200', 'asswhore': 'A260', 'fag': 'F200', 'bullshit': 'B423'}
value=abusive_sent.keys()
print("oooooooooooo",similar("chutya","chutiyya"))
for k,v in abusive_sent.items():
    if(soundex("ek")==k):
        for i in abusive_sent[k]:
            print(similar("ek",i))
        print(k,v)
