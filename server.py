import eventlet
import socketio
from mylog import logger as log 

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    if(sid is None):
        sid= sio.sid 
    log.info('User Connected: {}'.format(sid))
    send_msg("You are Connected", sid)

@sio.event
def disconnect(sid):
    log.info('User Disconnected: {}'.format(sid))




@sio.on("join")
def on_join(sid, data):
    log.info("User joined: {}".format(sid))
    sio.emit("utter_join", "{} has joined".format(sid))




@sio.on("user_uttered")
def user_uttered(sid, data):
    log.debug("User : {}".format(data))
    msg= parse_msg(data)
    send_msg(msg, sid)





def parse_msg(data):
    msg= data
    msg= msg.upper()
    #msg= data['message']
    return msg

def send_msg(msg, sid):
    log.info("Bot : {}".format(msg))
    sio.emit("bot_uttered", msg, room=sid)



if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5005)), app)