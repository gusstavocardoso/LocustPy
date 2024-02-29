from locust import HttpUser, TaskSet, task, between

class AlbumTaskSet(TaskSet):
    @task(1)
    def get_albums(self):
        self.client.get("/albums")

    @task(2)
    def create_album(self):
        payload = {
            "banda": "Metallica",
            "album": "Master Of Puppets",
            "ano": 1986,
            "integrantes": ["James", "Lars", "Kirk", "Cliff"]
        }
        self.client.post("/albums", json=payload)

class WebsiteUser(HttpUser):
    tasks = [AlbumTaskSet]
    wait_time = between(5, 9)
