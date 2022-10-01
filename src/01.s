.global _start

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

.equ MAX_LINE, 0xff
.equ BUFFER_SIZE, MAX_LINE+1

.section .data
eol:
    .byte '\n'

.section .bss
sum:
    .quad 0
file:
    .quad 0
buffer:
    .skip BUFFER_SIZE

.section .text
_start:
    cmpq $2, (%rsp)  # (%rsp) is argc, compare 2 to it.
    jl .hasnofilename
    movq 16(%rsp), %rdi  # 16(%rsp) is argv[1], pass it to open
    call open
    movq %rax, file
    jmp .hasfilename
.hasnofilename:
    movq $STDIN, %rax
.hasfilename:
    movq %rax, file

.mainloop:
    leaq buffer, %rdi
    call readline
    test %rax, %rax
    jz .endmainloop

    leaq buffer, %rdi
    call processline
    jmp .mainloop

.endmainloop:
    leaq file, %rdi
    call close

    mov sum, %rdi
    call print_u64

    movq $SYS_EXIT, %rax
    movq $OK, %rdi
    syscall

##
# rdi - the address of the null-terminated buffer to process
processline:
    call parseint
    add %rax, sum
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
# Reads a line from the currently opened file and stores it as a null
# terminated string
#
# Convention: a line includes the eol char if any.
#
# rdi - destination address
# returns: zero if nothing was read, otherwise non zero
readline:
    enter $16, $0
    movq %rdi, -8(%rbp)
    movq %rdi, -16(%rbp)  # remember start of buffer / dest address
.loopreadline:
    movq -8(%rbp), %rdi
    call readc
    test %rax, %rax
    jz .endreadline
    movq -8(%rbp), %rdi
    incq -8(%rbp)
    cmpb $'\n', (%rdi)
    jne .loopreadline
.endreadline:
    movq -8(%rbp), %rdi
    movb $EOS, (%rdi)  # end buffer with zero byte
    mov $0, %rax
    mov -16(%rbp), %rdi
    mov (%rdi), %al  # first read byte is stored in %rax, zero if no read
    leave
    ret

##
# rdi - destination address
# returns: the number of bytes read
readc:
    movq %rdi, %rsi  # store input to %rsi
    movq $SYS_READ, %rax  # 0x00 syscall is read()
    movq file, %rdi
    movq $1, %rdx
    syscall
    ret

##
# rdi - the file descriptor to close
close:
    movq $SYS_CLOSE, %rax
    syscall
    ret

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
    mov %rdi, %rax # Set the initial value to print
    mov $10, %r10  # Set our divisor
    mov $'0', %r11 # Ascii offset for numbers
    lea buffer+BUFFER_SIZE, %rdi
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
    ret

##
# rdi - the address of the null-terminated buffer to print
print:
    pushq %rdi
.loopprint:
    cmpb $EOS, (%rsp)
    je .endprint
    movq (%rsp), %rdi
    call putc
    incq (%rsp)
    jmp .loopprint
.endprint:
    leaq eol, %rdi
    call putc
    addq $8, %rsp
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
