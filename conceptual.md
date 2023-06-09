### Conceptual Exercise

####Answer the following questions below:

1. What is PostgreSQL?

- PostgreSQL is the Open Source relational database management system that is a specific implementation of a relational database management system that supports SQL along with its own set of features. In other words, PostgreSQL is a software that uses SQL as its language for managing and manipulating data. So, PostgreSQL is related to SQL in the sense that it uses SQL to communicate with it and manage its data.

2. What is the difference between SQL and PostgreSQL?

- SQL is a programming language used to communicate with relational databases. PostgreSQL is a specific implementation of a relational database management system that supports SQL along with its own set of features.

3. In `psql`, how do you connect to a database?

- \c <DATABASE_NAME>

4. What is the difference between `HAVING` and `WHERE`?

- **WHERE** is used to filter rows before grouping, while **HAVING** is used to filter groups after grouping.

5. What is the difference between an `INNER` and `OUTER` join?

- **INNER** returns only the matching rows between two tables, while **OUTER JOIN** returns all rows from both tables and fills in NULL for non-matching rows.

6. What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

- **LEFT OUTER JOIN** returns all rows from the left table and matching rows from the right table, while **RIGHT OUTER JOIN** returns all rows from the right table and matching rows from the left table.

7. What is an ORM? What do they do?

- **Object-Relational Mapping**, is a technique for converting data between incompatible type systems in object-oriented programming languages and relational databases ex. **SQLAlchemy**. ORMs provide a way to interact with a database using high-level programming language constructs, rather than low-level SQL.

8. What are some differences between making HTTP requests using AJAX
   and from the server side using a library like `requests`?

- Making HTTP requests using AJAX allows for asynchronous communication between the client and server, while making requests from the server side using a library like requests happens synchronously. Additionally, AJAX requests can be made without reloading the page, while server-side requests require a page reload.

9. What is CSRF? What is the purpose of the CSRF token?

- CSRF, or Cross-Site Request Forgery, is a type of attack that tricks a user into unknowingly executing actions on a website that they are logged into. A CSRF token is a unique value that is generated by a server and included in a form to prevent these types of attacks.

- Let's say you are logged into your social media account, and you receive a message from a friend with a link to a funny video. When you click on the link, you are taken to a website that looks like the social media website, but it is actually a fake website designed to steal your login credentials. When you enter your username and password on the fake website, the attacker can intercept the information and use it to log in to your account and possibly perform malicious actions.

10. What is the purpose of `form.hidden_tag()`?

- form.hidden_tag() is used in Flask to generate a hidden input field containing a CSRF token, which can be included in forms to prevent CSRF attacks.
