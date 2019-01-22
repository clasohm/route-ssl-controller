from kubernetes import client, config, watch

if __name__ == "__main__":
    config.load_incluster_config()
    crds = client.CustomObjectsApi(api_client)

    for event in watch.Watch().stream(crds.list_cluster_custom_object('route.openshift.io', 'v1', 'routes')):
        print("Event: %s %s %s" % (event['type'],event['object'].kind, event['object'].metadata.name))
