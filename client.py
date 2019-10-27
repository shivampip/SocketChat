import socketio
import asyncio
from mylog import logger as log 

# standard Python
sio = socketio.Client()

# asyncio
#sio = socketio.AsyncClient()

@sio.event
def message(data):
    print('I received a message!')


@sio.event
def connect():
    log.debug("I'm connected!")
    log.debug('my sid is', sio.sid)
    sio.emit("join", sio.sid)

@sio.event
def disconnect():
    log.debug("I'm disconnected!")


@sio.on("bot_uttered")
def on_bot_msg(data):
    log.info("Bot: {}".format(data))


@sio.on("utter_join")
def on_join(data):
    log.info(data)

#await sio.connect('ws://localhost:5005/socket.io/')
#sio.emit("session_request", {"session_id": "shivam"})


#msg= {"sender_id":"shivam", "message":"bye", "session_id": sio.sid}
#sio.emit("session_request", {"session_id": sio.sid })

#await sio.emit('user_uttered', msg)



def connect():
    #sio.connect('ws://localhost:5005/socket.io/')
    log.debug("Connecting...")
    sio.connect('ws://localhost:5005/')



def send(msg):
    sio.emit('user_uttered', msg)


connect()


msg= {"sender_id":"shivam", "message":"bye", "session_id": sio.sid}
#send(msg)


while(True):
    imsg= input()
    log.debug("User: {}".format(imsg))
    #msg= {"sender_id":"shivam", "message":imsg, "session_id": sio.sid}
    msg= imsg
    send(msg)