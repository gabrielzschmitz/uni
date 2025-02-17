/**
 * @file 7.cpp
 * @brief Exemplo de uso da estrutura std::priority_queue em C++
 *
 * Este programa demonstra como usar um std::priority_queue para armazenar e
 * processar uma fila de prioridades de idades. Os elementos com maior valor têm
 * maior prioridade e são removidos primeiro.
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <queue>

int main() {
  /* Declaração da fila de prioridade para armazenar idades */
  std::priority_queue<int> fila_prioridade;

  /* Inserindo elementos na fila de prioridade */
  fila_prioridade.push(25);
  fila_prioridade.push(30);
  fila_prioridade.push(22);

  /* Exibindo e removendo os elementos da fila de prioridade */
  std::cout << "Processando a fila de prioridade:\n";
  while (!fila_prioridade.empty()) {
    std::cout << fila_prioridade.top() << '\n';
    fila_prioridade.pop();
  }

  /* Verificando se a fila está vazia */
  if (fila_prioridade.empty())
    std::cout << "A fila de prioridade está vazia.\n";

  return 0;
}
