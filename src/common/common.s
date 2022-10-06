//go:build exclude

.equ SYS_READ, 0x00
.equ SYS_WRITE, 0x01
.equ SYS_OPEN, 0x02
.equ SYS_CLOSE, 0x03
.equ SYS_EXIT, 0x3c

.equ O_RDONLY, 0x00

.equ STDIN, 0x00
.equ STDOUT, 0x01

.equ EOS, 0
.equ OK, 0

.section .data
eol:
    .byte '\n'

.section .text

##
# rdi - the address of the null-terminated buffer to process
# returns: the int value of parsed number
parseint:
    xor %rax, %rax
    mov $10, %rdx
.loopparse:
    xor %rcx, %rcx
    movb (%rdi), %cl
    test %cl, %cl
    jz .endparse
    cmpb eol, %cl
    je .endparse
    imul %rdx, %rax
    sub $'0', %rcx
    add %rcx, %rax
    inc %rdi
    jmp .loopparse
.endparse:
    ret

##
# rdi - the value to print
print_u64:
    enter $32, $0
    mov %rdi, %rax # Set the initial value to print
    mov $10, %r10  # Set our divisor
    mov $'0', %r11 # Ascii offset for numbers
    lea -8(%rbp), %rdi
    movb $EOS, (%rdi)  # Set null-terminated string
.loopp64:
    dec %rdi
    xor %rdx, %rdx
    div %r10
    add %r11, %rdx
    mov %dl, (%rdi)
    test %rax, %rax
    jnz .loopp64

    call print
    leave
    ret

##
# Reads a line from the currently opened file and stores it as a null
# terminated string
#
# Convention: a line includes the eol char if any.
#
# rdi - input file descriptor
# rsi - destination address
# returns: zero if nothing was read, otherwise non zero
readline:
    enter $16, $0
    movq %rsi, -8(%rbp)
    movq %rsi, -16(%rbp)  # remember start of buffer / dest address
.loopreadline:
    movq -8(%rbp), %rsi
    call readc  # file descriptor should stay in %rdi
    test %rax, %rax
    jz .endreadline
    movq -8(%rbp), %rsi
    incq -8(%rbp)
    cmpb $'\n', (%rsi)
    jne .loopreadline
.endreadline:
    movq -8(%rbp), %rsi
    movb $EOS, (%rsi)  # end buffer with zero byte
    mov $0, %rax
    mov -16(%rbp), %rsi
    mov (%rsi), %al  # first read byte is stored in %rax, zero if no read
    leave
    ret

##
# rdi - the address of the null-terminated buffer to print
print:
    pushq %rdi
.loopprint:
    movq (%rsp), %rdi
    cmpb $EOS, (%rdi)
    je .endprint
    call putc
    incq (%rsp)
    jmp .loopprint
.endprint:
    leaq eol, %rdi
    call putc
    addq $8, %rsp
    ret

##
# Low level / OS dependent stuff
##

##
# rdi - input file descriptor
# rsi - destination address
# returns: the number of bytes read
readc:
    movq $SYS_READ, %rax  # 0x00 syscall is read()
    movq $1, %rdx
    syscall
    ret

##
# rdi - the address of the byte to print
putc:
    movq %rdi, %rsi  # function's first arg is second syscall arg
    movq $SYS_WRITE, %rax
    movq $STDOUT, %rdi
    # Length of the data
    movq $1, %rdx
    syscall
    ret

##
# rdi - address of null terminated filename
# returns: the open file descriptor
open:
    movq $SYS_OPEN, %rax
    movq $O_RDONLY, %rsi
    syscall
    ret

##
# rdi - the file descriptor to close
close:
    movq $SYS_CLOSE, %rax
    syscall
    ret
