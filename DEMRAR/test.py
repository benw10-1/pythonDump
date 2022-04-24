from ezsender.main import Rabbit

r = Rabbit()

r.connect()

r.send_dict({"d": 22})

r.close()
