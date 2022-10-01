.global _start

.include "src/common/common.s"

.equ MAX_LINE, 0xff
.equ BUFFER_SIZE, MAX_LINE+1
.equ HUGE, 9999

.section .data
p1: .quad HUGE
p2: .quad HUGE
p3: .quad HUGE

.section .bss
file: .quad 0
buffer: .skip BUFFER_SIZE
result_1: .quad 0
result_2: .quad 0

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
    mov file, %rdi
    leaq buffer, %rsi
    call readline
    test %rax, %rax
    jz .endmainloop

    leaq buffer, %rdi
    call processline
    jmp .mainloop
.endmainloop:

    leaq file, %rdi
    call close

    mov result_1, %rdi
    call print_u64
    mov result_2, %rdi
    call print_u64

    movq $SYS_EXIT, %rax
    movq $OK, %rdi
    syscall

##
# rdi - the address of the null-terminated buffer to process
processline:
    call parseint

    cmp p1, %rax
    jle .noinc1
    incq result_1
.noinc1:

    mov p1, %rcx
    add p2, %rcx
    add p3, %rcx

    mov %rax, %rdx
    add p1, %rdx
    add p2, %rdx

    cmp %rcx, %rdx
    jle .noinc2
    incq result_2
.noinc2:

    mov p2, %rcx
    mov %rcx, p3
    mov p1, %rcx
    mov %rcx, p2
    mov %rax, p1
    ret
