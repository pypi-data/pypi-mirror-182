import abc
from typing import Final

from volsite_postgres_common.db.FnT import FnT


class Arg:
    input: Final[str] = "_input"
    result: Final[str] = "_result"

    def __init__(self, name: str, d_type: FnT):
        self.name = name
        self.type = d_type

    def to_str(self) -> str:
        return f"{self.name}\t{self.type.value}"


class APlPgSqlFunction(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def in_args(self) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def out_args(self) -> list:
        raise NotImplementedError

    def declare(self) -> list:
        return list()

    @abc.abstractmethod
    def body(self) -> str:
        raise NotImplementedError

    def build_function(self) -> str:
        fn = f" CREATE OR REPLACE FUNCTION {self.name()} \n"
        if len(self.in_args()) + len(self.out_args()) > 0:
            fn += " (\n"
            args = list()
            for i in self.in_args():
                args.append(f" IN {i.to_str()}")
            for o in self.out_args():
                args.append(f" OUT {o.to_str()}")
            fn += ",\n".join(args)
            fn += "\n )\n"
        fn += " AS \n"
        fn += " $$ \n"
        if len(self.declare()) > 0:
            fn += " DECLARE \n"
            for d in self.declare():
                fn += f" {d.to_str()};\n"
        fn += " BEGIN \n\n"
        fn += self.body()
        fn += "\n\n END; \n"
        fn += " $$ \n"
        fn += " LANGUAGE PlPgSQL;"

        return fn


class AJsonPlPgSqlFunction(APlPgSqlFunction, metaclass=abc.ABCMeta):
    def in_args(self) -> list:
        return [
            Arg(Arg.input, FnT.JSONB)
        ]

    def out_args(self) -> list:
        return [
            Arg(Arg.result, FnT.JSONB)
        ]


class ASqlFunction(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def in_args(self) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def return_type(self) -> FnT:
        raise NotImplementedError

    @abc.abstractmethod
    def body(self) -> str:
        raise NotImplementedError

    def build_function(self) -> str:
        fn = f" CREATE OR REPLACE FUNCTION {self.name()} \n"
        if len(self.in_args()) > 0:
            fn += " (\n"
            args = list()
            for i in self.in_args():
                args.append(f" {i.to_str()}")
            fn += ",\n".join(args)
            fn += "\n )\n"
        if self.return_type() is None:
            fn += " RETURNS VOID\n"
        else:
            fn += f" RETURNS {self.return_type().value} \n"
        fn += " AS \n"
        fn += " $$ \n\n"
        fn += self.body()
        fn += "\n\n $$ \n"
        fn += " LANGUAGE SQL;"

        return fn


class AJsonSqlFunction(ASqlFunction, metaclass=abc.ABCMeta):
    def in_args(self) -> list:
        return [
            Arg(Arg.input, FnT.JSONB)
        ]

    def return_type(self) -> FnT:
        return FnT.JSONB