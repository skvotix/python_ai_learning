from dataclasses import dataclass


@dataclass
class Email:
    value: str

@dataclass
class Phone:
    value: str


@dataclass
class Name:
    value: str


@dataclass
class Error:
    error_text: str


@dataclass
class Message:
    text: str
    at_time: str