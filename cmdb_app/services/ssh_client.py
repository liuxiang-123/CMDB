import paramiko

class SSHClient:
    def __init__(self, host, username, password, port=22, timeout=15):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            timeout=self.timeout
        )

    def run(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode()

    def close(self):
        if self.client:
            self.client.close()
