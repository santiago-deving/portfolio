#include <iostream>

using namespace std;
int a;

int main(){
    cout << "HELLO WORLD!\nDigite um número: " << endl;
    cin >> a;
    cout << "O numero digitado foi: " << a << endl;
    if (a < 0)
    {
        cout << "Numero negativo!" << endl;
    }
    
    return 0;
}