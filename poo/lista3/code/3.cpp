/**
 * @file 3.cpp
 * @brief Exemplo de uso da estrutura std::set em C++
 *
 * Este programa demonstra como usar um std::set para armazenar valores únicos.
 * O conjunto armazena nomes sem duplicatas e permite inserção, exibição
 * e busca de elementos.
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <set>
#include <string>

int main() {
  /* Declaração do conjunto para armazenar nomes */
  std::set<std::string> nomes;

  /* Inserindo elementos no conjunto */
  nomes.insert("Alice");
  nomes.insert("Bob");
  nomes.insert("Charlie");
  nomes.insert("Alice"); /* Inserção duplicada (ignorada pelo set) */

  /* Exibindo todos os elementos do conjunto */
  std::cout << "Conteúdo do conjunto:\n";
  for (std::set<std::string>::iterator it = nomes.begin(); it != nomes.end();
       ++it)
    std::cout << *it << '\n';

  /* Busca por uma chave no set */
  std::string chave = "Alice";
  if (nomes.find(chave) != nomes.end())
    std::cout << chave << " está no conjunto.\n";
  else std::cout << chave << " não está no conjunto.\n";

  return 0;
}
