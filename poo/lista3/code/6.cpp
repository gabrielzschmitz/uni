/**
 * @file 6.cpp
 * @brief Exemplo de uso da estrutura std::queue em C++
 *
 * Este programa demonstra como usar um std::queue para armazenar e manipular
 * uma fila de nomes. A fila segue a ordem FIFO (First In, First Out),
 * permitindo inserção (push), remoção (pop) e acesso ao primeiro e último
 * elemento (front e back).
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <queue>
#include <string>

int main() {
  /* Declaração da fila para armazenar nomes */
  std::queue<std::string> fila;

  /* Inserindo elementos na fila */
  fila.push("Alice");
  fila.push("Bob");
  fila.push("Charlie");

  /* Exibindo o elemento na frente e atrás da fila */
  if (!fila.empty()) {
    std::cout << "Primeiro da fila: " << fila.front() << '\n';
    std::cout << "Último da fila: " << fila.back() << '\n';
  }

  /* Removendo elementos da fila */
  std::cout << "Atendendo os elementos da fila:\n";
  while (!fila.empty()) {
    std::cout << fila.front() << '\n';
    fila.pop();
  }

  /* Verificando se a fila está vazia */
  if (fila.empty()) std::cout << "A fila está vazia.\n";

  return 0;
}
