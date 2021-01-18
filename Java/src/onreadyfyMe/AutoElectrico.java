package onreadyfyMe;

import java.text.DecimalFormat;

public class AutoElectrico extends Auto {
	private String voltaje;

	public String getVoltaje() {
		return voltaje;
	}

	public void setVoltaje(String voltaje) {
		this.voltaje = voltaje;
	}

	public AutoElectrico(String marca, String modelo, double precio, String puertas, String voltaje) {
		super(marca, modelo, precio, puertas);
		this.voltaje = voltaje;
	}

	public AutoElectrico() {
	}

	@Override
	public void mostrarTodosDatos() {
		DecimalFormat formatea = new DecimalFormat("###,###.00");
		System.out.println("Marca: " + getMarca() + " // Modelo: " + getModelo() + " // Puertas: " + getPuertas()
				+ " // Precio: $" + formatea.format(getPrecio()) + " // Voltaje: " + getVoltaje());
	}

	@Override
	public boolean esLujo() {
		boolean esLujo = false;
		if ((int) Double.parseDouble(getVoltaje().substring(0, 3)) >= 240) {
			return esLujo = true;
		}
		return esLujo;
	}
}
