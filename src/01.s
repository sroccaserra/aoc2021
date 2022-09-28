.global _start

.section .data

file:
    .quad 0
buffer:
    .skip 0x100
eol:
    .byte '\n'

.equ O_RDONLY, 0x00
.equ STDOUT, 0x01
.equ EOS, 0
.equ OK, 0

.section .text
_start:
    movq 16(%rsp), %rdi  # 16(%rsp) is argv[1], pass it to open
    call open
    movq %rax, file

    leaq buffer, %rdi
    call readline

    leaq file, %rdi
    call close

    leaq buffer, %rdi
    call print

    movq $0x3c, %rax  # 0x3c syscall is exit()
    movq $OK, %rdi
    syscall

##
# rdi - address of null terminated filename
# returns: the open file descriptor
open:
    movq $0x02, %rax  # 0x02 syscall is open()
    movq $O_RDONLY, %rsi
    syscall
    ret

##
# Reads a line from the currently opened file and stores it as a null
# terminated string
#
# rdi - destination address
# returns: ?
readline:
    pushq %rdi
loopreadline:
    call readc
    cmpb $'\n', (%rsp)
    je endreadline
    incq (%rsp)
    movq (%rsp), %rdi
    jmp loopreadline
endreadline:
    movq (%rsp), %rax
    incq %rax
    movb $EOS, (%rax)
    addq $8, %rsp  # pop
    ret

##
# rdi - destination address
# returns: the number of bytes read
readc:
    movq %rdi, %rsi  # store input to %rsi
    movq $0x00, %rax  # 0x00 syscall is read()
    movq file, %rdi
    movq $1, %rdx
    syscall
    ret

##
# rdi - the file descriptor to close
close:
    movq $0x03, %rax  # 0x03 syscall is close()
    syscall
    ret

##
# rdi - the address of the null-terminated buffer to print
print:
    pushq %rdi
loopprint:
    cmpb $EOS, (%rsp)
    je endprint
    movq (%rsp), %rdi
    call putc
    incq (%rsp)
    jmp loopprint
endprint:
    leaq eol, %rdi
    call putc
    addq $8, %rsp
    ret

##
# rdi - the address of the byte to print
putc:
    movq %rdi, %rsi  # function's first arg is second syscall arg
    movq $0x01, %rax  # 0x01 syscall is write()
    movq $STDOUT, %rdi
    # Length of the data
    movq $1, %rdx
    syscall
    ret
