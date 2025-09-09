# 🔐 Cifra de Vigenère - Implementação e Criptoanálise

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completo-brightgreen.svg)]()

## 👥 Equipe

- **Johnatan Sousa Ramos** - 190089911
- **Kaillany Pereira Santos** - 211055488  
- **Ryan Reis Fontenele** - 211036132

*Universidade de Brasília (UnB) - Departamento de Ciência da Computação*  
*CIC0201 - Segurança Computacional*

---

## 📝 Descrição

Este projeto implementa a **Cifra de Vigenère**, um sistema de criptografia polialfabética clássica, desenvolvido em Python puro (sem bibliotecas externas de criptografia). A implementação inclui tanto o sistema de cifragem/decifragem quanto um módulo de criptoanálise baseado em análise de frequência.

### 🎯 Objetivos

- **Parte I**: Implementar cifrador/decifrador da Cifra de Vigenère
- **Parte II**: Desenvolver ataque por análise de frequência para recuperação de chaves

---

## 🔍 O que é a Cifra de Vigenère?

A Cifra de Vigenère é um método de criptografia que utiliza uma **palavra-chave** para realizar múltiplos deslocamentos no alfabeto. Diferentemente da Cifra de César (deslocamento fixo), cada letra do texto é deslocada por um valor diferente baseado na chave.

### 📐 Funcionamento Matemático

**Cifragem:**
```
C = (P + K) mod 26
```

**Decifragem:**
```
P = (C - K) mod 26
```

Onde:
- `C` = caractere cifrado
- `P` = caractere original  
- `K` = caractere da chave
- `mod 26` = operação módulo (tamanho do alfabeto)

### 💡 Exemplo Prático

```
Texto Original: "HELLO WORLD"
Chave:          "KEY"
Chave Expandida: "KEYKE YKEYK"
Texto Cifrado:  "RIJVS UYVJN"
```

---

## 🚀 Funcionalidades

### ✅ Parte I - Cifrador/Decifrador
- Cifragem de textos com chave fornecida
- Decifragem de textos cifrados
- Preservação de espaços, pontuação e case-sensitive
- Comportamento clássico: chave avança apenas para letras

### 🔓 Parte II - Ataque Criptanalítico
- **Análise de Frequência**: Baseada em distribuições estatísticas de português e inglês
- **Índice de Coincidência**: Para estimativa do tamanho da chave
- **Teste Qui-Quadrado (χ²)**: Para encontrar o melhor deslocamento por grupo
- **Recuperação Automática**: Encontra a chave mais provável e decifra o texto

---

## 🛠️ Como Usar

### Executar o Programa
```bash
python3 trab_seg.py
```

### Menu Principal
```
=== MENU PRINCIPAL ===
1 - Parte I: Cifrar/Decifrar mensagem
2 - Parte II: Ataque por análise de frequência  
3 - Sair
```


## 📊 Algoritmo de Ataque

### 🔍 Estratégia Principal
1. **Extração de Letras**: Remove espaços e pontuação
2. **Teste de Tamanhos**: Testa chaves de tamanho 1-15
3. **Agrupamento**: Divide letras em grupos por posição (i % k)
4. **Análise χ²**: Para cada grupo, encontra o melhor deslocamento
5. **Seleção Ótima**: Escolhe a chave com menor score total
6. **Decifragem**: Aplica a chave encontrada ao texto original

### 📈 Métricas Utilizadas
- **Índice de Coincidência**: ~0.065-0.07 (texto natural) vs ~0.038 (aleatório)
- **Teste Qui-Quadrado**: Compara frequências observadas vs esperadas
- **Frequências de Referência**: Português e inglês baseadas em corpus linguísticos

---

### ⚡ Complexidade
- **Temporal**: O(k × n × 26)
  - `k`: tamanho máximo da chave (15)
  - `n`: número de letras no texto
  - `26`: deslocamentos testados por grupo

---


## 📚 Referências

- [Frequência de Letras - Wikipedia](https://pt.wikipedia.org/wiki/Frequência_de_letras)
- [Apresentação Slides Canvas] (https://www.canva.com/design/DAGycv9JdhY/1cOCJzrRn71Ep6JrL8Ft-Q/edit?utm_content=DAGycv9JdhY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte da disciplina de Segurança Computacional da UnB.

---

⭐ **Se este projeto foi útil, considere dar uma estrela!**
