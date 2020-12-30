package onreadyfyMe;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;

public class Principal {

	public static void main(String[] args) {

		ArrayList<Vehiculo> vehiculos = agregaVehiculo();
		imprimirVehiculos(vehiculos);
		imprimirVehiculoCaroBarato(vehiculos);
		contieneLetraY(vehiculos);
		imprimirVehiculosOrdenadosPrecio(vehiculos);

	}

	// Para modificar rapidamente los datos de entrada dentro de la clase que los
	// utilizara, en el main()
	static ArrayList<Vehiculo> agregaVehiculo() {
		ArrayList<Vehiculo> listaVehiculos = new ArrayList<Vehiculo>();
		Vehiculo auto1 = new Auto("Peugeot", "206", 200000.00, "4");
		Vehiculo moto1 = new Moto("Honda", "Titan", 60000.00, "125cc");
		Vehiculo auto2 = new Auto("Peugeot", "208", 250000.00, "5");
		Vehiculo moto2 = new Moto("Yamaha", "YBR", 80500.50, "160cc");
		listaVehiculos.add(auto1);
		listaVehiculos.add(moto1);
		listaVehiculos.add(auto2);
		listaVehiculos.add(moto2);
		return listaVehiculos;
	}

	// El algoritmo usado para la impresión no tiene que depender de la cantidad, modelo o tipo de vehículo.
	public static void imprimirVehiculos(ArrayList<Vehiculo> vehiculos) {
		for (Vehiculo vehiculo : vehiculos) {
			vehiculo.mostrarTodosDatos();
		}
		System.out.println("=============================");
	}

	public static void imprimirVehiculoCaroBarato(ArrayList<Vehiculo> vehiculos) {
		double precioMasCaro = 0;
		String autoMasCaro = null;
		double precioMasBarato = 0;
		String autoMasBarato = null;
		// Busca Vehiculo mas caro
		for (Vehiculo vehiculo : vehiculos) {
			if (vehiculo.getPrecio() > precioMasCaro) {
				precioMasCaro = vehiculo.getPrecio();
				autoMasCaro = vehiculo.mostrarMarcaModelo();
			}
		}

		// Para no tener que asignar en linea de codigo un valor de inicio en la variable precioMasBarato
		precioMasBarato = precioMasCaro;

		// Busca Vehiculo mas barato
		for (Vehiculo vehiculo : vehiculos) {
			if (vehiculo.getPrecio() < precioMasBarato) {
				precioMasBarato = vehiculo.getPrecio();
				autoMasBarato = vehiculo.mostrarMarcaModelo();
			}
		}
		System.out.println("Vehículo más caro: " + autoMasCaro);
		System.out.println("Vehículo más barato: " + autoMasBarato);
	}

	public static void contieneLetraY(ArrayList<Vehiculo> vehiculos) {
		DecimalFormat formatea = new DecimalFormat("###,###.00");
		for (Vehiculo vehiculo : vehiculos) {
			if (vehiculo.getModelo().contains("Y")) {
				System.out.println("Vehículo que contiene en el modelo la letra ‘Y’: " + vehiculo.mostrarMarcaModelo()
						+ " $" + formatea.format(vehiculo.getPrecio()));
			}
		}
		System.out.println("=============================");
	}

	public static void imprimirVehiculosOrdenadosPrecio(ArrayList<Vehiculo> vehiculos) {
		System.out.println("Vehículos ordenados por precio de mayor a menor:");
		Collections.sort(vehiculos);
		for (Vehiculo vehiculo : vehiculos) {
			System.out.println(vehiculo.mostrarMarcaModelo());
		}
	}

}
