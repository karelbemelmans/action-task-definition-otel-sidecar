import argparse
import os
import json
from sidecar import SidecarGenerator


def main():
    parser = argparse.ArgumentParser(description='Collect input arguments')
    parser.add_argument('--task-definition', required=False, default="task-definition.json", help='The task defintion')
    args = parser.parse_args()

    # Do some Github feedback stuff
    # print("::notice file=entrypoint.sh,line=11::Checkpoint reached")

    # Read the task definition from file
    try:
        with open(args.task_definition, 'r') as fh:
            taskDefinition = json.load(fh)
    except Exception as e:
        print(f":error reading task definition: {e}")
        exit(1)

    # Validate if the task definition file has a containerDefinitions key
    if 'containerDefinitions' not in taskDefinition:
        print(f"::error: task definition does not contain containerDefinitions")
        exit(1)

    s = SidecarGenerator()
    updatedTaskDefinition = s.addOtelSidecar(taskDefinition)
    print("::info Updated task definition: %s" % updatedTaskDefinition)

    # Generate a new temporary filename with a random filename suffix
    file = f"updated-task-definition.json"

    # Write the updated task definition to file
    try:
        with open(file, 'w') as fh:
            json.dump(file, fh)
    except Exception as e:
        print(f":error writing updated task definition: {e}")
        exit(1)

    # Set the output variable for Github Actions
    try:
        with open(os.environ.get('GITHUB_OUTPUT'), 'a') as fh:
            fh.write(f'task-definition={file}\n')
    except Exception as e:
        print(f":error setting GITHUB_OUTPUT: {e}")
        exit(1)


if __name__ == "__main__":
    main()
