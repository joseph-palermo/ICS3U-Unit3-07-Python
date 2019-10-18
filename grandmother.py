#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program checks the grandmothers apporval
# or incorrect


def main():
    # This function checks the grandmothers approval

    # input
    print("This is an application to see if you're good enough for my "
          "grandchild.")
    print("Answer True or False to these questions.")

    # process
    rich = input("Are you rich? (True or False): ")
    print("")
    good_looking = input("Are you good looking? (True or False): ")
    print("")

    # output

    if rich == "True" or good_looking == "True":
        print("Good job child, you can date my grandchild. "
              "But if you hurt her I will hurt you.")
    else:
        print("thank u, next")


if __name__ == "__main__":
    main()
