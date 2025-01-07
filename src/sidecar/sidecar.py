class SidecarGenerator:

    def __init__(self, container_name, image):

        # Define the sidecar container
        self.otelSidecarDefinition = {
            "name": container_name,
            "image": image,
            "essential": True,
            "command": ["--config=/etc/ecs/otel-instance-metrics-config.yaml"],
        }

        pass

    def addOtelSidecar(self, json):
        return self._addSidecar(json, self.otelSidecarDefinition)

    def _addSidecar(self, json, sidecar):
        json["containerDefinitions"].append(sidecar)
        return json
