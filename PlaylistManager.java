import java.util.Scanner;

class Node {
    String data; // Nombre de la canción
    Node next;

    public Node(String data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    private Node head; // Inicio de la lista enlazada

    public LinkedList() {
        this.head = null;
    }

    // Método para agregar una canción
    public void add(String data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    // Método para eliminar una canción
    public void remove(String data) {
        if (head == null) {
            System.out.println("La lista está vacía.");
            return;
        }

        if (head.data.equals(data)) {
            head = head.next;
            return;
        }

        Node current = head;
        while (current.next != null && !current.next.data.equals(data)) {
            current = current.next;
        }

        if (current.next != null) {
            current.next = current.next.next;
        } else {
            System.out.println(data + " no se encontró en la lista.");
        }
    }

    // Método para buscar una canción
    public boolean search(String data) {
        Node current = head;
        while (current != null) {
            if (current.data.equals(data)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    // Método para mostrar la playlist
    public void display() {
        Node current = head;
        if (current == null) {
            System.out.println("La lista está vacía.");
            return;
        }

        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("None");
    }
}

public class PlaylistManager {
    public static void main(String[] args) {
        LinkedList playlist = new LinkedList();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- Gestión de Listas Musicales ---");
            System.out.println("1. Agregar canción");
            System.out.println("2. Eliminar canción");
            System.out.println("3. Mostrar playlist");
            System.out.println("4. Buscar canción");
            System.out.println("5. Salir");
            System.out.print("Selecciona una opción: ");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Ingresa el nombre de la canción: ");
                    String songToAdd = scanner.nextLine();
                    playlist.add(songToAdd);
                    System.out.println(songToAdd + " se agregó a la playlist.");
                    break;

                case "2":
                    System.out.print("Ingresa el nombre de la canción a eliminar: ");
                    String songToRemove = scanner.nextLine();
                    playlist.remove(songToRemove);
                    break;

                case "3":
                    System.out.println("Playlist actual:");
                    playlist.display();
                    break;

                case "4":
                    System.out.print("Ingresa el nombre de la canción a buscar: ");
                    String songToSearch = scanner.nextLine();
                    if (playlist.search(songToSearch)) {
                        System.out.println(songToSearch + " se encuentra en la playlist.");
                    } else {
                        System.out.println(songToSearch + " no está en la playlist.");
                    }
                    break;

                case "5":
                    System.out.println("¡Hasta luego!");
                    scanner.close();
                    return;

                default:
                    System.out.println("Opción no válida. Inténtelo de nuevo.");
            }
        }
    }
}
