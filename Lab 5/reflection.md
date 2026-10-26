# Reflection — Lab 5: Static Code Analysis

### 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing it. It helps identify programming errors, security vulnerabilities, and coding style violations, improving code quality, security, and maintainability.

### 2. What issues did you identify in the Python program?

The tools identified issues such as SQL injection risks, unsafe shell execution, bare exception handling, missing docstrings, inconsistent function naming, long lines, and unspecified file encoding.

### 3. How did Pylint, Bandit, and Flake8 help improve the code?

Pylint helped identify code quality and documentation issues. Bandit detected potential security vulnerabilities, while Flake8 identified formatting and PEP 8 style violations. I fixed the identified issues and reran the tools to verify the improvements.

### 4. What did you learn from this lab?

I learned that static analysis tools help detect problems early, improve code readability, and reduce security risks. Using multiple tools provides a more comprehensive review of a program than relying on manual inspection alone.