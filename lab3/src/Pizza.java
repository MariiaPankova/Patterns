import java.util.HashMap;

public class Pizza {
    enum Filling{
        CHEESE,
        OLIVES,
        SAUSAGES
    }

    private final HashMap<Filling,Integer>  ingredients;
    private final Dough dough;

    public Pizza(HashMap<Filling,Integer> ingredients, Dough dough) {
        this.dough = dough;
        this.ingredients = ingredients;
    }
    public String toString() {
        return "Pizza with " + ingredients.toString() + "  " + dough.toString();
    }
}
