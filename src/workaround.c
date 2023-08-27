//
// Created by verdgil on 27.08.23.
//

#include <stdio.h>
#include <signal.h>
#include <setjmp.h>


jmp_buf jump_buffer;

void sigsegv_handler(int signum) {
    printf("Access to memory is not allowed\n");
    longjmp(jump_buffer, 1);
}