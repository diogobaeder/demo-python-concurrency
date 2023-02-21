compile:
  gcc -c -Wall -Werror -fpic -o libs/libdemo.o libs/libdemo.c
  gcc -shared -o libs/libdemo.so libs/libdemo.o

check-call:
  python libs/demo.py

check-sleeps:
  python check_sleeps.py

check-counts-py39:
  python3.9 check_counts.py

check-counts-py310:
  python3.10 check_counts.py
