#!/usr/bin/env python3

from itertools import product
from pathlib import Path
from typing import Optional, TextIO
import sys


USAGE = """Usage:

Verification modes:
  python traceBFOc <size_of_initial_configuration>
  python traceBFOc <size_of_initial_configuration> all

Trace mode:
  python traceBFOc trace <initial_configuration> <max_steps>
  python traceBFOc trace <initial_configuration> <max_steps> <output_file>

Arguments:
  <size_of_initial_configuration>
      Odd configuration size, at most 31.

  all
      Run verification for every odd size from 5 up to and including
      <size_of_initial_configuration>.

  <initial_configuration>
      Binary configuration, for example 0010101.
      In trace mode its length must be at most 31.

  <max_steps>
      Maximum number of time steps in trace mode.

  <output_file>
      Optional file to which all configurations will be written.
      Configurations are always printed on the screen; when this argument
      is supplied, the same lines are also saved to the file.

Examples:
  python traceBFOc 11
  python traceBFOc 31 all
  python traceBFOc trace 0010101 100
  python traceBFOc trace 0010101 100 configurations.txt
"""


BFOc = 12766019579927887748828308653663109277301603915220967933337785052737964273352395268521715449368631189141265922117328783160550362758681395203209811341541376

setA0000031 = [
    1, 2, 3, 4, 6, 8, 14, 20, 36, 60, 108, 188, 352, 632, 1182,
    2192, 4116, 7712, 14602, 27596, 52488, 99880, 190746, 364724,
    699252, 1342184, 2581428, 4971068, 9587580, 18512792, 35792568,
    69273668, 134219796, 260301176, 505294128, 981706832
]

f = {}


def rule_to_dict(rule: int):
    return {
        f"{i:09b}": (rule >> i) & 1
        for i in range(512)
    }


def s(i1, i2, i3, i4, i5, i6, i7, i8, i9):
    return (
        str(i1) + str(i2) + str(i3) + str(i4) + str(i5)
        + str(i6) + str(i7) + str(i8) + str(i9)
    )


def nonactive():
    for i1, i2, i3, i4, i5, i6, i7, i8, i9 in product(
        range(2), repeat=9
    ):
        x = s(i1, i2, i3, i4, i5, i6, i7, i8, i9)
        f[x] = i5


def bfoc():
    """Corrected BFO rule constructed from transition templates."""
    nonactive()

    # T1 *11100*** -> 1
    for i1, i7, i8, i9 in product(range(2), repeat=4):
        x = s(i1, 1, 1, 1, 0, 0, i7, i8, i9)
        f[x] = 1

    # T2 11100**** -> 1
    for i6, i7, i8, i9 in product(range(2), repeat=4):
        x = s(1, 1, 1, 0, 0, i6, i7, i8, i9)
        f[x] = 1

    # T3 *00100*** -> 1
    for i1, i7, i8, i9 in product(range(2), repeat=4):
        x = s(i1, 0, 0, 1, 0, 0, i7, i8, i9)
        f[x] = 1

    # T4 00100**** -> 1
    for i6, i7, i8, i9 in product(range(2), repeat=4):
        x = s(0, 0, 1, 0, 0, i6, i7, i8, i9)
        f[x] = 1

    # T5 ***0110** -> 0
    for i1, i2, i3, i8, i9 in product(range(2), repeat=5):
        x = s(i1, i2, i3, 0, 1, 1, 0, i8, i9)
        f[x] = 0

    # T6 **0110*** -> 0
    for i1, i2, i7, i8, i9 in product(range(2), repeat=5):
        x = s(i1, i2, 0, 1, 1, 0, i7, i8, i9)
        f[x] = 0

    # T7
    for i1, i2, i3 in product(range(2), repeat=3):
        x = s(i1, i2, 0, 0, 1, 0, 1, 0, i3)
        f[x] = 0

    # T8
    for i1, i2, i3 in product(range(2), repeat=3):
        x = s(i1, 0, 0, 1, 0, 1, 0, i2, i3)
        f[x] = 1

    # T9 ***11101* -> 0
    for i1, i2, i3, i9 in product(range(2), repeat=4):
        x = s(i1, i2, i3, 1, 1, 1, 0, 1, i9)
        f[x] = 0

    # T10 111010*** -> 0
    for i7, i8, i9 in product(range(2), repeat=3):
        x = s(1, 1, 1, 0, 1, 0, i7, i8, i9)
        f[x] = 0

    # T11 1110111** -> 0
    for i8, i9 in product(range(2), repeat=2):
        x = s(1, 1, 1, 0, 1, 1, 1, i8, i9)
        f[x] = 0

    # T12 **1110110 -> 0
    for i1, i2 in product(range(2), repeat=2):
        x = s(i1, i2, 1, 1, 1, 0, 1, 1, 0)
        f[x] = 0

    return f


def next_step(configuration: str, size: int) -> str:
    length = len(configuration)

    return "".join(
        str(
            f[
                "".join(
                    configuration[(size - 4 + cell + offset) % length]
                    for offset in range(9)
                )
            ]
        )
        for cell in range(size)
    )


def toBinary(number: int, size: int) -> str:
    return bin(number).replace("0b", "").zfill(size)


def compute(initial_value: int, size: int):
    configuration = toBinary(initial_value, size)
    steps = 0

    while (
        configuration != size * "0"
        and configuration != size * "1"
        and steps < setA0000031[size] // 2
    ):
        configuration = next_step(configuration, size)
        steps += 1

    return initial_value, configuration, steps


def is_homogeneous(configuration: str) -> bool:
    return (
        configuration == "0" * len(configuration)
        or configuration == "1" * len(configuration)
    )


def validate_trace_arguments(
    initial_configuration: str,
    max_steps: int,
) -> None:
    size = len(initial_configuration)

    if size == 0:
        raise ValueError("Initial configuration cannot be empty.")

    if size % 2 == 0 or size > 31:
        raise ValueError(
            "In trace mode the configuration length must be odd and at most 31."
        )

    if any(value not in "01" for value in initial_configuration):
        raise ValueError(
            "Initial configuration must contain only characters 0 and 1."
        )

    if max_steps < 0:
        raise ValueError("max_steps must be non-negative.")


def format_trace_line(step: int, configuration: str) -> str:
    return f"{step:6d} {configuration}"


def write_trace_line(
    step: int,
    configuration: str,
    output_stream: Optional[TextIO] = None,
) -> None:
    line = format_trace_line(step, configuration)
    print(line)

    if output_stream is not None:
        print(line, file=output_stream)


def trace_configuration(
    initial_configuration: str,
    max_steps: int,
    output_file: Optional[str] = None,
):
    """
    Show all configurations from time 0 until a homogeneous configuration
    is reached or max_steps transitions have been performed. When output_file
    is provided, the same sequence is also written to that file.
    """
    validate_trace_arguments(initial_configuration, max_steps)

    output_stream: Optional[TextIO] = None

    try:
        if output_file is not None:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_stream = output_path.open("w", encoding="utf-8")

        configuration = initial_configuration
        step = 0

        write_trace_line(step, configuration, output_stream)

        while not is_homogeneous(configuration) and step < max_steps:
            configuration = next_step(configuration, len(configuration))
            step += 1
            write_trace_line(step, configuration, output_stream)

        if is_homogeneous(configuration):
            reason = "homogeneous configuration reached"
        else:
            reason = "maximum number of steps reached"

        summary = f"# stopped after {step} steps: {reason}"
        print(summary)
        if output_stream is not None:
            print(summary, file=output_stream)

        return configuration, step, reason
    finally:
        if output_stream is not None:
            output_stream.close()


def validate_verification_size(size: int) -> None:
    if size < 1:
        raise ValueError(
            "size_of_initial_configuration must be positive."
        )

    if size % 2 == 0 or size > 31:
        raise ValueError(
            "size_of_initial_configuration must be an odd number <= 31."
        )


def run_verification(size: int, run_all_sizes: bool) -> None:
    validate_verification_size(size)

    sizes = range(5, size + 1, 2) if run_all_sizes else [size]

    for current_size in sizes:
        for initial_value in range(2 ** current_size):
            result = compute(initial_value, current_size)

            assert (
                result[1] == "0" * current_size
                or result[1] == "1" * current_size
            ), (
                f"r[0]={toBinary(result[0], current_size)}, "
                f"r[1]={result[1]}"
            )
    print(
        f"SUCCESS: all configurations of length {size} "
        "converged to a homogeneous configuration."
    )


def run_trace_mode(arguments) -> int:
    if len(arguments) not in (2, 3):
        print("ERROR: Invalid arguments for trace mode.", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1

    initial_configuration = arguments[0]

    try:
        max_steps = int(arguments[1])
    except ValueError:
        print("ERROR: max_steps must be an integer.", file=sys.stderr)
        return 1

    output_file = arguments[2] if len(arguments) == 3 else None

    try:
        _, _, reason = trace_configuration(
            initial_configuration,
            max_steps,
            output_file,
        )
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if output_file is not None:
        print(f"Configurations saved to: {output_file}")
        print(f"Stop reason: {reason}")

    return 0


def run_verification_mode(arguments) -> int:
    if len(arguments) not in (1, 2):
        print("ERROR: Invalid verification arguments.", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1

    try:
        size = int(arguments[0])
    except ValueError:
        print(
            "ERROR: size_of_initial_configuration must be an integer.",
            file=sys.stderr,
        )
        print(USAGE, file=sys.stderr)
        return 1

    if len(arguments) == 2 and arguments[1] != "all":
        print("ERROR: The optional argument must be 'all'.", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1

    try:
        run_verification(size, run_all_sizes=len(arguments) == 2)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("ERROR: Missing required arguments!", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1

    if sys.argv[1] == "trace":
        return run_trace_mode(sys.argv[2:])

    return run_verification_mode(sys.argv[1:])


f = rule_to_dict(BFOc)
# To construct the corrected rule from templates instead, use:
# f = bfoc()


if __name__ == "__main__":
    sys.exit(main())
