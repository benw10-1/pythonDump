from channels.generic.websocket import AsyncWebsocketConsumer
import json


class BasicConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = self.scope['url_route']['kwargs'][
            'cid']  # gets CID to define the group that the consumer is a part of

        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )  # add consumer to group

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)  # check if data is in JSON format
            print("in: ", data)
            cmd = data['cmd']
        except Exception as e:
            return
        try:
            pass
        except Exception as e:
            print("Exception: " + str(e))

    async def sender(self, event):
        data = event['data']
        print("out: ", data)
        await self.send(text_data=json.dumps(data))
