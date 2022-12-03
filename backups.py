import requests,sys,concurrent.futures,time
def testspeed():
    def statuscode(name, timeout=0.1):
        try:
            status = requests.get(url_name+"/"+name, allow_redirects=False)
        except:
            return False
        if "incident id" in status.text or "access denied" in status.text:
                return False
        elif len(status.text) <= 40:
            return False
        if status.status_code == 200:
            print(status.url+"\n"+str(status.status_code))
    try:
        url_name = sys.argv[1]
    except:
        print("usage is python3 backups.py https://sub.domain.com without / in the end!")
    else:
        if url_name.startswith("https://"):
            delete = url_name.replace("https://","")
            regex = delete.split(".")[0]
        elif url_name.startswith("http://"):
            delete = url_name.replace("http://","")
            regex = delete.split(".")[0]
        end_points = ["gz","zip","tar","tar.gz","csv","doc","docx","xls","xlsx","sql","7z","rar","dump.sql","sql.tar.gz","sql.zip","bak","backup","bakup","old","tmp","log","db","sql.bak","zip.bak","zip.old"]
        for i in end_points:
            i = regex+"."+i
            statuscode(i)
        for i in end_points:
            i = delete+"."+i
            statuscode(i)

#new line
with concurrent.futures.ThreadPoolExecutor() as pl:
    pl.submit(testspeed())
