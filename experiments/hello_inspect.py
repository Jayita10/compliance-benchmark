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
            ),
            Sample(
                input="What is 5 + 3? Reply with only the number.",
                target="8",
            ),
            Sample(
                input="What is 10 - 4? Reply with only the number.",
                target="6",
            ),
            Sample(
                input="What is 3 × 3? Reply with only the number.",
                target="9",
            ),
            Sample(
                input="What is 12 ÷ 4? Reply with only the number.",
                target="3",
            ),
        ],
        solver=generate(),
        scorer=exact(),
    )