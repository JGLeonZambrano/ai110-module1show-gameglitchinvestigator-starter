from app import check_guess, parse_guess

# --- Existing starter tests (import fixed: was logic_utils, now app) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"

# --- New tests targeting new bug fixes ---

def test_decimal_input_rejected():
    # Bug fix: decimals should be rejected, not silently truncated
    ok, value, err = parse_guess("7.5")
    assert ok == False
    assert err is not None

def test_out_of_range_rejected():
    # Bug fix: out-of-range numbers should be rejected
    ok, value, err = parse_guess("0")
    assert ok == False
    assert "range" in err.lower()