public class Americano extends Drink{
    @Override
    public int sell() {
        return this.sell_cost - this.component_cost;
    }

    public Americano(int component_cost, int sell_cost) {
        this.component_cost = component_cost;
        this.sell_cost = sell_cost;
    }
}
