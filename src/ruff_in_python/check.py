from pathlib import Path
from .message import IfTuple, ImportStarUsage, Location, Message
import ast


def check_statement(path: Path, stmt: ast.stmt) -> list[Message]:
    """recursive function to parse statement"""
    messages = []

    match stmt:
        case ast.FunctionDef() | ast.AsyncFunctionDef() | ast.ClassDef():
            for body_stmt in stmt.body:
                messages.extend(check_statement(path, body_stmt))
        case ast.For() | ast.AsyncFor() | ast.While():
            for body_stmt in stmt.body:
                messages.extend(check_statement(path, body_stmt))
            for orelse_stmt in stmt.orelse:
                messages.extend(check_statement(path, orelse_stmt))
        case (
            ast.Return()
            | ast.Delete()
            | ast.Assign()
            | ast.AugAssign()
            | ast.AnnAssign()
            | ast.Raise()
            | ast.Assert()
            | ast.Import()
            | ast.Global()
            | ast.Nonlocal()
            | ast.Expr()
            | ast.Pass()
            | ast.Break()
            | ast.Continue()
        ):
            pass  # Do nothing for these statement types
        case ast.If():
            # Check if the test is a tuple
            if isinstance(stmt.test, ast.Tuple):  # Assuming node is a tuple type
                messages.append(
                    IfTuple(
                        filename=path,
                        location=Location(row=stmt.lineno, column=stmt.col_offset),
                    )
                )
            for body_stmt in stmt.body:
                messages.extend(check_statement(path, body_stmt))
            for orelse_stmt in stmt.orelse:
                messages.extend(check_statement(path, orelse_stmt))

        case ast.With() | ast.AsyncWith():
            for body_stmt in stmt.body:
                messages.extend(check_statement(path, body_stmt))
        case ast.ImportFrom():
            print(123)
            for alias in stmt.names:
                if alias.name == "*":
                    messages.append(
                        ImportStarUsage(
                            filename=path,
                            location=Location(row=stmt.lineno, column=stmt.col_offset),
                        )
                    )
        case ast.ImportFrom() | ast.Try():
            raise NotImplementedError
        case _:
            print("BUG!: ", type(stmt))
    # Add more elif clauses for other statement types...

    return messages


def check_ast(path: Path, python_ast: list[ast.stmt]) -> list[Message]:
    messages = []
    for stmt in python_ast:
        messages.extend(check_statement(path, stmt))
    print("All Messages:", messages)
    return messages
