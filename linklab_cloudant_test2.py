import conductor
import couchdb


account = conductor.ConductorAccount('hegde.sachet@gmail.com', 'Linklabs@123')
node = account.get_module('$301$0-0-0-03000243e')

#node = account.get_module('')
messages = node.get_recent_messages(mins_back=24*60*10)


#-----------------------------------------------------
couch = couchdb.Server("https://%s.cloudant.com" % 'sachet')
couch.resource.credentials = ('sachet', 'Cloudant@123')
db = couch['linklabs_test1']

for message in messages:
    uplinkMessage=message
    doc_id, doc_rev = db.save({
        'module': uplinkMessage[0],
        'gateway': uplinkMessage[1],
        'payload': uplinkMessage[2]
  
    })
    doc = db[doc_id]
#uplinkMessage=messages[0]
#print uplinkMessage[2]








