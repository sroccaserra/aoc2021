.global _start

.include "src/common/common.s"

.equ MAX_LINE, 0xff
.equ BUFFER_SIZE, MAX_LINE+1
.equ HUGE, 9999

.section .data

.section .bss
file: .quad 0
buffer: .skip BUFFER_SIZE

hpos: .quad 0
depth_1: .quad 0
depth_2: .quad 0
aim: .quad 0

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

    mov hpos, %rax
    mulq depth_1
    mov %rax, %rdi
    call print_u64

    mov hpos, %rax
    mulq depth_2
    mov %rax, %rdi
    call print_u64

    movq $SYS_EXIT, %rax
    movq $OK, %rdi
    syscall

##
# rdi - the address of the null-terminated buffer to process
processline:
    enter $16, $0
    movb (%rdi), %cl
    movb %cl, -8(%rbp)  # Set first char of command to first local var byte
    movb $' ', %al  # For upcoming repne. %rdi is already set at the start
    repne scasb  # Advance %rdi to next space
    call parseint
    mov %rax, %rdi
    cmpb $'f', -8(%rbp)
    jne .noforward
    call forward
.noforward:
    cmpb $'u', -8(%rbp)
    jne .noup
    call up
.noup:
    cmpb $'d', -8(%rbp)
    jne .nodown
    call down
.nodown:
    leave
    ret

##
# rdi - the value for the forward command
forward:
    add %rdi, hpos
    mov aim, %rax
    mul %rdi
    add %rax, depth_2
    ret

##
# rdi - the value for the up command
up:
    sub %rdi, depth_1
    sub %rdi, aim
    ret

##
# rdi - the value for the down command
down:
    add %rdi, depth_1
    add %rdi, aim
    ret
