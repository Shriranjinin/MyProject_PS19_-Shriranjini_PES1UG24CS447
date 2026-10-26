# Issues Identified and Fixes — Lab 5

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection | Security | 9 | SQL query used string interpolation, creating a potential SQL injection vulnerability. | Replaced string interpolation with parameterized SQL queries. |
| Unsafe shell execution | Security | 24 | `shell=True` could allow command injection through unsafe input. | Replaced subprocess execution with `print()`. |
| Bare exception | Code quality | 30 | A bare `except` could hide unexpected errors. | Specified the appropriate exception type. |
| Missing docstrings | Maintainability | 1, 8, 13, 17, 23, 27, 34 | Module and functions lacked documentation. | Added descriptive module and function docstrings. |
| Invalid function naming | Code quality | 8, 13, 17, 23, 27 | Function names did not follow the `snake_case` naming convention. | Renamed functions using `snake_case`. |
| Long lines | Code style | 5, 9, 14, 29 | Lines exceeded the recommended character limit. | Split long statements across multiple lines. |
| Unspecified file encoding | Code quality | 18 | File opening did not explicitly specify an encoding. | Specified UTF-8 encoding. |

**Note:** Line numbers refer to the original code and should be checked against the original reports. Include only fixes actually made in your final code.