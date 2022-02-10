public class CafeLatte extends Cafe{
    @Override
    public Drink make_coffee(){
        return new Latte(5, 45);
    }
}
