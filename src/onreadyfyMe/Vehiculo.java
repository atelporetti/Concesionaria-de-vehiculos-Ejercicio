package onreadyfyMe;

import java.text.DecimalFormat;

public class Vehiculo implements Comparable<Vehiculo> {
	private String marca;
	private String modelo;
	private double precio;

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	public Vehiculo() {
	}

	public Vehiculo(String marca, String modelo, double precio) {
		this.marca = marca;
		this.modelo = modelo;
		this.precio = precio;
	}

	public void mostrarTodosDatos() {
		DecimalFormat formatea = new DecimalFormat("###,###.00");
		System.out.println(
				"Marca: " + getMarca() + " // Modelo: " + getModelo() + " // Precio: $" + formatea.format(getPrecio()));
	}

	public String mostrarMarcaModelo() {
		String marcaModelo = getMarca() + " " + getModelo();
		return marcaModelo;
	}

	@Override
	public int compareTo(Vehiculo v) {
		if (this.precio > v.precio) {
			return -1;
		}
		if (this.precio < v.precio) {
			return 1;
		}
		return 0;
	}

}
