from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import exact
from inspect_ai.solver import generate


@task
def hello_inspect():
    return Task(
        dataset=[
            Sample(
                input="What is 2 + 2? Reply with only the number.",
                target="4",
            )
        ],
        solver=generate(),
        scorer=exact(),
    )