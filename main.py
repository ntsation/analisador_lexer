import re

patterns = [
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificador
    (r'(if|else|for|while|return)\b', 'KEYWORD'),  # Palavras-chave
    (r'[\+\-\*/=<>]', 'OPERATOR'),  # Operadores
    (r'[(),;{}]', 'SYMBOL'),  # Símbolos
    (r'\d+', 'NUMBER'),  # Números
    (r'"(?:\\.|[^"\\])*"', 'STRING'),  # Strings
    (r'//.*', ''),  # Comentários de linha
    (r'/\*[\s\S]*?\*/', ''),  # Comentários de bloco
    (r'\s+', ''),  # Espaços em branco
]

# Exemplo de código


def lexer(code):
    tokens = []
    while code:
        for pattern, token_type in patterns:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                if token_type:
                    tokens.append((value, token_type))
                code = code[len(value):]
                break
        else:
            raise ValueError("Caractere inesperado: {}".format(code[0]))
    return tokens


# Teste
code = """
int main() {
    // Programa de exemplo
    int x = 5;
    if (x > 0) {
        return 1;
    }
    return 0;
}
"""

print(lexer(code))
