login.cgi : login.o
	gcc -o login.cgi login.o
	chmod a+rx login.cgi
login.o : login.c
	gcc -c login.c
clean : 
	rm -f login.o
