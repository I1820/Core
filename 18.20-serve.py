#!/usr/bin/env python3

from I1820.http.main import main as main_http
from I1820.mqtt.main import main as main_mqtt
from I1820.controllers.main import main as main_cntl

if __name__ == '__main__':
    print(' * 18.20 at Sep 07 2016 7:20 IR721')
    main_cntl()
    main_mqtt()
    main_http()
