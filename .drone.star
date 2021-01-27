def main(ctx):
    steps = []
    for env in ("pytest-pure", "pytest-external"):
        for python in ("3.6", "3.7", "3.8", "3.9"):
            steps.append(step(env=env, python=python))
    steps.append(step(env="flake8", python="3.7"))

    return dict(
        kind="pipeline",
        type="docker",
        name="default",
        trigger=dict(branch="master"),
        steps=steps,
    )


def step(env, python):
    result = dict(
        name="{} (py{})".format(env, python),
        image="python:{}-alpine".format(python),
        depends_on=["install task"],
        environment=dict(
            # set coverage database file name to avoid conflicts between steps
            COVERAGE_FILE=".coverage.{}.{}".format(env, python),
        ),
        commands=[
            "apk add curl git gcc libc-dev",
            "./bin/task PYTHON_BIN=python3 VENVS=/opt/py{python}/ -f {env}:run".format(
                python=python,
                env=env,
            ),
        ],
    )
    return result
