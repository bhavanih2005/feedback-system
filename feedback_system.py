import sys

def calculate_average_rating(ratings):
    if not ratings:
        return 0.0
    return sum(ratings) / len(ratings)

def feedback_status(avg_rating):
    if avg_rating >= 4.5:
        return "Excellent Feedback"
    elif avg_rating >= 3.5:
        return "Good Feedback"
    elif avg_rating >= 2.5:
        return "Average Feedback"
    else:
        return "Poor Feedback"

def get_ratings_from_args(args):
    ratings = []
    for r in args:
        try:
            val = int(r)
            if 1 <= val <= 5:     # rating should be between 1 and 5
                ratings.append(val)
            else:
                print(f"Warning: Rating {r} ignored (must be 1–5).")
        except ValueError:
            print(f"Warning: '{r}' is not a valid number. Ignored.")
    return ratings

if __name__ == "__main__":
    script_name = sys.argv[0]

    # Check if user has given input
    if len(sys.argv) > 3:
        student_name = sys.argv[1]
        faculty_name = sys.argv[2]
        ratings = get_ratings_from_args(sys.argv[3:])
        print("User provided feedback details:")
    else:
        # Default values
        student_name = "chaitanya"
        faculty_name = "Dr. Rao"
        ratings = [4, 5, 4, 5]
        print("No input given - using default values:")

    avg_rating = calculate_average_rating(ratings)
    status = feedback_status(avg_rating)

    print("\n========== Student Feedback Report ==========")
    print("Script Name :", script_name)
    print("Student Name:", student_name)
    print("Faculty Name:", faculty_name)
    print("Ratings     :", ratings)
    print("Average     :", round(avg_rating, 2))
    print("Status      :", status)
