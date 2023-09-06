import os
import yaml

with open("environment.yaml") as file_handle:
    environment_data = yaml.safe_load(file_handle)

print(environment_data)

with open("requirements.txt", "w") as file_handle:
    for dependency in environment_data["dependencies"]:
        if isinstance(dependency, dict):
            for lib in dependency['pip']:
                file_handle.write(lib + "\n")