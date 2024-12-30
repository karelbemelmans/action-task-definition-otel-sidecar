# Task Definition Otel Sidecar

This action adds an OpenTelemetry sidecar to an ECS `task-definition.json` file. It's very much overkill to do it this way, but I wanted to create a proper Github action with some good tests.

```yaml
name: Example workflow using our action
on:
  workflow_dispatch:

jobs:
  hello-world:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Run Python action
        id: python-action
        uses: karelbemelmans/task-definition-otel-sidecar@main
        with:
          task-definition: 'example/task-definition.json'
          container-name: 'aws-otel-collector'
          image: 'public.ecr.aws/aws-observability/aws-otel-collector:v0.30.0'

      - name: Show generated task definition
        run: |
          echo "file: ${{ steps.python-action.outputs.task-definition }}"
          cat ${{ steps.python-action.outputs.task-definition }} | jq '.'
```
