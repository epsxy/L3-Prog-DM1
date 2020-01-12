.PHONY: test ex1 ex2 ex3 ex4

test:
	py.test ex1/test.py ex2/test.py ex3/test.py ex4/test.py

ex1:
	python3 -m ex1.main

ex2:
	python3 -m ex2.main

ex3:
	python3 -m ex3.main

ex4:
	python3 -m ex4.main
