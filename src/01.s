.global _start

.section .data

file:
    .quad 0
buffer:
    .skip 0x100

.equ O_RDONLY, 0x0
.equ STDOUT, 0x1

.section .text
_start:
    movq 16(%rsp), %rdi  # 16(%rsp) is argv[1], pass it to open
    call open
    movq %rax, file

    call readline

    leaq file, %rdi
    call close

    leaq buffer, %rdi
    call print

    movq $0x3c, %rax  # 0x3c syscall is exit()
    movq $0, %rdi
    syscall

##
# rdi - address of null terminated filename
# returns: the open file descriptor
open:
    movq $0x02, %rax  # 0x02 syscall is open()
    movq $O_RDONLY, %rsi
    syscall
    ret

readline:
    movq $0x00, %rax  # 0x00 syscall is read()
    movq file, %rdi
    leaq buffer, %rsi
    movq $8, %rdx
    syscall
    ret

##
# rdi - the file descriptor to close
close:
    movq $0x03, %rax  # 0x03 syscall is close()
    syscall
    ret

##
# rdi - the buffer to print
print:
    movq %rdi, %rsi  # function's first arg is second syscall arg
    movq $0x01, %rax  # 0x01 syscall is write()
    movq $STDOUT, %rdi
    # Length of the data
    movq $4, %rdx
    syscall
    ret
