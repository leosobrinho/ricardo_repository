// Classe Motor
class Motor {
    private String tipo; 
    private int potencia; 

    public Motor(String tipo, int potencia) {
        this.tipo = tipo;
        this.potencia = potencia;
    }

    public String getTipo() {
        return tipo;
    }

    public int getPotencia() {
        return potencia;
    }

    public void exibirDetalhes() {
        System.out.println("Motor tipo: " + tipo + ", Potência: " + potencia + " CV");
    }
}


class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private Motor motor; 

    public Carro(String marca, String modelo, int ano, Motor motor) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.motor = motor; 
    }

    public void exibirDetalhes() {
        System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Ano: " + ano);
        motor.exibirDetalhes(); 
    }

    public static void main(String[] args) {
        
        Motor motor1 = new Motor("Gasolina", 120);

        
        Carro carro1 = new Carro("Toyota", "Corolla", 2020, motor1);

      
        carro1.exibirDetalhes();
    }
}
