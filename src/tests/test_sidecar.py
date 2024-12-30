import unittest
from sidecar import SidecarGenerator


class TestSidecar(unittest.TestCase):

    # Example data of a task definition
    taskDefinition = {
        "containerDefinitions": [
            {
                "name": "my-container",
                "image": "my-image"
            }
        ]
    }

    def test_sidear_with_valid_input(self):

        expectedTaskDefinition = {
            "containerDefinitions": [
                {
                    "name": "my-container",
                    "image": "my-image"
                },
                {
                    "name": "otel",
                    "image": "otel/opentelemetry-collector-contrib"
                }
            ]
        }

        s = SidecarGenerator()
        generated = s.addOtelSidecar(self.taskDefinition)
        self.assertEqual(generated, expectedTaskDefinition)


if __name__ == '__main__':
    unittest.main()
