public class Main {
    public static void main(String[] args) {
        Pizzaiolo director = Pizzaiolo.getInstance("Kevin");
        Pizzaiolo director2 = Pizzaiolo.getInstance("Not Kevin");
        System.out.println(director.toString() + director2.toString());
        Pizza pizza = director.pepperoni();
        System.out.println(pizza);

        Pizza pizza1 = director.cheese();
        System.out.println(pizza1);

        Pizza pizza2 = director.olive();
        System.out.println(pizza2);
    }
}

