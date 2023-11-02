"""Driver code which imports our custom package and execute the function"""
"""
package-folder (test_package directory)
├── test_driver.py
└── my_package
    └── __init__.py
"""
from my_package import count_in_list

my_list = ["Sunil", "Prathamesh", "Aditya", "Prathamesh"]
word = "Prathamesh"
count = count_in_list(my_list, word)
print(f"{word} in list occurd {count} times")
