# src/page_tracker/app.py

import os
from functools import cache
import uuid

from flask import Flask, request, jsonify, redirect
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")  # pylint: disable=E1101
        return "Sorry, something went wrong \N{pensive face}", 500
    else:
        return f"This page has been seen {page_views} times."
    
@app.route("/shorten_url", methods=["POST"])
def shorten_url():
    try:
        original_url = request.form.get("original_url")
        if not original_url:
            return "Original URL is required", 400

        # Generiere eine eindeutige ID für die verkürzte URL
        short_url_id = str(uuid.uuid4())[:8]
        shortened_url = f"http://localhost/{short_url_id}"

        # Speichere die Verknüpfung zwischen der Original-URL und der verkürzten URL in Redis
        redis().set(short_url_id, original_url)

        return f"Shortened URL: {shortened_url}"
    except Exception as e:
        app.logger.exception("Error shortening URL")
        return "Sorry, something went wrong \N{pensive face}", 500
    
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
        for key in redis().scan_iter(match="short:*"):
            short_url_id = key.decode("utf-8")[6:]  # Entferne das Präfix "short:"
            original_url = redis().get(key).decode("utf-8")
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
