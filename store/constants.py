import os
import sys

name = "Discord Rich Presence for Plex"
version = "2.3.2"

plexClientID = "discord-rich-presence-plex"
discordClientID = "1021479470642761789"
configFilePath = "config.json"
cacheFilePath = "cache.json"
logFilePath = "console.log"

isUnix = sys.platform in ["linux", "darwin"]
processID = os.getpid()
