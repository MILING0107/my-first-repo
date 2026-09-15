; 汇编测试代码：打印字符串，MASM/TASM 均支持

STACKSG   SEGMENT STACK

        DW 512 DUP(?)  ; 定义栈区，512个字单元

STACKSG   ENDS
DATA    SEGMENT

; 要打印的字符串，0DH(回车)、0AH(换行)、24H($)是DOS打印结束标识

MSG     DB 'Hello Assembly!',0DH,0AH,'$'

DATA    ENDS

CODE    SEGMENT

ASSUME  CS:CODE,DS:DATA,SS:STACKSG  ; 关联段寄存器与段名START:  ; 程序入口
START:
        MOV AX,DATA

        MOV DS,AX        ; 初始化数据段寄存器（必须步骤）

        LEA DX,MSG       ; 取字符串首地址送入DX

        MOV AH,09H       ; DOS中断功能号：09H=打印字符串

        INT 21H          ; 调用DOS 21H中断，执行打印

        MOV AH,4CH       ; DOS中断功能号：4CH=程序退出

        INT 21H          ; 调用中断，返回DOS系统

CODE    ENDS

        END START        ; 程序结束，指定入口为START