from app.calculator import calculator


def test_calculator_add(monkeypatch, capsys):
    inputs = iter(["2 + 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_calculator_subtract(monkeypatch, capsys):
    inputs = iter(["10 - 4", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out


def test_calculator_multiply(monkeypatch, capsys):
    inputs = iter(["3 * 4", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Result: 12.0" in captured.out


def test_calculator_divide(monkeypatch, capsys):
    inputs = iter(["10 / 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_calculator_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["5 / 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out


def test_calculator_invalid_format(monkeypatch, capsys):
    inputs = iter(["2 +", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid format" in captured.out


def test_calculator_invalid_numbers(monkeypatch, capsys):
    inputs = iter(["abc + def", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid numbers" in captured.out


def test_calculator_unsupported_operator(monkeypatch, capsys):
    inputs = iter(["5 ^ 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Error: Unsupported operator" in captured.out


def test_calculator_exit(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out


def test_calculator_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Supported operations" in captured.out


def test_calculator_history_empty(monkeypatch, capsys):
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "No calculations yet" in captured.out


def test_calculator_history_with_entries(monkeypatch, capsys):
    inputs = iter(["2 + 3", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Calculation history:" in captured.out
    assert "AddCalculation(2.0, 3.0) = 5.0" in captured.out