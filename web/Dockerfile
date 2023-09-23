FROM python:3.11.2-slim-bullseye

RUN apt-get update && \
    apt-get upgrade --yes

# Erstelle den Benutzer "realpython" mit einem Heimverzeichnis
RUN useradd --create-home realpython
USER realpython
WORKDIR /home/realpython

# Setze die Umgebungsvariable VIRTUALENV und erstelle ein virtuelles Umgebung
ENV VIRTUALENV=/home/realpython/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

# Kopiere die Dateien pyproject.toml und constraints.txt ins aktuelle Arbeitsverzeichnis
COPY --chown=realpython pyproject.toml constraints.txt ./
RUN python -m pip install --upgrade pip setuptools

# Kopiere den gesamten Inhalt des src-Verzeichnisses in das Arbeitsverzeichnis
COPY --chown=realpython src/ src/

# Installiere das Flask-Projekt und verwende die in constraints.txt definierten Abhängigkeiten
RUN python -m pip install . -c constraints.txt

CMD ["flask", "--app", "url_shortener.app", "run", \
     "--host", "0.0.0.0", "--port", "5000"]