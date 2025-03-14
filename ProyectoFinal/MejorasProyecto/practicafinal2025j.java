import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Libro {
    private String titulo;
    private String autor;
    private String isbn;
    private boolean disponible;

    public Libro(String titulo, String autor, String isbn) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.disponible = true;
    }

    public static Libro agregar(Scanner scanner) {
        System.out.print("Título: ");
        String titulo = scanner.nextLine().trim();
        System.out.print("Autor: ");
        String autor = scanner.nextLine().trim();
        String isbn;
        while (true) {
            System.out.print("ISBN: ");
            isbn = scanner.nextLine().trim();
            if (!isbn.isEmpty()) {
                break;
            }
            System.out.println("Error: El ISBN no puede estar vacío.");
        }
        return new Libro(titulo, autor, isbn);
    }

    public void prestar() {
        if (this.disponible) {
            this.disponible = false;
            System.out.println("Libro \"" + this.titulo + "\" prestado con éxito.");
        } else {
            System.out.println("El libro \"" + this.titulo + "\" ya está prestado.");
        }
    }

    public void devolver() {
        if (!this.disponible) {
            this.disponible = true;
            System.out.println("Libro \"" + this.titulo + "\" devuelto con éxito.");
        } else {
            System.out.println("El libro \"" + this.titulo + "\" ya estaba disponible.");
        }
    }

    public String mostrar() {
        String estado = this.disponible ? "Sí" : "No";
        return "- " + this.titulo + " (" + this.autor + ") - ISBN: " + this.isbn + " - Disponible: " + estado;
    }

    public String buscar() {
        String estado = this.disponible ? "Sí" : "No";
        return this.titulo + " (" + this.autor + ") - ISBN: " + this.isbn + " - Disponible: " + estado;
    }

    public String getIsbn() {
        return this.isbn;
    }
}

public class Main {
    public static void main(String[] args) {
        List<Libro> libros = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nBienvenido al Sistema de Gestión de Biblioteca");
            System.out.println("1. Agregar libro");
            System.out.println("2. Prestar libro");
            System.out.println("3. Devolver libro");
            System.out.println("4. Mostrar libros");
            System.out.println("5. Buscar libro");
            System.out.println("6. Salir");

            System.out.print("Elige una opción: ");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "1":
                    Libro nuevoLibro = Libro.agregar(scanner);
                    libros.add(nuevoLibro);
                    System.out.println("Libro \"" + nuevoLibro.mostrar() + "\" agregado con éxito.");
                    break;
                case "2":
                    System.out.print("ISBN del libro a prestar: ");
                    String isbnPrestar = scanner.nextLine();
                    Libro libroPrestar = buscarLibroPorIsbn(libros, isbnPrestar);
                    if (libroPrestar != null) {
                        libroPrestar.prestar();
                    } else {
                        System.out.println("Libro no encontrado.");
                    }
                    break;
                case "3":
                    System.out.print("ISBN del libro a devolver: ");
                    String isbnDevolver = scanner.nextLine();
                    Libro libroDevolver = buscarLibroPorIsbn(libros, isbnDevolver);
                    if (libroDevolver != null) {
                        libroDevolver.devolver();
                    } else {
                        System.out.println("Libro no encontrado.");
                    }
                    break;
                case "4":
                    if (libros.isEmpty()) {
                        System.out.println("No hay libros en la biblioteca.");
                    } else {
                        for (Libro libro : libros) {
                            System.out.println(libro.mostrar());
                        }
                    }
                    break;
                case "5":
                    System.out.print("ISBN del libro a buscar: ");
                    String isbnBuscar = scanner.nextLine();
                    Libro libroBuscar = buscarLibroPorIsbn(libros, isbnBuscar);
                    if (libroBuscar != null) {
                        System.out.println(libroBuscar.buscar());
                    } else {
                        System.out.println("Libro no encontrado.");
                    }
                    break;
                case "6":
                    System.out.println("Saliendo del sistema...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        }
    }

    private static Libro buscarLibroPorIsbn(List<Libro> libros, String isbn) {
        for (Libro libro : libros) {
            if (libro.getIsbn().equals(isbn)) {
                return libro;
            }
        }
        return null;
    }
}