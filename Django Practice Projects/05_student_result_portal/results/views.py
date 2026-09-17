from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def results(request):
    students = [
        {
            "name": "Mayur Jadhav",
            "roll_no": 101,
            "course": "Python Full Stack",
            "marks": {
                "Python": 85,
                "Django": 78,
                "SQL": 82,
            },
            "percentage": 81.7,
            "grade": "A",
            "result_status": "Pass",
        },
        {
            "name": "Rahul Sharma",
            "roll_no": 102,
            "course": "Python Full Stack",
            "marks": {
                "Python": 72,
                "Django": 68,
                "SQL": 75,
            },
            "percentage": 71.7,
            "grade": "B",
            "result_status": "Pass",
        },
        {
            "name": "Priya Patil",
            "roll_no": 103,
            "course": "Data Science",
            "marks": {
                "Python": 91,
                "Django": 88,
                "SQL": 94,
            },
            "percentage": 91.0,
            "grade": "A+",
            "result_status": "Pass",
        },
        {
            "name": "Amit Kumar",
            "roll_no": 104,
            "course": "Web Development",
            "marks": {
                "Python": 45,
                "Django": 38,
                "SQL": 42,
            },
            "percentage": 41.7,
            "grade": "C",
            "result_status": "Fail",
        },
        {
            "name": "Neha Singh",
            "roll_no": 105,
            "course": "Python Full Stack",
            "marks": {
                "Python": 79,
                "Django": 84,
                "SQL": 76,
            },
            "percentage": 79.7,
            "grade": "B+",
            "result_status": "Pass",
        },
    ]

    return render(request, "results/result.html", {"students": students})