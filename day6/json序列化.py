# https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424

import json

Info = {
    "name" : "zhoujunjie",
    "age" : 20
}

f = open('test.txt','w')
json.dump(Info,f)

f.close()
