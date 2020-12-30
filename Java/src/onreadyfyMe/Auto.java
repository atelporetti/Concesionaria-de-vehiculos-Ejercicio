package onreadyfyMe;

import java.text.DecimalFormat;

public class Auto extends Vehiculo {
	private String puertas;

	public String getPuertas() {
		return puertas;
	}

	public void setPuertas(String puertas) {
		this.puertas = puertas;
	}

	public Auto(String marca, String modelo, double precio, String puertas) {
		super(marca, modelo, precio);
		this.puertas = puertas;
	}

	public Auto() {
	}

	public void mostrarTodosDatos() {
		DecimalFormat formatea = new DecimalFormat("###,###.00");
		System.out.println("Marca: " + getMarca() + " // Modelo: " + getModelo() + " // Puertas: " + getPuertas()
				+ " // Precio: $" + formatea.format(getPrecio()));
	}

}