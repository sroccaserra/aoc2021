.global _start

.section .data

file:
    .quad 0
s:
    .quad 0, 0, 0, 0, 0, 0, 0, 0

.section .text
_start:
    movq $0x02, %rax  # 0x02 syscall is open()
    # Third value on the stack points to the second argument's null terminated char*
    movq 16(%rsp), %rdi
    movq $0x0, %rsi  # 0x0 is O_RDONLY
    syscall
    movq %rax, file

    movq $0x00, %rax  # 0x00 syscall is read()
    movq file, %rdi
    leaq s, %rsi
    movq $8, %rdx
    syscall

    movq $0x03, %rax  # 0x03 syscall is close()
    movq file, %rdi
    syscall

    movq $0x01, %rax  # 0x01 syscall is write()
    movq $0x1, %rdi  # 0x1 fd is stdout
    leaq s, %rsi
    # Length of the data
    movq $4, %rdx
    syscall

    ### Exit
    movq $0x3c, %rax
    movq $0, %rdi
    # movq filename, %r8
    # movb (%r8), %dil
    # leaq s, %r10
    # movb (%r10), %dil

    syscall
