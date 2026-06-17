import sys
import os

sys.path.append(
    os.path.abspath(".")
)

from src.ml.predict import predict_code


def test_safe_c():

    code = """
#include <stdio.h>

int main() {

    char buffer[50];

    fgets(
        buffer,
        sizeof(buffer),
        stdin
    );

    return 0;
}
"""

    result = predict_code(code)

    assert result["result"] == "SAFE"


def test_vulnerable_c():

    code = """
#include <stdio.h>

int main() {

    char buffer[10];

    gets(buffer);

    return 0;
}
"""

    result = predict_code(code)

    assert result["result"] == "VULNERABLE"


def test_safe_python():

    code = """
def suma(a, b):

    return a + b

print(
    suma(
        2,
        3
    )
)
"""

    result = predict_code(code)

    assert result["result"] == "SAFE"


def test_vulnerable_python():

    code = """
import os

cmd = input()

os.system(
    cmd
)
"""

    result = predict_code(code)

    assert result["result"] == "VULNERABLE"