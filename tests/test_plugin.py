import ast
import pytest
from flake8_no_chained_assignments.plugin import NoChainedAssignmentsChecker, ERROR_CODE


def _run(code: str):
    tree = ast.parse(code)
    checker = NoChainedAssignmentsChecker(tree)
    return list(checker.run())


def test_simple_assignment_ok():
    errors = _run("a = 1")
    assert errors == []


def test_augmented_assignment_ok():
    errors = _run("a += 1")
    assert errors == []


def test_annotated_assignment_ok():
    errors = _run("a: int = 1")
    assert errors == []


def test_chained_assignment_detected():
    errors = _run("a = b = 1")
    assert len(errors) == 1
    code, col, msg, _type = errors[0]
    assert msg.startswith(ERROR_CODE)


def test_chained_assignment_triple():
    errors = _run("a = b = c = 1")
    assert len(errors) == 1
    assert errors[0][2].startswith(ERROR_CODE)


def test_chained_assignment_line_number():
    src = "\nx = y = 42\n"
    errors = _run(src)
    assert len(errors) == 1
    line, col, msg, _type = errors[0]
    assert line == 2


def test_multiple_chained_assignments():
    src = "a = b = 1\nc = d = 2\n"
    errors = _run(src)
    assert len(errors) == 2


def test_function_scope():
    src = """
def foo():
    x = y = 0
    return x, y
"""
    errors = _run(src)
    assert len(errors) == 1
