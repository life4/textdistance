def main(ctx):
    steps = []
    for env in ("pytest-pure", "pytest-external"):
        for python in ("3.6", "3.7", "3.8", "3.9"):
            steps.append(step(env="pytest-pure", python="3.6"))
    steps.append(step(env="flake8", python="3.7"))

    return dict(
        kind="pipeline",
        type="docker",
        name="default",
        trigger=dict(
            branch="master",
        ),
        steps=steps,
    )


def step(env, python):
    result = dict(
        name="{} (py{})".format(env, python),
        image="python:{}-alpine".format(python),
        depends_on=["clone"],  # run in parallel
        environment=dict(
            # set coverage database file name
            # to avoid conflicts between steps
            COVERAGE_FILE=".coverage.{}.{}".format(env, python),
        ),
        commands=[
            # install DepHell
            "apk add curl git gcc libc-dev",
            "python3 -m pip install wheel",
            "curl -L dephell.org/install > install.py",
            "python3 install.py --branch=master",
            "dephell inspect self",
            # install deps
            "export DEPHELL_ENV={}".format(env),
            "dephell venv create",
            "dephell deps install --silent",
            "dephell project register --traceback --level=DEBUG",
            # run
            "dephell venv run",
        ],
    )
    return result
