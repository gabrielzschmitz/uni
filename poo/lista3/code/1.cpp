/**
 * @file 1.cpp
 * @brief Exemplo de uso da estrutura std::map em C++
 *
 * Este programa demonstra como usar um std::map para armazenar pares
 * chave-valor, onde a chave é uma string (nome) e o valor é um inteiro (idade).
 * Ele permite inserir, exibir e buscar elementos no mapa.
 *
 * @author Gabriel dos Santos Schmitz
 * @date 17-02-2025
 */

#include <iostream>
#include <map>
#include <string>

int main() {
  /* Declaração do mapa para armazenar nomes e idades */
  std::map<std::string, int> dados;

  /* Inserindo elementos no mapa */
  dados["Alice"] = 25;
  dados["Bob"] = 30;
  dados["Charlie"] = 22;

  /* Exibindo todos os elementos do mapa */
  std::cout << "Conteúdo do mapa:\n";
  for (std::map<std::string, int>::iterator it = dados.begin();
       it != dados.end(); ++it)
    std::cout << it->first << " -> " << it->second << '\n';

  /* Busca por uma chave no map */
  std::string chave = "Alice";
  std::map<std::string, int>::iterator it = dados.find(chave);
  if (it != dados.end())
    std::cout << chave << " tem " << it->second << " anos.\n";
  else std::cout << "Nome não encontrado no mapa.\n";

  return 0;
}
