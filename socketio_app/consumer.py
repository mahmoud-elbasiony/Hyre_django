# from socketio import Namespace

# from rest_framework.response import Response
# from rest_framework import status, generics



# class MyNamespace(generics.GenericAPIView):
    
#     def on_connect(self):
#         print('Client connected')

#     def on_disconnect(self):
#         print('Client disconnected')

#     def on_my_event(self, data):
#         print('Received data:', data)
#         self.emit('my_response', {'message': 'Response from server'})




# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.accept()
#         await self.send(text_data=json.dumps({"msg":"WebSocket connection opened"}))
        
     

#     async def disconnect(self, close_code):
#         # Called on WebSocket closing
#         pass

#     async def receive(self, text_data):
#         # Called on WebSocket receiving a message
#         pass


# from channels.consumer import SyncConsumer

# class EchoConsumer(SyncConsumer):

#     def websocket_connect(self, event):
#         print(event["type"])
#         self.send({
#             "type": "websocket.accept" 
#         })

        

#     def websocket_receive(self, event):
#         print(event["text"])
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })

from channels.consumer import AsyncConsumer


class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print(event["text"])
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

        
    async def websocket_disconnect(self, event):
        # Handle WebSocket disconnection
         await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })    