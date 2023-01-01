#!/usr/bin/python3
import drop

while True:
    text = input("~@drop~:#$ ")
    if text.strip() == "":
        continue
    result, error = drop.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
