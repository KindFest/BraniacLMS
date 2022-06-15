from locust import HttpUser, task

SERVER_IP_ADDR = "31.31.192.83"


class LoadTestingBraniacLMS(HttpUser):
    @task
    def test_some_pages_open(self):
        # Mainapp
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/1/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/2/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/3/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/4/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/5/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/6/")
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/courses/7/")
        # Authapp
        self.client.get(f"http://{SERVER_IP_ADDR}/authapp/register/")
        self.client.get(f"http://{SERVER_IP_ADDR}/authapp/login/")
        # News
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/news/")
        # Contacts
        self.client.get(f"http://{SERVER_IP_ADDR}/mainapp/contacts/")
