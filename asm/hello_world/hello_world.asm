section .data
  hello db 'Hello, World!', 10, 0
  
section .text
  global _start
 
_start:
  mov eax, 4     ; sys call #
  mov ebx, 1     ; file descriptor
  mov ecx, hello ; pointer to string
  mov edx, 16    ; string length
  int 0x80       ; interrupt to invoke sys call
  mov eax, 1     ; sys call to exit
  int 0x80       ; interrupt to invoke syscall

  
