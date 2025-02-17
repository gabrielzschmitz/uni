/**
 * @file 5.cpp
 * @brief Exemplo de uso da estrutura std::stack em C++
 *
 * Este programa demonstra como usar um std::stack para armazenar e manipular
 * uma pilha de nomes. A pilha segue a ordem LIFO (Last In, First Out),
 * permitindo inserção (push), remoção (pop) e exibição do elemento no topo
 * (top).
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <stack>
#include <string>

int main() {
  /* Declaração da pilha para armazenar nomes */
  std::stack<std::string> pilha;

  /* Inserindo elementos na pilha */
  pilha.push("Alice");
  pilha.push("Bob");
  pilha.push("Charlie");

  /* Exibindo o elemento no topo da pilha */
  if (!pilha.empty())
    std::cout << "Elemento no topo da pilha: " << pilha.top() << '\n';

  /* Removendo elementos da pilha */
  std::cout << "Removendo elementos da pilha:\n";
  while (!pilha.empty()) {
    std::cout << pilha.top() << '\n';
    pilha.pop();
  }

  /* Verificando se a pilha está vazia */
  if (pilha.empty()) std::cout << "A pilha está vazia.\n";

  return 0;
}
