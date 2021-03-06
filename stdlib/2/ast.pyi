# Python 2.7 ast

import typing
from typing import Any, Iterator, TypeVar, Union

from _ast import *
from _ast import AST, Module

__version__ = ...  # type: str
PyCF_ONLY_AST = ...  # type: int

_T = TypeVar('_T', bound=AST)

def parse(source: Union[str, unicode], filename: Union[str, unicode] = ..., mode: Union[str, unicode] = ...) -> Module: ...
def copy_location(new_node: AST, old_node: AST) -> AST: ...
def dump(node: AST, annotate_fields: bool = ..., include_attributes: bool = ...) -> str: ...
def fix_missing_locations(node: AST) -> AST: ...
def get_docstring(node: AST, clean: bool = ...) -> str: ...
def increment_lineno(node: AST, n: int = ...) -> AST: ...
def iter_child_nodes(node: AST) -> Iterator[AST]: ...
def iter_fields(node: AST) -> Iterator[typing.Tuple[str, Any]]: ...
def literal_eval(node_or_string: Union[str, unicode, AST]) -> Any: ...
def walk(node: AST) -> Iterator[AST]: ...

class NodeVisitor():
    def visit(self, node: AST) -> Any: ...
    def generic_visit(self, node: AST) -> None: ...

class NodeTransformer(NodeVisitor):
    def generic_visit(self, node: _T) -> _T: ...
