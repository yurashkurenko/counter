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
        wifipwd=para.split(",")[1]
        description=para.split(",")[2]
        polling=para.split(",")[3]
        lighting=para.split(",")[1]
        chatid=para.split(",")[4]
        return {"id_dev":id_dev,"wifissid":wifissid, \
        "description":description, "polling":polling, \
        "chatid":chatid}
