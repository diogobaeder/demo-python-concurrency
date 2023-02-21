compile:
  gcc -c -Wall -Werror -fpic -o libs/demolib.o libs/demolib.c
  gcc -shared -o libs/demolib.so libs/demolib.o

check-call:
  python libs/demolib_wrapper.py

check-concurrency:
  python check_concurrency.py
