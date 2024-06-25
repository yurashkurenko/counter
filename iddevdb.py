from vedis import Vedis
IDATABASE =  'idevices.vdb'

def getdevparafromid(dev_id):
    with Vedis(IDATABASE) as idb:
        para=idb[dev_id].decode()
        return para

def getdevparajsonfromid(dev_id):
    with Vedis(IDATABASE) as idb:
        para=idb[dev_id].decode()
        id_dev=para.split(",")[0]
        wifissid=para.split(",")[1]
        wifipwd=para.split(",")[2]
        description=para.split(",")[3]
        polling=para.split(",")[4]
        lighting=para.split(",")[5]
        chatid=para.split(",")[6]
        return {"id_dev":id_dev,"wifissid":wifissid,"wifipwd":wifipwd, \
        "description":description, "polling":polling, \
        "lighting":lighting, "chatid":chatid}
