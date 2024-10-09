class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private int velocidade; 

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0; 
    }

    public void acelerar(int incremento) {
        this.velocidade += incremento;
        System.out.println("Acelerando. Velocidade atual: " + this.velocidade + " km/h");
    }

    public void frear(int decremento) {
        this.velocidade -= decremento;
        if (this.velocidade < 0) {
            this.velocidade = 0; 
        }
        System.out.println("Freando. Velocidade atual: " + this.velocidade + " km/h");
    }

    public void exibirVelocidade() {
        System.out.println("Velocidade atual: " + this.velocidade + " km/h");
    }

    public void exibirDetalhes() {
        System.out.println("Marca: " + this.marca + ", Modelo: " + this.modelo + ", Ano: " + this.ano);
    }

    public static void main(String[] args) {
        
        Carro carro1 = new Carro("Toyota", "Corolla", 2020);
        Carro carro2 = new Carro("Honda", "Civic", 2021);
        Carro carro3 = new Carro("Ford", "Focus", 2019);

        
        carro1.exibirDetalhes();
        carro2.exibirDetalhes();
        carro3.exibirDetalhes();

        
        carro1.acelerar(50);
        carro1.frear(20);
        carro1.exibirVelocidade();
        carro1.frear(40); 
    }
}
