#include <iostream>
#include <string>

constexpr uintptr_t XREF_KEY = 0x80908090;
constexpr uint8_t   XOR_KEY  = 0x80;

volatile const char* password = "\xd5\xf0\xd8\xdf\xe9\xd3\xdf\xc1\xdf\xee\xb1\xe3\xb3\xdf\xf0\xb4\xeb\xf2\xdf\xd7\xe9\xd4\xe8\xdf\xce\xef\xf5\xdf\xc6\xec\xe1\xf7\xf3\xdf\xc1\xd4\xdf\xe1\xee\xe4\xdf\xd4\xdf\xe1\xec\xec";
volatile const char* right = "\xf9\xf4\xe3\xf4\xe6\xfb\xc7\xb0\xb0\xc4\xdf\xca\xb0\xc2\xdf\xd0\xc1\xd3\xd3\xd7\xcf\xd2\xc4\xdf\xc8\xc5\xd2\xc5\xfd";
volatile const char* wrong = "\xf9\xf4\xe3\xf4\xe6\xfb\xc7\xb0\xb0\xc4\xdf\xca\xb0\xc2\xdf\xd5\xdf\xc6\xb4\xb1\xc9\xb3\xc4\xc4\xfd";

volatile uintptr_t pass_xref = (uintptr_t)password ^ XREF_KEY;
volatile uintptr_t right_xref = (uintptr_t)right ^ XREF_KEY;
volatile uintptr_t wrong_xref = (uintptr_t)wrong ^ XREF_KEY;

char* stk_decrypt(const char* ptr) {
	const volatile auto sz = strlen(ptr);
	volatile auto str = new char[sz+1];
	for (size_t i = 0; i < sz; i++) {
		str[i] = ptr[i] ^ 0x80;
	}
	str[sz] = 0;
	return str;
}

bool stk_strcmp(const char* ptr, const char* str) {
	const volatile auto sz = strlen(ptr);
	const volatile auto szz = strlen(str);
	const volatile auto minsz = sz > szz ? szz : sz;
	volatile auto wrong = false;
	for (size_t i = 0; i < minsz; i++) {
		if (ptr[i] != str[i])
			wrong = true;
	}
	return !wrong && sz == szz;
}

int main() {
	std::cout << "STK ULTRA STK PASSWORD STK PROTECTED STK PASSWORD STK STORAGE\n";
	std::cout << "ENTER A PASSWORD TO SEE IF ITS IN STK DATABASE STACK ON STK VM ON STK DATACENTERS\n";
	std::cout << "STK PASS: ";
	std::string pas;
	std::cin >> pas;
	volatile auto dec_pass = stk_decrypt(reinterpret_cast<const char*>(pass_xref ^ XREF_KEY));
	volatile auto dec_right = stk_decrypt(reinterpret_cast<const char*>(right_xref ^ XREF_KEY));
	volatile auto dec_wrong = stk_decrypt(reinterpret_cast<const char*>(wrong_xref ^ XREF_KEY));
	volatile auto pass_chk = stk_strcmp(dec_pass, pas.c_str());
	delete[] dec_pass;
	volatile auto right_chk = stk_strcmp(dec_right, pas.c_str());
	delete[] dec_right;
	volatile auto wrong_chk = stk_strcmp(dec_wrong, pas.c_str());
	delete[] dec_wrong;
	if (pass_chk != (right_chk ^ wrong_chk) && (pass_chk+3^0x4) == 0) {
		volatile auto decc_right = stk_decrypt(reinterpret_cast<const char*>(right_xref ^ XREF_KEY));
		std::cout << decc_right;
	} else
	{
		volatile auto decc_wrong = stk_decrypt(reinterpret_cast<const char*>(wrong_xref ^ XREF_KEY));
		std::cout << decc_wrong;
	}
	return 0;
}

