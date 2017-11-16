#!/bin/sh

ps aux | grep "kaiketsusennin" | grep -v grep | awk '{ print "kill -9", $2 }' | sh