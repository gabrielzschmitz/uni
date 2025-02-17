/**
 * @file 4.cpp
 * @brief Exemplo de uso da estrutura std::multiset em C++
 *
 * Este programa demonstra como usar um std::multiset para armazenar valores que
 * podem se repetir. O multiset armazena nomes permitindo duplicatas e permite
 * inserção, exibição e busca de elementos.
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <set>
#include <string>

int main() {
  /* Declaração do multiset para armazenar nomes */
  std::multiset<std::string> nomes;

  /* Inserindo elementos no multiset */
  nomes.insert("Alice");
  nomes.insert("Bob");
  nomes.insert("Charlie");
  nomes.insert("Alice"); /* Inserção duplicada (permitida pelo multiset) */

  /* Exibindo todos os elementos do multiset */
  std::cout << "Conteúdo do multiset:\n";
  for (std::multiset<std::string>::iterator it = nomes.begin();
       it != nomes.end(); ++it)
    std::cout << *it << '\n';

  /* Busca por uma chave no multiset */
  std::string chave = "Alice";
  int count = nomes.count(chave);
  if (count > 0)
    std::cout << chave << " aparece " << count << " vezes no multiset.\n";
  else std::cout << chave << " não está no multiset.\n";

  return 0;
}
