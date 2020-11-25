#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import csv
import sys
import operator

por_usuario = {}

errores = {}

logfile = "syslog.log"
f = open(logfile, "r")

error_file = "error_message.csv"
user_file = "user_statistics.csv"

for log in f:
    #result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]")
    if result.group(2) not in errores.key():
        errores[result.group(2)] = 0
    errores[result.group(2)] += 1

    if result.group(3) not in por_usuario.keys():
        por_usuario[result.group(3)] = {}
        por_usuario[result.group(3)]["INFO"] = 0
        por_usuario[result.group(3)]["ERROR"] = 0

    if result
