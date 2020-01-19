SECTION .data

file: db 6, 15, 28, 35, 214, 141, 173, 34, 174, 0
flag: db 110, 108, 122, 110, 125, 103, 124, 109, 108, 19, 76, 64, 79, 23, 87, 91, 0

SECTION .text

global _start

_start:
	mov rcx, 0
	mov rax, 41
L1:	
	mov bl, [file + rcx]	
	xor bl, al
	mov [file + rcx], bl
	mov dl, 3
	mul dl

	add rcx, 1
	cmp rcx, 9
	jne L1

	mov rax, 85
	mov rdi, file
	mov rsi, 493
	syscall

	mov rdi, rax

	mov rax, 0
	push 23
L2:
	mov bl, [flag + rax]
	xor bl, [rsp]

	mov rcx, [rsp]
	add rcx, 1
	mov [rsp], rcx

	push rax

	mov rax, 1
	push rbx
	mov rsi, rsp
	mov rdx, 1
	syscall

	lea rsp, [rsp + 8]

	pop rax
	
	add rax, 1
	cmp rax, 16
	jnz L2

	mov rax, 60
	mov rdi, 0
	syscall
