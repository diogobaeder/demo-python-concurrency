compile:
  gcc -c -Wall -Werror -fpic -o libs/libdemo.o libs/libdemo.c
  gcc -shared -o libs/libdemo.so libs/libdemo.o

check-call:
  python libs/demo.py

check-concurrency:
  python check_concurrency.py
