public class Pizzaiolo {

    private static Pizzaiolo instance;
    private final ConcreteBuilder builder = new ConcreteBuilder();
    private final String name;

    private Pizzaiolo(String name){
        this.name = name;
    }


    public static Pizzaiolo getInstance(String name){
        if (instance == null){
            instance = new Pizzaiolo(name);
        }
        return instance;
    }

    @Override
    public String toString() {
        return name;
    }

    public Pizza pepperoni(){
        return builder.reset()
                .addIngredient(Pizza.Filling.SAUSAGES, 100)
                .addIngredient(Pizza.Filling.CHEESE, 10)
                .getResult();

    }

    public Pizza cheese(){
        return builder.reset()
                .chooseDough(new Dough(Dough.FlourType.CORN, Dough.DoughType.THICK))
                .addIngredient(Pizza.Filling.CHEESE,100)
                .getResult();
    }

    public Pizza olive(){
        return builder.reset()
                .chooseDough(new Dough(Dough.FlourType.RYE, Dough.DoughType.THICK))
                .addIngredient(Pizza.Filling.OLIVES,3)
                .getResult();
    }
}
