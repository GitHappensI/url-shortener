# url-shortener
Ein URL-Verkürzer-Projekt mit Minikube, Docker, Flask und Redis.

## Beschreibung
Dieses Projekt erstellt einen Webdienst, der es ermöglicht, lange URLs zu verkürzen.
Es verwendet Flask als Webframework, Redis zur Speicherung von Zuordnungen zwischen verkürzten und Original-URLs und Docker zur Containerisierung der Anwendung.
Darüber hinaus wird ein Kubernetes Netzwerk verwendet, um die Skalierbarkeit des Web-Dienstes zu ermöglichen.

## Verzeichnisstruktur
**url-shortener/ :** Das Hauptverzeichnis des Projekts.  
< ├── **Docker-Compose.yml :** Die Docker-Compose-Datei zur Bereitstellung von Redis und dem Webdienst.  
< └── **web/ :** Das Verzeichnis für den Webdienst.  
< < ├── **Dockerfile :** Die Docker-Datei zur Erstellung des Webdienst-Containers.  
< < ├── **constraints.txt :** Die Datei mit den Python-Abhängigkeiten.  
< < ├── **pyproject.toml :** Die Datei zur Konfiguration des Python-Build-Systems.  
< < ├── **redis-data-pvc.yaml :** Die YAML-Datei zur Erstellung eines Persistent Volume Claims für Redis-Daten.  
< < ├── **redis-service.yaml :** Die YAML-Datei zur Erstellung eines Kubernetes-Diensts für Redis.  
< < ├── **redis-service-deployment.yaml :** Die YAML-Datei zur Erstellung eines Kubernetes-Deployments für Redis.  
< < ├── **web-service-and-ingress.yaml :** Die YAML-Datei zur Erstellung eines Kubernetes-Ingress für den Webdienst.  
< < ├── **web-service-deployment.yaml :** Die YAML-Datei zur Erstellung eines Kubernetes-Deployments für den Webdienst.  
< < └── **src/ :** Das Verzeichnis mit dem Quellcode des Webdienstes.  
< < < ├── **app.py :** Die Hauptanwendungsdatei des Webdienstes.  
< < < ├── **templates/ :** Das Verzeichnis mit HTML-Templates.  
< < < < └── **index.html :** Das HTML-Template für die Benutzeroberfläche.  
< < < └── **static/ :** Das Verzeichnis mit statischen Dateien.  
< < < < └── **styles.css :** Das CSS-Stylesheet für das Styling der Benutzeroberfläche.  

## Verwendung
Stellen Sie sicher, dass Docker, Docker-Compose und Minikube installiert sind.  
Führen Sie docker-compose up im Hauptverzeichnis aus, um den Webdienst und Redis zu starten.  
Führen Sie das Kubernetes Netzwerk im Verzeichnis "web/" aus, um den Webdienst skalieren zu können.  
Die Benutzeroberflächen sind unter http://localhost bzw. http://localhost/shortened_urls verfügbar.  

## Autoren
Leon Seelbach  
Lukas Schönberger  
Daniel Kleiser  
Paul Moosmayer  
  
