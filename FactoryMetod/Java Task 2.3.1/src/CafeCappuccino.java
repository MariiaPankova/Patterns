public class CafeCappuccino extends Cafe{
    @Override
    public Drink make_coffee(){
        return new Cappuccino(4, 20);
    }
}
