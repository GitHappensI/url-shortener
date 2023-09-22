import os
from functools import cache
import uuid

from flask import Flask, request, jsonify, redirect, render_template
from redis import Redis, RedisError

HOST_NAME = "http://localhost"

app = Flask(__name__, template_folder="/home/realpython/src/page_tracker/templates", static_folder="/home/realpython/src/page_tracker/static")

@app.route("/", methods=["GET", "POST"])
def shorten_url():
    if request.method == 'POST':
        original_url = request.form["url"]

        # Generiere eine eindeutige ID für die verkürzte URL
        short_url_id = "id" + str(uuid.uuid4())[:8]

        # Speichere die Verknüpfung zwischen der Original-URL und der verkürzten URL in Redis
        redis().set(short_url_id, original_url)

        urls_shortened = redis().incr("urls_shortened")

        # Display the template HTML with the generated url
        return render_template('index.html', short_url_id=short_url_id, host_url = HOST_NAME, urls_shortened=urls_shortened)
    
    return render_template('index.html')

# Route to redirect to a particular shortened url if found
@app.route('/<short_url_id>')
def redirect_to_original_url(short_url_id):
    original_url = redis().get(short_url_id)

    if original_url:
        return redirect(original_url)
    else:
        return "Short URL not found", 404

@app.route("/shortened_urls")
def list_shortened_urls():
    try:
        # Hier kannst du die Liste der verkürzten URLs aus Redis abrufen und sie dem Benutzer anzeigen
        shortened_urls = []

        # Annahme: Redis-Schlüssel für verkürzte URLs beginnen mit "short:"
        for key in redis().scan_iter(match="id:*"):
            short_url_id = key.decode("utf-8")[3:]
            original_url = redis().get(key).decode("utf-8")
            # original_url = "dummy"
            shortened_urls.append({"id": short_url_id, "url": original_url})

        return jsonify(shortened_urls)
    except Exception as e:
        app.logger.exception("Error listing shortened URLs")
        return "Sorry, something went wrong \N{pensive face}", 500

@cache
def redis():
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
