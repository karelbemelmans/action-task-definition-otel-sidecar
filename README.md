# My first Python Action

This action runs a Python script that simply return a hello line using the name that was passed as an input argument.

Example workflow:

```yaml
name: Example workflow using our action
on:
  workflow_dispatch:

jobs:
  hello-world:
    runs-on: ubuntu-latest
    steps:
      - name: Run Python action
        id: hello-world
        uses: karelbemelmans/my-first-python-action@main
        with:
          who: "John Connor"

      - name: Show greeting
        run: |
          echo "${{ steps.hello-world.outputs.greeting }}"

```
