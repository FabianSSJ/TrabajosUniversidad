import java.util.Stack;

public class Analizador_Sintactico {

    // Método para verificar el balanceo de delimitadores (paréntesis, corchetes, llaves)
    public static boolean balancearDelimitadores(String expresion) {
        Stack<Character> pila = new Stack<>();
        for (char c : expresion.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                pila.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (pila.isEmpty()) return false;
                char top = pila.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return pila.isEmpty();
    }

    // Método para validar la disposición de operadores y operandos
    public static boolean validarOperadoresOperandos(String expresion) {
        String operadores = "+-*/";
        boolean ultimoFueOperador = false;
        boolean contieneOperando = false;

        for (char c : expresion.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                contieneOperando = true;
                ultimoFueOperador = false;
            } else if (operadores.indexOf(c) != -1) {
                if (ultimoFueOperador) return false; // Dos operadores consecutivos
                ultimoFueOperador = true;
            } else if (c == '(' || c == ')') {
                continue; // Ignorar paréntesis aquí
            } else {
                return false; // Caracter no reconocido
            }
        }
        // No debe terminar en un operador
        return contieneOperando && !ultimoFueOperador;
    }

    // Método para validar una expresión completa
    public static boolean validar(String expresion) {
        return balancearDelimitadores(expresion) && validarOperadoresOperandos(expresion);
    }

    // Método para realizar pruebas
    public static void pruebas() {
        String[] casos = {
            "((a + b) * c)",
            "5 * (3 + 2)",
            "5 * (3 + 2",
            "a + + b",
            "(a + b) * c)",
            "(a + b) * (c + d)"
        };

        for (String caso : casos) {
            boolean resultado = validar(caso);
            System.out.println("Expresión: " + caso + " - " + (resultado ? "Válida" : "Inválida"));
        }
    }

    public static void main(String[] args) {
        System.out.println("Resultados de las pruebas:");
        pruebas();
    }
}
