# Imports der benötigten Packages
import os
from functools import cache
import uuid
from flask import Flask, request, jsonify, redirect, render_template
from redis import Redis, RedisError

# Definiere die Redis-Funktion und verwende die Umgebungsvariable "REDIS_URL" oder Standardwert "redis://localhost:6379"
@cache
def redis():
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

# Definiere die Variable HOST_NAME für den Hostnamen
HOST_NAME = "http://localhost"

# Definiere die Variable hostname_scaled für Load Balancing
hostname_scaled = os.uname().nodename

# Erstelle und konfiguriere ein Flask-Objekt
app = Flask(__name__, template_folder="/home/realpython/src/url_shortener/templates", static_folder="/home/realpython/src/url_shortener/static")

# Flask Standard-Route z.B "http://localhost"
@app.route("/", methods=["GET", "POST"])
def shorten_url():
    if request.method == 'POST':
        original_url = request.form["url"]

        # Generiere eine eindeutige ID für die verkürzte URL und füge Präfix "id:" hinzu
        short_url_id = str(uuid.uuid4())[:8]
        short_url_id = "id:" + short_url_id

        # Speichere die Verknüpfung zwischen der Original-URL und der verkürzten URL in Redis
        redis().set(short_url_id, original_url)

        # Zähle die Anzahl der Seitenaufrufe und speichere sie in Redis
        urls_shortened = redis().incr("urls_shortened")

        # Zeige das HTML-Template mit der generierten URL und der Anzahl der Seitenaufrufe
        return render_template('index.html', short_url_id=short_url_id, host_url = HOST_NAME, urls_shortened=urls_shortened, hostname_scaled=hostname_scaled)
    
    # Zeige das HTML-Template mit dem zugewiesenen host
    return render_template('index.html', hostname_scaled=hostname_scaled)

# Route zur Umleitung zu einer bestimmten verkürzten URL, falls gefunden
@app.route('/<short_url_id>')
def redirect_to_original_url(short_url_id):
    original_url = redis().get(short_url_id)

    if original_url:
        return redirect(original_url)
    else:
        return "Short URL not found", 404

# Route zur Liste mit den verkürzten URLs in Redis
@app.route("/shortened_urls")
def list_shortened_urls():
        
    # Lege eine Liste zum Speichern der Redis-Einträge fest
    shortened_urls = []

    # Redis-Schlüssel für verkürzte URLs beginnen mit "id:"
    for key in redis().scan_iter(match="id:*"):
        short_url_id = key.decode("utf-8")
        original_url = redis().get(key).decode("utf-8")
        shortened_urls.append({"id": short_url_id, "url": original_url})

    return jsonify(shortened_urls)