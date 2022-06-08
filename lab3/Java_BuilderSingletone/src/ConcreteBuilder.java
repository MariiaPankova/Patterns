import java.util.HashMap;

public class ConcreteBuilder implements Builder {
    Dough dough;
    HashMap<Pizza.Filling,Integer> ingredients;

    public ConcreteBuilder() {
        reset();
    }

    @Override
    public ConcreteBuilder reset() {
        ingredients = new HashMap<>();
        dough = new Dough(Dough.FlourType.WHEAT, Dough.DoughType.THIN);
        return this;
    }

    @Override
    public Pizza getResult() {
        return new Pizza(ingredients, dough);
    }

    @Override
    public ConcreteBuilder chooseDough(Dough dough) {
        this.dough = dough;
        return this;
    }

    @Override
    public ConcreteBuilder addIngredient(Pizza.Filling filling, int num) {
        this.ingredients.put(filling, num);
        return this;
    }

}
