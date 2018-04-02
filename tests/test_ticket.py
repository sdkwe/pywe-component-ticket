# -*- coding: utf-8 -*-

import redis_extensions as redis
from pywe_component_ticket import ComponentTicket, get_component_verify_ticket, set_component_verify_ticket
from pywe_storage import RedisStorage

from local_wecfg_example import WECHAT


class TestTicketCommands(object):

    def test_component_ticket_mem(self):
        token = WECHAT.get('JSAPI', {}).get('token')
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        encodingaeskey = WECHAT.get('JSAPI', {}).get('encodingaeskey')
        encrypt = 'ghzY0SkCfJlD/dKofrErxS2jaQCfNWWOkzque5y2jCZ+gn+Gv1WeDoKBh+A2RgasuU+B8ZiIl21t89XGZaGnsJ2xFD0rpBqkzmIg2GJslaDbjVJGxPd1kLjOPotbEgAgSqc2b9L3qr/gVq2yWLQrRmHWQndJ19MDhTr95jAL1NF98AkUdVwOlm6NPoAt/CPe82jQzGqBf6IxoupSofeP/Z3fP3itgSOu6VaKoD6mP6AijsdK/qsMxhSOJImTgaXNBGllvgtdTFA7CIqAbp4J/wuVtMlARX1oN3YCPCnJnHXatxZ2VjHINVZmUVSPdoBCw2telFEGJF1RSJTpq5bl/x9+440j0nOT6DF1t7AJLkoM9zUivj1OhrFY3U6ivTFwqbc0jpL4iCHswkaM44CEEeOwbS4tFSkYQI3cy9dtBBH0b23eJbJStwniUa321I394yS2sfu76TvZkM6ZpCjl8Q=='
        msg_signature = '5a9fba8c2a9a3c1e7356ded1b7d4b6df650a902f'
        timestamp = '1522391275'
        nonce = '720781927'
        ticket = 'ticket@@@9xVhCN6TsWYK8fu7hJqriI2B3aJckd-1epTmK-9TYL1bHfUcdR-JKvIDK9VvqF_id_0P7M2nn3WT-_7T_FxcQA'

        component_ticket = ComponentTicket(appid=appid, secret=appsecret, token=token, encodingaeskey=encodingaeskey, storage=None)
        component_ticket.set_component_verify_ticket(post_data=None, encrypt=encrypt, msg_signature=msg_signature, timestamp=timestamp, nonce=nonce)
        ticket1 = component_ticket.get_component_verify_ticket()
        assert isinstance(ticket1, basestring)
        assert ticket == ticket1

        set_component_verify_ticket(appid=appid, secret=appsecret, token=token, encodingaeskey=encodingaeskey, post_data=None, encrypt=encrypt, msg_signature=msg_signature, timestamp=timestamp, nonce=nonce, storage=None)
        ticket2 = get_component_verify_ticket(appid=appid, secret=appsecret, token=token, encodingaeskey=encodingaeskey, storage=None)
        assert ticket == ticket2

    def test_component_ticket_redis(self):
        token = WECHAT.get('JSAPI', {}).get('token')
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')
        encodingaeskey = WECHAT.get('JSAPI', {}).get('encodingaeskey')
        encrypt = 'ghzY0SkCfJlD/dKofrErxS2jaQCfNWWOkzque5y2jCZ+gn+Gv1WeDoKBh+A2RgasuU+B8ZiIl21t89XGZaGnsJ2xFD0rpBqkzmIg2GJslaDbjVJGxPd1kLjOPotbEgAgSqc2b9L3qr/gVq2yWLQrRmHWQndJ19MDhTr95jAL1NF98AkUdVwOlm6NPoAt/CPe82jQzGqBf6IxoupSofeP/Z3fP3itgSOu6VaKoD6mP6AijsdK/qsMxhSOJImTgaXNBGllvgtdTFA7CIqAbp4J/wuVtMlARX1oN3YCPCnJnHXatxZ2VjHINVZmUVSPdoBCw2telFEGJF1RSJTpq5bl/x9+440j0nOT6DF1t7AJLkoM9zUivj1OhrFY3U6ivTFwqbc0jpL4iCHswkaM44CEEeOwbS4tFSkYQI3cy9dtBBH0b23eJbJStwniUa321I394yS2sfu76TvZkM6ZpCjl8Q=='
        msg_signature = '5a9fba8c2a9a3c1e7356ded1b7d4b6df650a902f'
        timestamp = '1522391275'
        nonce = '720781927'
        ticket = 'ticket@@@9xVhCN6TsWYK8fu7hJqriI2B3aJckd-1epTmK-9TYL1bHfUcdR-JKvIDK9VvqF_id_0P7M2nn3WT-_7T_FxcQA'

        r = redis.StrictRedisExtensions(host='localhost', port=6379, db=0)
        storage = RedisStorage(r)

        component_ticket = ComponentTicket(appid=appid, secret=appsecret, token=token, encodingaeskey=encodingaeskey, storage=storage)
        component_ticket.set_component_verify_ticket(post_data=None, encrypt=encrypt, msg_signature=msg_signature, timestamp=timestamp, nonce=nonce)
        ticket1 = component_ticket.get_component_verify_ticket()
        assert isinstance(ticket1, basestring)
        assert ticket == ticket1

        set_component_verify_ticket(appid=appid, secret=appsecret, token=token, encodingaeskey=encodingaeskey, post_data=None, encrypt=encrypt, msg_signature=msg_signature, timestamp=timestamp, nonce=nonce, storage=storage)
        ticket2 = get_component_verify_ticket(appid=appid, secret=appsecret, token=token, encodingaeskey=encodingaeskey, storage=storage)
        assert ticket == ticket2
