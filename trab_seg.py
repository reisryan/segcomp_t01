class CifraVigenere:
    def __init__(self):
        # Aqui eu considero que o usuario digite letras maiusculas ou minusculas 
        self.alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
        self.tamanho_alfabeto = len(self.alfabeto_maiusculo)
    
    def obter_frequencias_idioma(self, idioma):
        # fiz basicamente um dicionario para acessar a frequencia de cada letra nos idiomas portugues e ingles, na pirmeira posicao e referente ao portugues a segunda e para o ingles
        frequencia_letras = {
        'a': [14.63, 8.167],
        'b': [1.04, 1.492],
        'c': [3.88, 2.782],
        'd': [4.99, 4.253],
        'e': [12.57, 12.702],
        'f': [1.02, 2.228],
        'g': [1.30, 2.015],
        'h': [1.28, 6.094],
        'i': [6.18, 6.966],
        'j': [0.40, 0.153],
        'k': [0.02, 0.772],
        'l': [2.78, 4.025],
        'm': [4.74, 2.406],
        'n': [5.05, 6.749],
        'o': [10.73, 7.507],
        'p': [2.52, 1.929],
        'q': [1.20, 0.095],
        'r': [6.53, 5.987],
        's': [7.81, 6.327],
        't': [4.34, 9.056],
        'u': [4.63, 2.758],
        'v': [1.67, 0.978],
        'w': [0.01, 2.360],
        'x': [0.21, 0.150],
        'y': [0.01, 1.974],
        'z': [0.47, 0.074]}
        
        # retorna frequências do idioma especificado
        return {letra: freq[idioma] for letra, freq in frequencia_letras.items()}

    def normalizar_chave(self, chave):
        chave_normalizada = []
        for char in chave:
            if char in self.alfabeto_maiusculo:
                chave_normalizada.append(char)
            elif char in self.alfabeto_minusculo:
                # Aqui eu mudo a chave para maiuscula tambem 
                chave_normalizada.append(char.upper())
            else:
                # E tiro qualquer coisa que n seja letra de "A" ate "Z"
                continue
        return "".join(chave_normalizada)
    
    def cifrar(self, texto_original, chave):
        chave_normalizada = self.normalizar_chave(chave)
        if not chave_normalizada:
            raise ValueError("A chave deve conter pelo menos uma letra do alfabeto")
        
        texto_cifrado = []
        indice_chave = 0  # Índice que só avança para letras
        
        for char_texto in texto_original:
            if char_texto in self.alfabeto_maiusculo:
                char_chave = chave_normalizada[indice_chave % len(chave_normalizada)]
                idx_texto = self.alfabeto_maiusculo.index(char_texto)
                idx_chave = self.alfabeto_maiusculo.index(char_chave)
                idx_cifrado = (idx_texto + idx_chave) % self.tamanho_alfabeto
                texto_cifrado.append(self.alfabeto_maiusculo[idx_cifrado])
                indice_chave += 1  # Avança a chave apenas para letras
                
            elif char_texto in self.alfabeto_minusculo:
                char_chave = chave_normalizada[indice_chave % len(chave_normalizada)]
                idx_texto = self.alfabeto_minusculo.index(char_texto)
                idx_chave = self.alfabeto_maiusculo.index(char_chave)
                idx_cifrado = (idx_texto + idx_chave) % self.tamanho_alfabeto
                texto_cifrado.append(self.alfabeto_minusculo[idx_cifrado])
                indice_chave += 1  # Avança a chave apenas para letras
                
            else:
                # Espaços e pontuação passam sem modificação e sem avançar a chave
                texto_cifrado.append(char_texto)
        
        return "".join(texto_cifrado)
    #aqui é so engenharia reversa, de acordo com a chave e a mensagem criptografada, tamanho e eposicao das letras eu utilizo os lacos para encontrar a letra correspondente  
    def decifrar(self, texto_cifrado, chave):
        chave_normalizada = self.normalizar_chave(chave)
        if not chave_normalizada:
            raise ValueError("A chave deve conter pelo menos uma letra do alfabeto")
        
        texto_decifrado = []
        indice_chave = 0  # Índice que só avança para letras
        
        for char_cifrado in texto_cifrado:
            if char_cifrado in self.alfabeto_maiusculo:
                char_chave = chave_normalizada[indice_chave % len(chave_normalizada)]
                idx_cifrado = self.alfabeto_maiusculo.index(char_cifrado)
                idx_chave = self.alfabeto_maiusculo.index(char_chave)
                idx_decifrado = (idx_cifrado - idx_chave) % self.tamanho_alfabeto
                texto_decifrado.append(self.alfabeto_maiusculo[idx_decifrado])
                indice_chave += 1  # Avança a chave apenas para letras
                
            elif char_cifrado in self.alfabeto_minusculo:
                char_chave = chave_normalizada[indice_chave % len(chave_normalizada)]
                idx_cifrado = self.alfabeto_minusculo.index(char_cifrado)
                idx_chave = self.alfabeto_maiusculo.index(char_chave)
                idx_decifrado = (idx_cifrado - idx_chave) % self.tamanho_alfabeto
                texto_decifrado.append(self.alfabeto_minusculo[idx_decifrado])
                indice_chave += 1  # Avança a chave apenas para letras
            else:
                # Espaços e pontuação passam sem modificação e sem avançar a chave
                texto_decifrado.append(char_cifrado)
        
        return "".join(texto_decifrado)

    def calcular_frequencias_texto(self, texto):
        """
        Calcula as frequências das letras em um texto (apenas letras, ignora outros caracteres)
        Retorna um dicionário com as frequências percentuais
        """
        # Contador para cada letra (apenas minúsculas)
        contador = {letra: 0 for letra in self.alfabeto_minusculo}
        total_letras = 0
        
        # Conta as ocorrências de cada letra
        for char in texto:
            if char.lower() in self.alfabeto_minusculo:
                contador[char.lower()] += 1
                total_letras += 1
        
        # Calcula as frequências percentuais
        if total_letras == 0:
            return {letra: 0 for letra in self.alfabeto_minusculo}
        
        frequencias = {}
        for letra, count in contador.items():
            frequencias[letra] = (count / total_letras) * 100
        
        return frequencias

    def _indice_coincidencia(self, texto):
        """
        Calcula o Índice de Coincidência para um texto
        """
        contador = [0] * 26
        total_letras = 0
        
        for char in texto:
            if char.lower() in self.alfabeto_minusculo:
                idx = ord(char.lower()) - ord('a')
                contador[idx] += 1
                total_letras += 1
        
        if total_letras < 2:
            return 0.0
        
        # Fórmula do IC: Σ(ni * (ni-1)) / (N * (N-1))
        soma = sum(n * (n - 1) for n in contador)
        ic = soma / (total_letras * (total_letras - 1))
        return ic

    def encontrar_tamanho_chave(self, texto_cifrado, max_tamanho=15):
        """
        Encontra o provável tamanho da chave usando o Índice de Coincidência
        Respeitando que a chave avança apenas nas letras (comportamento clássico)
        """
        melhor_tamanho = 1
        melhor_ic_medio = 0
        
        # Extrai apenas as letras do texto preservando suas posições relativas
        letras_apenas = []
        posicoes_letras = []
        
        for i, char in enumerate(texto_cifrado):
            if char.lower() in self.alfabeto_minusculo:
                letras_apenas.append(char)
                posicoes_letras.append(i)
        
        if len(letras_apenas) < 10:  # Texto muito pequeno
            return 1
        
        for tamanho in range(1, min(max_tamanho + 1, len(letras_apenas))):
            # Divide as letras em grupos baseados na posição da letra no keystream (não na posição no texto)
            grupos = [''] * tamanho
            
            for idx_letra, letra in enumerate(letras_apenas):
                # A posição no keystream é a posição da letra entre as letras
                grupos[idx_letra % tamanho] += letra
            
            # Calcula IC médio para este tamanho
            ic_total = 0
            grupos_validos = 0
            
            for grupo in grupos:
                if len(grupo) > 1:
                    ic_total += self._indice_coincidencia(grupo)
                    grupos_validos += 1
            
            if grupos_validos > 0:
                ic_medio = ic_total / grupos_validos
                
                # Para português/inglês, IC próximo a 0.065-0.07 indica texto natural
                if ic_medio > melhor_ic_medio:
                    melhor_ic_medio = ic_medio
                    melhor_tamanho = tamanho
        
        return melhor_tamanho

    def _melhor_deslocamento_chi2(self, grupo, freq_idioma):
        """
        Encontra o melhor deslocamento usando teste qui-quadrado
        """
        if not grupo:
            return 0
            
        melhor_deslocamento = 0
        melhor_chi2 = float('inf')
        
        for deslocamento in range(26):
            # Decifra o grupo com este deslocamento
            grupo_decifrado = ''
            for char in grupo:
                if char in self.alfabeto_maiusculo:
                    idx = (self.alfabeto_maiusculo.index(char) - deslocamento) % 26
                    grupo_decifrado += self.alfabeto_maiusculo[idx]
                else:
                    idx = (self.alfabeto_minusculo.index(char) - deslocamento) % 26
                    grupo_decifrado += self.alfabeto_minusculo[idx]
            
            # Calcula frequências do grupo decifrado
            freq_grupo = self.calcular_frequencias_texto(grupo_decifrado)
            
            # Calcula qui-quadrado
            chi2 = 0.0
            for letra in self.alfabeto_minusculo:
                observado = freq_grupo[letra]
                esperado = freq_idioma.get(letra, 0.1)  # Evita divisão por zero
                if esperado > 0:
                    chi2 += ((observado - esperado) ** 2) / esperado
            
            if chi2 < melhor_chi2:
                melhor_chi2 = chi2
                melhor_deslocamento = deslocamento
        
        return melhor_deslocamento

    def atacar_por_frequencia(self, texto_cifrado, idioma=0):
        """
        Realiza o ataque por análise de frequência para descobrir a chave
        idioma: 0 para português, 1 para inglês
        Retorna a chave encontrada e o texto decifrado
        """
        print(f"\n=== INICIANDO ATAQUE POR FREQUÊNCIA ===")
        print(f"Idioma: {'Português' if idioma == 0 else 'Inglês'}")
        
        # Obter frequências de referência do idioma
        frequencias_idioma = self.obter_frequencias_idioma(idioma)
        
        # Extrair apenas letras do texto cifrado
        letras_apenas = []
        for char in texto_cifrado:
            if char in self.alfabeto_maiusculo or char in self.alfabeto_minusculo:
                letras_apenas.append(char)
        
        print(f"Total de letras no texto: {len(letras_apenas)}")
        
        if len(letras_apenas) < 4:
            print("Texto muito pequeno para análise!")
            return "A", texto_cifrado
        
        # Testar diferentes tamanhos de chave (1 a min(15, len(letras)/2))
        max_teste = min(15, len(letras_apenas) // 2)
        melhor_chave = ""
        melhor_score = float('inf')
        melhor_tamanho = 1
        
        for tamanho_teste in range(1, max_teste + 1):
            # Dividir letras em grupos
            grupos = [[] for _ in range(tamanho_teste)]
            for i, letra in enumerate(letras_apenas):
                grupos[i % tamanho_teste].append(letra)
            
            # Para cada grupo, encontrar melhor deslocamento
            chave_teste = []
            score_total = 0
            
            for grupo in grupos:
                if not grupo:
                    chave_teste.append('A')
                    continue
                
                melhor_deslocamento = 0
                melhor_chi2 = float('inf')
                
                # Testar todos os deslocamentos possíveis
                for desl in range(26):
                    # Decifrar grupo com este deslocamento
                    grupo_decifrado = []
                    for char in grupo:
                        if char in self.alfabeto_maiusculo:
                            idx = (self.alfabeto_maiusculo.index(char) - desl) % 26
                            grupo_decifrado.append(self.alfabeto_maiusculo[idx].lower())
                        else:
                            idx = (self.alfabeto_minusculo.index(char) - desl) % 26
                            grupo_decifrado.append(self.alfabeto_minusculo[idx])
                    
                    # Calcular chi-quadrado para este grupo
                    freq_grupo = self.calcular_frequencias_texto(''.join(grupo_decifrado))
                    chi2 = 0.0
                    
                    for letra in self.alfabeto_minusculo:
                        observado = freq_grupo.get(letra, 0)
                        esperado = frequencias_idioma.get(letra, 0.1)
                        if esperado > 0:
                            chi2 += ((observado - esperado) ** 2) / esperado
                    
                    if chi2 < melhor_chi2:
                        melhor_chi2 = chi2
                        melhor_deslocamento = desl
                
                chave_teste.append(self.alfabeto_maiusculo[melhor_deslocamento])
                score_total += melhor_chi2
            
            # Calcular score médio para este tamanho de chave
            score_medio = score_total / len(grupos) if grupos else float('inf')
            
            print(f"Tamanho {tamanho_teste}: chave={''.join(chave_teste)}, score={score_medio:.2f}")
            
            # Manter a melhor chave (menor chi-quadrado é melhor)
            if score_medio < melhor_score:
                melhor_score = score_medio
                melhor_chave = ''.join(chave_teste)
                melhor_tamanho = tamanho_teste
        
        print(f"\nTamanho provável da chave: {melhor_tamanho}")
        print(f"=== RESULTADO DO ATAQUE ===")
        
        # Decifrar o texto completo com a melhor chave encontrada
        texto_decifrado = self.decifrar(texto_cifrado, melhor_chave)
        
        return melhor_chave, texto_decifrado

if __name__ == "__main__":
    cifrador = CifraVigenere()
    
    print("=" * 60)
    print("CIFRA DE VIGENÈRE - TRABALHO DE SEGURANÇA")
    print("=" * 60)
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Parte I: Cifrar/Decifrar mensagem")
        print("2 - Parte II: Ataque por análise de frequência")
        print("3 - Sair")
        
        opcao = input("\nEscolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == "1":
            # PARTE I: Cifrador/Decifrador
            print("\n=== PARTE I: CIFRADOR/DECIFRADOR ===")
            texto = input("Digite a mensagem que deseja criptografar: ")
            chave = input("Digite a senha para a criptografia: ")
            
            try:
                print(f"\nMensagem original: {texto}")
                print(f"Senha utilizada: {chave}")
                
                # Cifrar
                texto_cifrado = cifrador.cifrar(texto, chave)
                print(f"Mensagem criptografada: {texto_cifrado}")
                
                # Decifrar (teste)
                texto_decifrado = cifrador.decifrar(texto_cifrado, chave)
                print(f"Texto decifrado (teste): {texto_decifrado}")
                
            except Exception as e:
                print(f"Erro: {e}")
                
        elif opcao == "2":
            # PARTE II: Ataque por análise de frequência
            print("\n=== PARTE II: ATAQUE POR ANÁLISE DE FREQUÊNCIA ===")
            print("Este módulo tentará recuperar a senha de mensagens cifradas")
            print("usando análise estatística das frequências de letras.\n")
            
            print("Escolha o idioma da mensagem:")
            print("1 - Português")
            print("2 - Inglês")
            
            idioma_opcao = input("Digite 1 ou 2: ").strip()
            if idioma_opcao not in ["1", "2"]:
                print("Opção inválida!")
                continue
                
            idioma = 0 if idioma_opcao == "1" else 1
            idioma_nome = "Português" if idioma == 0 else "Inglês"
            
            texto_cifrado = input(f"\nDigite a mensagem cifrada em {idioma_nome}: ")
            
            if not texto_cifrado.strip():
                print("Mensagem não pode estar vazia!")
                continue
            
            try:
                chave_encontrada, texto_decifrado = cifrador.atacar_por_frequencia(texto_cifrado, idioma)
                
                print(f"Chave recuperada: {chave_encontrada}")
                print(f"Texto decifrado: {texto_decifrado}")
                
                continuar = input("\nDeseja atacar outra mensagem? (s/n): ").strip().lower()
                if continuar != 's':
                    print("Retornando ao menu principal...")
                    
            except Exception as e:
                print(f"Erro durante o ataque: {e}")
                
        elif opcao == "3":
            print("\nSaindo do programa...")
            break
            
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")