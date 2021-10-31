CREATE TABLE school(
    school_id int,
    school_name VARCHAR(255),
    school_address VARCHAR(255),
    PRIMARY KEY(school_id)
);

CREATE TABLE students (
    student_id int,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birth_date DATETIME,
    school_id int,
    gender VARCHAR(255),
    PRIMARY KEY (student_id),
    FOREIGN KEY (school_id) REFERENCES school(school_id)
);

CREATE TABLE author(
    author_id int,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    PRIMARY KEY (author_id)
);

CREATE TABLE genre(
    genre_id int,
    name VARCHAR(255),
    PRIMARY KEY (genre_id)
);

CREATE TABLE book(
    book_id int,
    name VARCHAR(255),
    page_count int,
    author_id int,
    genre_id int,
    PRIMARY KEY (book_id),
    FOREIGN KEY (author_id) REFERENCES author(author_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);

CREATE TABLE loans(
    borrow_id int,
    student_id int,
    book_id int,
    taken_date DATETIME,
    returned_date DATETIME,
    PRIMARY KEY (borrow_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);
