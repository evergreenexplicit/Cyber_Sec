# Zad1
## Stos w funkcji login zajmują kolejno:
- wskaźnik do tablicy code
- adres instrukcji po wywołaniu main
- wartość stack base pointera
- zmienna secret
- zmienna authenticated
- tablica pass[10]
jako że stos rośnie od największego adresu do najmniejszego, nadpisując "pass" zbyt długim stringiem, nadpisujemy też poprzednio zapisane wartości, czyli "authenticated". String nie może być zbyt długi, bo nadpiszemy też poprzednie zmienne.


Do pierwszego zadania nie potrzeba execstack, wystarczy nam tylko buffer overflow umożliwiony przez  - fno-stack-protector.
# fno-stack-protector


fstack-protector is a protection that will put some random content called stack canary before return address of your function call

Before return, it will check the random content is the same as before then return, otherwise it exited.

Because buffer overflow attack is try to overwritten the return address of function, it must overwrite stack canary.

But stack canary is generated randomly, so it could used to prevent overwrite the return address.
 # execstack
Buffer overflow attack also comes with shellcode.

Overwrite the return address and point to your shellcode and then generate the shell.

Execstack is a protection to prevent this happen.

The input buffer is on the stack and your shellcode is, too.

But execstack make memory area of stack non-executable.

When program return to shellcode, it will find out this memory area is non-executable.

It will cause segmentation fault.
