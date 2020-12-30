package onreadyfyMe;

import java.text.DecimalFormat;

public class Moto extends Vehiculo {
	private String cilindrada;

	public String getCilindrada() {
		return cilindrada;
	}

	public void setCilindrada(String cilindrada) {
		this.cilindrada = cilindrada;
	}

	public Moto(String marca, String modelo, double precio, String cilindrada) {
		super(marca, modelo, precio);
		this.cilindrada = cilindrada;
	}

	public Moto() {
	}

	@Override
	public void mostrarTodosDatos() {
		DecimalFormat formatea = new DecimalFormat("###,###.00");
		System.out.println("Marca: " + getMarca() + " // Modelo: " + getModelo() + " // Cilindrada: " + getCilindrada()
				+ " // Precio: $" + formatea.format(getPrecio()));
	}

}