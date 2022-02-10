public class CafeEspresso extends Cafe{
    @Override
    public Drink make_coffee(){
        return new Espresso(3, 15);
    }
}
