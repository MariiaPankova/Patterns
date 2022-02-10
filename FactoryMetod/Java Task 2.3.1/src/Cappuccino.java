public class Cappuccino extends Drink{
    @Override
    public int sell() {
        return this.sell_cost - this.component_cost;
    }

    public Cappuccino(int component_cost, int sell_cost) {
        this.component_cost = component_cost;
        this.sell_cost = sell_cost;
    }
}
