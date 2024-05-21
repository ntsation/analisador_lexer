import re

patterns = [
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  
    (r'(if|else|for|while|return)\b', 'KEYWORD'),  
    (r'[\+\-\*/=]', 'OPERATOR'),  
    (r'[(),;{}]', 'SYMBOL'),  
    (r'\d+', 'NUMBER'),  
    (r'//.*|/\*[\s\S]*?\*/', ''),  
    (r'\s+', ''),  
]

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
    return tokens

code = """
int main() {
    // Programa de exemplo
    int x = 5;
    return 0;
}
"""
print(lexer(code))