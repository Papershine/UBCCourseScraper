# UBCCourseScraper

_A Python script that scrapes for all the undergrad courses and their characteristics from the UBC website_

After running the script, the results will be dumped into `.json` files.

You can access the (not latest) course data using the `.json` files on this repository.

To run the script, run `python3 main.py`.

This script requires `beautifulsoup4` and `requests` to be installed (e.g. from `pip`) in order to function correctly.

Example output for a course:

    {
        "code": "MATH 226",
        "url": "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=MATH&course=226",
        "title": "MATH 226 Advanced Calculus I",
        "prereqs": "Pre-reqs:     Either (a) a score of 68% or higher in MATH 121 or (b) a score of 80% or higher in one of MATH 101, MATH 103, MATH 105, SCIE 001. ",
        "coreqs": "Co-reqs:      One of MATH 152, MATH 221, MATH 223. "
    }

