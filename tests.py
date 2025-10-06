from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    print("Results from main.py:")
    print(" " + run_python_file("calculator", "main.py"))

    print("Results from main.py '3 + 5':")
    print(" " + run_python_file("calculator", "main.py", ["3 + 5"]))

    print("Results from test.py:")
    print(" " + run_python_file("calculator", "tests.py"))

    print("Results from incorrect main.py:")
    print(" " + run_python_file("calculator", "../main.py"))

    print("Results from incorrect nonexistent.py:")
    print(" " + run_python_file("calculator", "nonexistent.py"))

#    print("Results for current directory:")
#    print(" " + get_files_info("calculator", "."))
#
#    print("Results from pkg/calculator.py:")
#    print(" " + get_files_info("calculator", "pkg/calculator.py"))
#
#    print("Results from /bin/cat:")
#    print(" " + get_files_info("calculator", "/bin/cat"))
#
#    print("Results from pkg/does_not_exists.py:")
#    print(" " + get_files_info("calculator", "pkg/does_not_exits.py"))
#
#    print("Results for writing lorem.txt:")
#    print(" " + write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#
#    print("Results for writing pkg/morelorem.txt:")
#    print(" " + write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#
#    print("Results for writing /tmp/temp.txt:")
#    print(" " + write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    main()
