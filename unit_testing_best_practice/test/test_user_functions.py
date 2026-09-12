import pytest
import io
import sys
sys.path += ['../src']
from user_functions import *


def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'




def test_username_with_user_input_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(''))
    assert get_username_from_input() is None

def test_username_with_user_input_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
    assert get_username_from_input() is None


def test_username_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('dooinn'))
    assert get_username_from_input() == 'dooinn'


def test_password_too_short(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Ab1!'))
    assert get_password_from_input() is None

def test_password_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Password!'))
    assert get_password_from_input() is None

def test_password_no_special_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Password1'))
    assert get_password_from_input() is None

def test_password_no_letter(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12345678!'))
    assert get_password_from_input() is None

def test_password_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Passw0rd!'))
    assert get_password_from_input() == 'Passw0rd!'
