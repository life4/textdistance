def main(ctx):
    return dict(
        kind="pipeline",
        type="docker",
        name="default",
        trigger=dict(branch="master"),
        steps=[
            dict(
                name="install task",
                image="debian:latest",
                commands=[
                    "apt update",
                    "apt install -y wget",
                    "wget https://taskfile.dev/install.sh",
                    "sh install.sh",
                    "rm install.sh",
                ],
            ),

            step(env="pytest-pure", python="3.7"),
            step(env="pytest-pure", python="3.8"),
            step(env="pytest-pure", python="3.9"),
            step(env="pytest-pure", python="3.10"),

            step(env="pytest-external", python="3.7"),
            step(env="pytest-external", python="3.8"),
            step(env="pytest-external", python="3.9"),
            # step(env="pytest-external", python="3.10"),

            step(env="flake8", python="3.9"),
        ],
    )


def step(env, python):
    result = dict(
        name="{} (py{})".format(env, python),
        image="python:{}-buster".format(python),
        depends_on=["install task"],
        environment=dict(
            # set coverage database file name to avoid conflicts between steps
            COVERAGE_FILE=".coverage.{}.{}".format(env, python),
        ),
        commands=[
            "apt update",
            "apt install -y curl git gcc libc-dev build-essential",
            "./bin/task PYTHON_BIN=python3 VENVS=/opt/py{python}/ -f {env}:run".format(
                python=python,
                env=env,
            ),
        ],
    )
    return result
