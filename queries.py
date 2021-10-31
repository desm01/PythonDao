def select_all_where_author_id(id):
    return "SELECT * FROM author WHERE author_id ={}".format(id)

def select_all_where_student_id(id):
    return """
    SELECT * FROM students
    INNER JOIN school ON students.student_id = school.school_id 
    WHERE student_id = {}
    """.format(id)

def select_all_where_book_name(name):
    return """
    SELECT * FROM book
    INNER JOIN author on book.author_id = author.author_id
    INNER JOIN genre on book.genre_id = genre.genre_id
    WHERE book.name = '{}'
    """.format(name)

def select_all_where_loan_id(id):
    return """
    SELECT * FROM loans
    INNER JOIN students on loans.student_id = students.student_id
    INNER JOIN book on loans.book_id = book.book_id
    WHERE loans.borrow_id = {}
    """.format(id)

def select_all_loans_where_not_returned():
    return """
    SELECT * FROM loans
    INNER JOIN students on loans.student_id = students.student_id
    INNER JOIN book on loans.book_id = book.book_id
    WHERE returned_date is null
    """