import os

base_path = os.path.dirname(os.path.dirname(__file__))
env_path = os.path.join(base_path,".env")
print(env_path)