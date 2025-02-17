/**
 * @file 2.cpp
 * @brief Exemplo de uso da estrutura std::multimap em C++
 *
 * Este programa demonstra como usar um std::multimap para armazenar pares
 * chave-valor, onde a chave é uma string (nome) e o valor é um inteiro (idade).
 * Diferente de std::map, std::multimap permite múltiplos valores para a mesma
 * chave. Ele permite inserir, exibir e buscar elementos no multimap.
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <map>
#include <string>

int main() {
  /* Declaração do multimap para armazenar nomes e idades */
  std::multimap<std::string, int> dados;

  /* Inserindo elementos no multimap */
  dados.insert(std::make_pair("Alice", 25));
  dados.insert(std::make_pair("Bob", 30));
  dados.insert(std::make_pair("Charlie", 22));
  dados.insert(std::make_pair("Alice", 28)); /* Alice aparece duas vezes */

  /* Exibindo todos os elementos do multimap */
  std::cout << "Conteúdo do multimap:\n";
  for (std::multimap<std::string, int>::iterator it = dados.begin();
       it != dados.end(); ++it)
    std::cout << it->first << " -> " << it->second << '\n';

  /* Busca por uma chave no multimap */
  std::string chave = "Alice";
  std::pair<std::multimap<std::string, int>::iterator,
            std::multimap<std::string, int>::iterator>
    faixa = dados.equal_range(chave);

  if (faixa.first != dados.end() && faixa.first->first == chave) {
    std::cout << chave << " tem as seguintes idades: ";
    for (std::multimap<std::string, int>::iterator it = faixa.first;
         it != faixa.second; ++it)
      std::cout << it->second << " ";
    std::cout << "\n";
  } else std::cout << "Nome não encontrado no multimap.\n";

  return 0;
}
