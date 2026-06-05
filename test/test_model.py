import sys
import os

sys.path.append(
    os.path.abspath(".")
)

from src.ml.predict import predict_code


def test_safe():

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


def test_vulnerable():

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