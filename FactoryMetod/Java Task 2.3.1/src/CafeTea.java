public class CafeTea extends Cafe{
    @Override
    public Drink make_coffee(){
        return new Tea(1, 15);
    }
}
