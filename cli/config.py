from logging import DEBUG
from os import getenv

APIURL = getenv("API_URL", "http://localhost")
LOGLEVEL = DEBUG

GAMES = {
    1: ["gnome-terminal", "-e", "/home/julien/Projets/Webgames/Shifumi/client.py --addr {host} --port {port}"]
}
