public class CafeAmericano extends Cafe {
    @Override
    public Drink make_coffee(){
        return new Americano(4, 25);
    }
}
