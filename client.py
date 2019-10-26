import socketio
import asyncio

# standard Python
sio = socketio.Client()

# asyncio
#sio = socketio.AsyncClient()

@sio.event
def message(data):
    print('I received a message!')

@sio.on('my message')
def on_message(data):
    print('I received a message!')

@sio.event
def message(data):
    print('I received a message!')


@sio.event
def connect():
    print("I'm connected!")
    print('my sid is', sio.sid)

@sio.event
def disconnect():
    print("I'm disconnected!")


@sio.on("bot_uttered")
def on_bot_msg(data):
    print("Bot: {}".format(data))


#await sio.connect('ws://localhost:5005/socket.io/')
#sio.emit("session_request", {"session_id": "shivam"})


#msg= {"sender_id":"shivam", "message":"bye", "session_id": sio.sid}
#sio.emit("session_request", {"session_id": sio.sid })

#await sio.emit('user_uttered', msg)



def connect():
    sio.connect('ws://localhost:5005/socket.io/')



def send(msg):
    sio.emit('user_uttered', msg)


connect()


msg= {"sender_id":"shivam", "message":"bye", "session_id": sio.sid}
send(msg)


while(True):
    imsg= input()
    print("User: {}".format(imsg))
    msg= {"sender_id":"shivam", "message":imsg, "session_id": sio.sid}
    send(msg)