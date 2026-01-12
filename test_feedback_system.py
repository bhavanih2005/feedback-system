from feedback_system import calculate_average_rating, feedback_status

def test_average_rating():
    ratings = [4, 5, 3]
    assert calculate_average_rating(ratings) == 4.0   # average = 12/3 = 4.0

def test_empty_ratings():
    ratings = []
    assert calculate_average_rating(ratings) == 0.0

def test_excellent_feedback():
    assert feedback_status(4.6) == "Excellent Feedback"

def test_good_feedback():
    assert feedback_status(3.8) == "Good Feedback"

def test_average_feedback():
    assert feedback_status(2.8) == "Average Feedback"

def test_poor_feedback():
    assert feedback_status(2.0) == "Poor Feedback"
