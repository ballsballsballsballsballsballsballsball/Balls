	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 17
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rax
	.cfi_def_cfa_offset 16
	leaq	L_.str(%rip), %rdi
	callq	_puts
	xorl	%eax, %eax
	popq	%rcx
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"balls\n"


.subsections_via_symbols
