CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO User (email, password)
VALUES ('test@example.com', 'password123');

SELECT * FROM User