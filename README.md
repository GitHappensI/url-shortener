# Url-Shortener
Ein URL-Verkürzer-Projekt mit Minikube, Docker, Flask und Redis.

## Zielsetzung
Dieses Projekt hat das Ziel, einen Webdienst zu entwickeln, der die Verkürzung von langen URLs ermöglicht. Die Kernkomponenten umfassen:

- **Webframework:** Die Anwendung wird auf dem Flask-Webframework aufgebaut.
- **Datenbank:** Redis wird verwendet, um die Zuordnung zwischen verkürzten und Original-URLs zu speichern.
- **Containerisierung:** Die Anwendung wird in einem Docker-Container bereitgestellt, um die Portabilität und Skalierbarkeit zu gewährleisten.
- **Orchestrierung:** Kubernetes wird eingesetzt, um das Netzwerk für die Skalierbarkeit des Webdienstes zu verwalten.
- **Load Balancing:** Ingress wird als Load Balancer verwendet, um den Verkehr effizient zu verteilen.

Durch die Kombination dieser Technologien wird ein zuverlässiger und skalierbarer URL-Verkürzungsdienst bereitgestellt.

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
Führen Sie **"docker compose up"** im Hauptverzeichnis aus, um den Webdienst und Redis zu starten.
Führen Sie das Kubernetes-Netzwerk im Verzeichnis "web/" aus, um den Webdienst skalieren zu können.
Das Kubernetes-Netzwerk kann mit den folgenden Befehlen ausgeführt werden: **"kubectl apply -f redis-data-pvc.yaml"**, **"kubectl apply -f redis-service-deployment.yaml"**, 
**"kubectl apply -f redis-service.yaml"**, **"kubectl apply -f web-service-deployment.yaml"** und **"kubectl apply -f web-service-and-ingress.yaml"**.
Der Webdienst kann über den folgenden Befehl auf z.B. 5 Instanzen skaliert werden **"kubectl scale deployment web-deployment --replicas=5"**.
Die Benutzeroberflächen sind unter http://localhost bzw. http://localhost/shortened_urls verfügbar.
Zusätzlich ist der Webdienst auch über den DHBW-Server unter http://141.72.188.185 zu erreichen.

## Autoren
Leon Seelbach  
Lukas Schönberger  
Daniel Kleiser  
Paul Moosmayer  
  
