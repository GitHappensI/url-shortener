# Url-Shortener
Ein URL-Verkürzer-Projekt mit Minikube, Docker, Flask und Redis.

## Zielsetzung
Dieses Projekt entwickelt einen Webdienst, der es ermöglicht, lange URLs einfach und effizient zu verkürzen. Dabei kommen folgende Technologien zum Einsatz:

- **Webframework:** Die Anwendung wird auf dem Flask-Webframework aufgebaut.
- **Webserver:** Gunicorn dient als Webserver für die Anwendung.
- **Datenbank:** Redis wird verwendet, um die Zuordnung zwischen verkürzten und Original-URLs zu speichern.
- **Containerisierung:** Die Anwendung wird in einem Docker-Container bereitgestellt, um die Portabilität und Skalierbarkeit zu gewährleisten.
- **Orchestrierung:** Kubernetes wird eingesetzt, um das Netzwerk für die Skalierbarkeit des Webdienstes zu verwalten.
- **Load Balancing:** Ingress wird als Load Balancer verwendet, um den Verkehr effizient zu verteilen.

Durch die Kombination dieser Technologien wird ein zuverlässiger und skalierbarer URL-Verkürzungsdienst bereitgestellt.

## Verzeichnisstruktur
**url-shortener/ :** Das Hauptverzeichnis des Projekts.  
< ├── **Docker-Compose.yml :** Die Docker-Compose-Datei zur Bereitstellung von Redis und dem Webdienst.  
< ├── **Anwendungsarchitektur.jpg :** Die grafische Darstellung der Anwendungsarchitektur.  
< └── **screencast/ :** Das Verzeichnis für die Screenncasts und Erklärungsvideo.  
 < < ├── **Erklärungsvideo.mp4 :** Erklärung der Anwendungsarchitektur.  
 < < ├── **Screencast_Docker-Compose.mp4 :** Screencast zur Ausführung von Docker-Compose.  
 < < ├── **Screencast_Minikube.mp4 :** Screencast zur Ausführung des Kubernetes-Netzwerks.  
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
Stellen Sie sicher, dass Docker, Docker-Compose und Minikube installiert sind. Folgen Sie dann diesen Schritten:

**1. Starten Sie Docker-Compose:** Navigieren Sie zum Hauptverzeichnis des Projekts und führen Sie den folgenden Befehl aus, um den Webdienst und Redis zu starten (vgl. Screencast_Docker-Compose.mp4):  
- **"docker compose up"**  

**2. Starten Sie das skalierbare Kubernetes-Netzwerk:** Wechseln Sie in das Verzeichnis "web/" und verwenden Sie die folgenden Befehle, um das Kubernetes-Netzwerk zu erstellen und den Webdienst zu skalieren (vgl. Screencast_Minikube.mp4):  
- **"kubectl apply -f redis-data-pvc.yaml"**  
- **"kubectl apply -f redis-service-deployment.yaml"**  
- **"kubectl apply -f redis-service.yaml"**  
- **"kubectl apply -f web-service-deployment.yaml"**  
- **"kubectl apply -f web-service-and-ingress.yaml"**  

Wenn Sie den Webdienst auf beispielsweise 5 Instanzen skalieren möchten, verwenden Sie den folgenden Befehl:  
- **"kubectl scale deployment web-deployment --replicas=5"**  

**3. Zugriff auf die Benutzeroberflächen:** Nachdem die Dienste gestartet wurden, können Sie die Benutzeroberflächen über Ihren Webbrowser erreichen:
- Der Hauptdienst ist unter http://localhost verfügbar.
- Die Liste der verkürzten URLs finden Sie unter http://localhost/shortened_urls.
- Zusätzlich ist der Webdienst auch über den DHBW-Server unter http://141.72.188.185 erreichbar.

## Autoren
Leon Seelbach  
Lukas Schönberger  
Daniel Kleiser  
Paul Moosmayer