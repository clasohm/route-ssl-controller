import json
import yaml
from kubernetes import client, config, watch
import os

if __name__ == "__main__":
    config.load_kube_config()

    api_instance = client.CoreV1Api()
    
    print("Waiting for Routes to come up...")

    for event in watch.Watch().stream(api_instance.list_pod_for_all_namespaces):
        print("Event: %s %s %s" % (event['type'],event['object'].kind, event['object'].metadata.name))
