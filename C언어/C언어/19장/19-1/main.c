// �ҽ� ���� - main.c
#include <stdio.h>           // �ý��� ��� ������ ���� ����1
#include "student.h"         // ����� ���� ��� ������ ���� ����2

int main(void)
{
	Student a = { 315, "ȫ�浿" };   // ����ü ���� ����� �ʱ�ȭ

	printf("�й� : %d, �̸� : %s\n", a.num, a.name);  // ����ü ��� ���

	return 0;
}